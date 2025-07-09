import socket

# 서버 설정
HOST = '0.0.0.0'    # 모든 인터페이스에서 접속을 허용 (localhost: '127.0.0.1')
PORT = 65432        # 서버가 사용할 포트 번호

# socket.socket() 생성자 파라미터:
# - socket.AF_INET: IPv4 주소 체계 사용
# - socket.SOCK_STREAM: TCP 소켓 (연결 지향적, 신뢰성 있는 통신)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # s.bind(): 소켓을 특정 주소와 포트에 바인딩
    # 소켓이 해당 주소와 포트에서 들어오는 연결을 수신할 수 있게 함
    s.bind((HOST, PORT))
    
    # s.listen(): 소켓을 수신 대기 상태로 설정
    # 클라이언트의 연결 요청을 기다리는 상태가 됨
    s.listen()
    print(f"Server is running on {HOST}:{PORT}...")
    
    # s.accept(): 클라이언트 연결 요청을 수락
    # 반환값: (conn, addr) - 연결된 소켓 객체와 클라이언트 주소
    conn, addr = s.accept()
    
    # 연결된 클라이언트와 통신
    with conn:
        print(f"Connected by {addr}")
        
        # 클라이언트로부터 데이터를 계속 수신
        while True:
            # conn.recv(bufsize): 클라이언트로부터 데이터 수신
            # bufsize만큼의 데이터를 받을 수 있음 (최대 1024바이트)
            data = conn.recv(1024)
            
            # 데이터가 없으면 클라이언트가 연결을 끊은 것
            if not data:
                break
                
            print(f"Received data: {data}")
            
            # conn.sendall(data): 클라이언트에게 데이터 전송
            # 모든 데이터를 전송할 때까지 반복 (에코 서버)
            conn.sendall(data)