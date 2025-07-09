import socket
import threading

# 서버 설정
HOST = '0.0.0.0'
PORT = 65432

def handle_client(conn, addr):
    """
    클라이언트와의 통신을 처리하는 함수
    각 클라이언트는 별도의 스레드에서 실행됨
    """
    print(f"New connection from {addr}")
    
    try:
        while True:
            # conn.recv(): 클라이언트로부터 데이터 수신
            data = conn.recv(1024)
            
            # 데이터가 없으면 클라이언트가 연결을 끊은 것
            if not data:
                break
            
            print(f"Received from {addr}: {data.decode('utf-8')}")
            
            # 에코 응답 전송
            response = f"Echo: {data.decode('utf-8')}"
            conn.sendall(response.encode('utf-8'))
            
    except ConnectionResetError:
        print(f"Client {addr} disconnected unexpectedly")
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        # 연결 종료
        conn.close()
        print(f"Connection with {addr} closed")

def main():
    # socket.socket() 생성자로 서버 소켓 생성
    # - socket.AF_INET: IPv4 주소 체계
    # - socket.SOCK_STREAM: TCP 소켓
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # socket.SO_REUSEADDR: 소켓 주소 재사용 허용
        # 서버 재시작 시 "Address already in use" 에러 방지
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # 서버 소켓을 주소와 포트에 바인딩
        server_socket.bind((HOST, PORT))
        
        # 소켓을 수신 대기 상태로 설정
        # 백로그 크기를 5로 설정 (대기 중인 연결 요청 최대 5개)
        server_socket.listen(5)
        
        print(f"Multi-client server is running on {HOST}:{PORT}")
        print("Waiting for connections...")
        
        try:
            while True:
                # 새로운 클라이언트 연결 수락
                conn, addr = server_socket.accept()
                
                # 각 클라이언트를 별도의 스레드에서 처리
                # target: 실행할 함수
                # args: 함수에 전달할 인수
                # daemon=True: 메인 프로그램 종료 시 스레드도 함께 종료
                client_thread = threading.Thread(
                    target=handle_client, 
                    args=(conn, addr),
                    daemon=True
                )
                client_thread.start()
                
        except KeyboardInterrupt:
            print("\nServer shutting down...")
        except Exception as e:
            print(f"Server error: {e}")

if __name__ == "__main__":
    main() 