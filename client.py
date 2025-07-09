import socket

# 서버 연결 설정
HOST = '127.0.0.1'  # 로컬호스트 (서버가 같은 컴퓨터에서 실행 중)
PORT = 65432        # 서버와 같은 포트 번호

# socket.socket() 생성자로 클라이언트 소켓 생성
# - socket.AF_INET: IPv4 주소 체계
# - socket.SOCK_STREAM: TCP 소켓 (연결 지향적)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # s.connect(): 서버에 연결 요청
    # 서버의 주소와 포트로 연결 시도
    s.connect((HOST, PORT))
    
    print(f"Connected to server {HOST}:{PORT}")
    
    # 사용자로부터 메시지 입력받기
    while True:
        message = input("Enter message (or 'quit' to exit): ")
        
        if message.lower() == 'quit':
            break
        
        # s.sendall(): 서버로 데이터 전송
        # 문자열을 바이트로 인코딩하여 전송
        s.sendall(message.encode('utf-8'))
        
        # s.recv(): 서버로부터 응답 수신
        # 최대 1024바이트까지 수신
        data = s.recv(1024)
        
        # 받은 데이터를 문자열로 디코딩하여 출력
        print(f"Received from server: {data.decode('utf-8')}")
    
    print("Connection closed.") 