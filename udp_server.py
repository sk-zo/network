import socket

# 서버 설정
HOST = '0.0.0.0'
PORT = 65433

def main():
    # socket.socket() 생성자로 UDP 소켓 생성
    # - socket.AF_INET: IPv4 주소 체계
    # - socket.SOCK_DGRAM: UDP 소켓 (연결 없는, 데이터그램 기반)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        # UDP 소켓을 주소와 포트에 바인딩
        server_socket.bind((HOST, PORT))
        
        print(f"UDP server is running on {HOST}:{PORT}")
        print("Waiting for UDP packets...")
        
        try:
            while True:
                # server_socket.recvfrom(): 클라이언트로부터 데이터그램 수신
                # 반환값: (data, client_address)
                # - data: 수신된 바이트 데이터
                # - client_address: 송신자의 주소 (IP, 포트)
                data, client_address = server_socket.recvfrom(1024)
                
                print(f"Received from {client_address}: {data.decode('utf-8')}")
                
                # 에코 응답 준비
                response = f"UDP Echo: {data.decode('utf-8')}"
                
                # server_socket.sendto(): 특정 클라이언트에게 데이터그램 전송
                # UDP는 연결이 없으므로 목적지 주소를 명시해야 함
                server_socket.sendto(response.encode('utf-8'), client_address)
                
                print(f"Sent response to {client_address}")
                
        except KeyboardInterrupt:
            print("\nUDP server shutting down...")
        except Exception as e:
            print(f"UDP server error: {e}")

if __name__ == "__main__":
    main()

"""
UDP vs TCP 비교:

UDP (User Datagram Protocol):
- 연결 없는 프로토콜 (connectionless)
- 빠르지만 신뢰성이 낮음
- 데이터 손실 가능성
- 순서 보장 안됨
- 실시간 애플리케이션에 적합 (게임, 스트리밍)

TCP (Transmission Control Protocol):
- 연결 지향적 프로토콜 (connection-oriented)
- 느리지만 신뢰성이 높음
- 데이터 손실 없음
- 순서 보장됨
- 파일 전송, 웹 브라우징에 적합
""" 