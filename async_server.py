import asyncio
import socket

# 서버 설정
HOST = '0.0.0.0'
PORT = 65432

async def handle_client(reader, writer):
    """
    비동기로 클라이언트를 처리하는 함수
    
    Args:
        reader: asyncio.StreamReader - 데이터 읽기용
        writer: asyncio.StreamWriter - 데이터 쓰기용
    """
    # 클라이언트 주소 정보 가져오기
    addr = writer.get_extra_info('peername')
    print(f"New async connection from {addr}")
    
    try:
        while True:
            # 비동기적으로 데이터 읽기
            # reader.read(n): 최대 n바이트 읽기
            data = await reader.read(1024)
            
            # 클라이언트가 연결을 끊으면 빈 바이트가 반환됨
            if not data:
                break
            
            message = data.decode('utf-8')
            print(f"Received from {addr}: {message}")
            
            # 에코 응답 생성
            response = f"Async Echo: {message}"
            
            # 비동기적으로 데이터 쓰기
            # writer.write(): 데이터를 버퍼에 쓰기
            writer.write(response.encode('utf-8'))
            
            # writer.drain(): 버퍼의 데이터를 실제로 전송
            await writer.drain()
            
    except asyncio.CancelledError:
        print(f"Connection with {addr} was cancelled")
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        # 연결 종료
        print(f"Closing connection with {addr}")
        writer.close()
        await writer.wait_closed()

async def main():
    """
    메인 비동기 함수 - 서버 시작
    """
    print(f"Starting async server on {HOST}:{PORT}")
    
    try:
        # asyncio.start_server(): 비동기 서버 시작
        # handle_client: 각 클라이언트 연결에 대해 호출될 함수
        server = await asyncio.start_server(
            handle_client,      # 클라이언트 핸들러 함수
            HOST,              # 바인딩할 호스트
            PORT,              # 바인딩할 포트
            reuse_address=True  # 주소 재사용 허용
        )
        
        # 서버가 수신 대기 중인 주소들 출력
        addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
        print(f"Async server is serving on {addrs}")
        
        # 서버가 영구적으로 실행되도록 함
        # server.serve_forever(): 서버를 무한히 실행
        await server.serve_forever()
        
    except KeyboardInterrupt:
        print("\nShutting down async server...")
    except Exception as e:
        print(f"Server error: {e}")

def run_async_server():
    """
    비동기 서버 실행 함수
    """
    try:
        # asyncio.run(): 비동기 함수 실행
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nAsync server stopped")

if __name__ == "__main__":
    run_async_server()

"""
비동기 소켓 프로그래밍 특징:

1. 단일 스레드 동시성:
   - 스레드 생성 없이 많은 연결 처리 가능
   - 이벤트 루프 기반으로 효율적

2. 논블로킹 I/O:
   - I/O 작업 중 다른 작업 처리 가능
   - await 키워드로 비동기 대기

3. 메모리 효율성:
   - 스레드 생성 비용 없음
   - 컨텍스트 스위칭 오버헤드 없음

4. 확장성:
   - 수천 개의 동시 연결 처리 가능
   - C10K 문제 해결에 적합

주요 asyncio 소켓 함수들:

- asyncio.start_server(): 비동기 서버 시작
- asyncio.open_connection(): 비동기 클라이언트 연결
- reader.read(n): 비동기 데이터 읽기
- writer.write(data): 비동기 데이터 쓰기
- writer.drain(): 버퍼 플러시
- writer.close(): 연결 종료
- writer.wait_closed(): 연결 종료 대기

사용 예시:
$ python async_server.py
그 다음 다른 터미널에서:
$ telnet localhost 65434
""" 