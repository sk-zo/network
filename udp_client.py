import socket

# 서버 연결 설정
HOST = '127.0.0.1'  # 로컬호스트
PORT = 65433        # UDP 서버 포트

def main():
    # socket.socket() 생성자로 UDP 클라이언트 소켓 생성
    # - socket.AF_INET: IPv4 주소 체계
    # - socket.SOCK_DGRAM: UDP 소켓 (연결 없는)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        print(f"UDP client ready to send messages to {HOST}:{PORT}")
        
        while True:
            message = input("Enter message (or 'quit' to exit): ")
            
            if message.lower() == 'quit':
                break
            
            try:
                # client_socket.sendto(): 서버로 데이터그램 전송
                # UDP는 연결 없이 바로 데이터를 전송
                # 목적지 주소를 명시해야 함
                client_socket.sendto(message.encode('utf-8'), (HOST, PORT))
                
                # client_socket.recvfrom(): 서버로부터 응답 수신
                # 반환값: (data, server_address)
                response, server_address = client_socket.recvfrom(1024)
                
                print(f"Received from {server_address}: {response.decode('utf-8')}")
                
            except ConnectionResetError:
                print("Server is not responding")
            except Exception as e:
                print(f"Error: {e}")
        
        print("UDP client closed.")

if __name__ == "__main__":
    main()

"""
UDP 클라이언트 특징:

1. 연결 설정 불필요:
   - TCP의 connect()와 달리 바로 데이터 전송 가능
   - sendto()로 목적지 주소와 함께 데이터 전송

2. 상태 없음 (Stateless):
   - 서버가 클라이언트 정보를 기억하지 않음
   - 각 패킷은 독립적으로 처리됨

3. 빠른 전송:
   - 연결 설정/해제 과정 없음
   - 헤더 오버헤드가 적음

4. 신뢰성 없음:
   - 패킷 손실, 중복, 순서 바뀜 가능
   - 애플리케이션 레벨에서 처리 필요
""" 