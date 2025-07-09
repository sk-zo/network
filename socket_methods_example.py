import socket
import sys
import time

def demonstrate_socket_methods():
    """
    소켓 객체의 주요 메소드들을 시연하는 함수
    """
    print("=== 소켓 메소드 실습 ===\n")
    
    # 1. 소켓 생성 및 기본 정보
    print("1. 소켓 생성 및 기본 정보")
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    print(f"TCP 소켓 family: {tcp_socket.family}")  # socket.AF_INET
    print(f"TCP 소켓 type: {tcp_socket.type}")      # socket.SOCK_STREAM
    print(f"UDP 소켓 family: {udp_socket.family}")  # socket.AF_INET
    print(f"UDP 소켓 type: {udp_socket.type}")      # socket.SOCK_DGRAM
    
    # 2. 소켓 옵션 설정
    print("\n2. 소켓 옵션 설정")
    
    # SO_REUSEADDR: 주소 재사용 허용
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("SO_REUSEADDR 옵션 설정됨")
    
    # SO_KEEPALIVE: 연결 유지 확인
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    print("SO_KEEPALIVE 옵션 설정됨")
    
    # 소켓 옵션 조회
    reuse_addr = tcp_socket.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    keep_alive = tcp_socket.getsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE)
    print(f"SO_REUSEADDR 값: {reuse_addr}")
    print(f"SO_KEEPALIVE 값: {keep_alive}")
    
    # 3. 소켓 바인딩 및 정보 조회
    print("\n3. 소켓 바인딩 및 정보 조회")
    
    try:
        # 바인딩 (포트 0은 자동 할당)
        tcp_socket.bind(('localhost', 0))
        
        # getsockname(): 소켓의 로컬 주소 조회
        local_addr = tcp_socket.getsockname()
        print(f"로컬 주소: {local_addr}")
        
        # listen() 시작
        tcp_socket.listen(1)
        print("리스닝 시작됨")
        
        # 소켓 상태 확인
        print(f"소켓 파일 디스크립터: {tcp_socket.fileno()}")
        
    except Exception as e:
        print(f"바인딩 오류: {e}")
    
    # 4. 타임아웃 설정
    print("\n4. 타임아웃 설정")
    
    # settimeout(): 소켓 타임아웃 설정
    tcp_socket.settimeout(5.0)  # 5초 타임아웃
    timeout_value = tcp_socket.gettimeout()
    print(f"타임아웃 값: {timeout_value}초")
    
    # 블로킹/논블로킹 모드
    tcp_socket.setblocking(False)  # 논블로킹 모드
    print("논블로킹 모드로 설정됨")
    
    tcp_socket.setblocking(True)   # 블로킹 모드
    print("블로킹 모드로 설정됨")
    
    # 5. 소켓 닫기
    print("\n5. 소켓 닫기")
    
    tcp_socket.close()
    udp_socket.close()
    print("소켓들이 닫혔습니다")

def demonstrate_socket_options():
    """
    다양한 소켓 옵션들을 시연하는 함수
    """
    print("\n=== 소켓 옵션 실습 ===\n")
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("1. 기본 소켓 옵션들")
        
        # 소켓 옵션 상수들
        options = [
            (socket.SOL_SOCKET, socket.SO_REUSEADDR, "SO_REUSEADDR - 주소 재사용"),
            (socket.SOL_SOCKET, socket.SO_KEEPALIVE, "SO_KEEPALIVE - 연결 유지"),
            (socket.SOL_SOCKET, socket.SO_BROADCAST, "SO_BROADCAST - 브로드캐스트"),
            (socket.SOL_SOCKET, socket.SO_SNDBUF, "SO_SNDBUF - 송신 버퍼 크기"),
            (socket.SOL_SOCKET, socket.SO_RCVBUF, "SO_RCVBUF - 수신 버퍼 크기"),
        ]
        
        for level, option, description in options:
            try:
                value = s.getsockopt(level, option)
                print(f"{description}: {value}")
            except Exception as e:
                print(f"{description}: 오류 - {e}")
        
        print("\n2. 소켓 옵션 설정")
        
        # 송신/수신 버퍼 크기 설정
        s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 8192)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 8192)
        
        send_buf = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
        recv_buf = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
        
        print(f"송신 버퍼 크기: {send_buf}")
        print(f"수신 버퍼 크기: {recv_buf}")

def demonstrate_address_family():
    """
    다양한 주소 패밀리를 시연하는 함수
    """
    print("\n=== 주소 패밀리 실습 ===\n")
    
    # 주소 패밀리 상수들
    families = [
        (socket.AF_INET, "AF_INET - IPv4"),
        (socket.AF_INET6, "AF_INET6 - IPv6"),
        (socket.AF_UNIX, "AF_UNIX - Unix 도메인 소켓"),
    ]
    
    for family, description in families:
        try:
            s = socket.socket(family, socket.SOCK_STREAM)
            print(f"{description}: 지원됨")
            s.close()
        except Exception as e:
            print(f"{description}: 지원되지 않음 - {e}")

def demonstrate_socket_types():
    """
    다양한 소켓 타입을 시연하는 함수
    """
    print("\n=== 소켓 타입 실습 ===\n")
    
    # 소켓 타입 상수들
    types = [
        (socket.SOCK_STREAM, "SOCK_STREAM - TCP (연결 지향)"),
        (socket.SOCK_DGRAM, "SOCK_DGRAM - UDP (데이터그램)"),
        (socket.SOCK_RAW, "SOCK_RAW - 원시 소켓"),
    ]
    
    for sock_type, description in types:
        try:
            s = socket.socket(socket.AF_INET, sock_type)
            print(f"{description}: 지원됨")
            s.close()
        except Exception as e:
            print(f"{description}: 지원되지 않음 - {e}")

def demonstrate_hostname_resolution():
    """
    호스트명 해석 관련 함수들을 시연
    """
    print("\n=== 호스트명 해석 실습 ===\n")
    
    # 호스트명 관련 함수들
    print("1. 호스트 정보 조회")
    
    try:
        # gethostname(): 로컬 호스트명 조회
        hostname = socket.gethostname()
        print(f"로컬 호스트명: {hostname}")
        
        # gethostbyname(): 호스트명을 IP 주소로 변환
        ip_address = socket.gethostbyname(hostname)
        print(f"로컬 IP 주소: {ip_address}")
        
        # getfqdn(): 완전한 도메인명 조회
        fqdn = socket.getfqdn()
        print(f"완전한 도메인명: {fqdn}")
        
    except Exception as e:
        print(f"호스트 정보 조회 오류: {e}")
    
    print("\n2. 주소 변환")
    
    try:
        # inet_aton(): IP 주소 문자열을 바이너리로 변환
        binary_ip = socket.inet_aton('127.0.0.1')
        print(f"127.0.0.1의 바이너리 표현: {binary_ip}")
        
        # inet_ntoa(): 바이너리 IP를 문자열로 변환
        string_ip = socket.inet_ntoa(binary_ip)
        print(f"바이너리를 문자열로: {string_ip}")
        
    except Exception as e:
        print(f"주소 변환 오류: {e}")

def main():
    """
    메인 함수 - 모든 실습 함수들을 실행
    """
    print("파이썬 소켓 프로그래밍 실습")
    print("=" * 40)
    
    demonstrate_socket_methods()
    demonstrate_socket_options()
    demonstrate_address_family()
    demonstrate_socket_types()
    demonstrate_hostname_resolution()
    
    print("\n실습 완료!")

if __name__ == "__main__":
    main()

"""
주요 소켓 메소드 요약:

생성 및 설정:
- socket.socket(family, type) : 소켓 생성
- setsockopt(level, option, value) : 소켓 옵션 설정
- getsockopt(level, option) : 소켓 옵션 조회
- settimeout(timeout) : 타임아웃 설정
- setblocking(flag) : 블로킹/논블로킹 모드 설정

서버 소켓:
- bind(address) : 주소와 포트에 바인딩
- listen(backlog) : 연결 대기 상태로 설정
- accept() : 클라이언트 연결 수락

클라이언트 소켓:
- connect(address) : 서버에 연결

데이터 전송 (TCP):
- send(data) : 데이터 전송
- sendall(data) : 모든 데이터 전송
- recv(bufsize) : 데이터 수신

데이터 전송 (UDP):
- sendto(data, address) : 데이터그램 전송
- recvfrom(bufsize) : 데이터그램 수신

정보 조회:
- getsockname() : 로컬 주소 조회
- getpeername() : 원격 주소 조회
- fileno() : 파일 디스크립터 조회

종료:
- close() : 소켓 닫기
- shutdown(how) : 소켓 종료
""" 