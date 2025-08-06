# 소켓 프로그래밍 실습 가이드

## 📋 실습 파일 목록

1. **server.py** - 기본 TCP 에코 서버 (단일 클라이언트)
2. **client.py** - 기본 TCP 클라이언트
3. **multi_client_server.py** - 멀티 클라이언트 TCP 서버 (threading 사용)
4. **udp_server.py** - UDP 에코 서버
5. **udp_client.py** - UDP 클라이언트
6. **async_server.py** - 비동기 TCP 서버 (asyncio 사용)
7. **socket_methods_example.py** - 소켓 메소드 및 옵션 실습

## 🚀 실습 순서

### 1. 기본 TCP 통신 실습

#### 서버 실행:
```bash
python server.py
```

#### 클라이언트 실행 (새 터미널):
```bash
python client.py
```

**실습 내용:**
- 서버가 클라이언트 연결을 수락하는 과정 관찰
- 메시지 전송 및 에코 응답 확인
- 한 번에 하나의 클라이언트만 처리되는 것 확인

### 2. 멀티 클라이언트 서버 실습

#### 서버 실행:
```bash
python multi_client_server.py
```

#### 여러 클라이언트 실행 (각각 새 터미널):
```bash
python client.py
python client.py
python client.py
```

**실습 내용:**
- 여러 클라이언트가 동시에 접속 가능한지 확인
- 각 클라이언트가 독립적으로 메시지 전송 가능한지 테스트
- 스레드 기반 동시성 처리 관찰

### 3. UDP 통신 실습

#### UDP 서버 실행:
```bash
python udp_server.py
```

#### UDP 클라이언트 실행 (새 터미널):
```bash
python udp_client.py
```

**실습 내용:**
- 연결 없는 통신 방식 체험
- TCP와 UDP의 차이점 비교
- 데이터그램 기반 통신 이해

### 4. 비동기 서버 실습

#### 비동기 서버 실행:
```bash
python async_server.py
```

#### 테스트 방법:
1. **텔넷 사용:**
   ```bash
   telnet localhost 65434
   ```

2. **기본 클라이언트 사용 (포트 변경):**
   - client.py의 PORT를 65434로 변경하고 실행

**실습 내용:**
- 단일 스레드에서 여러 클라이언트 처리
- 비동기 I/O 성능 비교
- 이벤트 루프 기반 동시성 이해

### 5. 소켓 메소드 실습

#### 실행:
```bash
python socket_methods_example.py
```

**실습 내용:**
- 다양한 소켓 메소드 동작 확인
- 소켓 옵션 설정 및 조회
- 주소 패밀리 및 소켓 타입 이해
- 호스트명 해석 기능 테스트

## 🔧 추가 테스트 방법

### 1. 텔넷을 사용한 수동 테스트
```bash
telnet localhost 65432
```
- 서버에 직접 연결하여 수동으로 메시지 전송
- 서버 응답 확인

### 2. 파이썬 인터프리터에서 테스트
```python
import socket

# 클라이언트 소켓 생성
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 65432))

# 메시지 전송
s.sendall(b'Hello, Server!')

# 응답 수신
data = s.recv(1024)
print(f'Received: {data.decode()}')

s.close()
```

### 3. 네트워크 모니터링
```bash
# 포트 사용 현황 확인
netstat -an | grep :65432

# 프로세스별 포트 사용 확인
lsof -i :65432
```

## 🎯 심화 실습 과제

### 1. 채팅 서버 구현
- 멀티 클라이언트 서버를 확장하여 브로드캐스트 기능 추가
- 클라이언트 간 메시지 중계 기능 구현

### 2. 파일 전송 서버
- 바이너리 데이터 전송 처리
- 파일 크기 정보 선전송 후 파일 데이터 전송

### 3. HTTP 서버 구현
- 간단한 HTTP 요청/응답 처리
- 정적 파일 서빙 기능

### 4. 프로토콜 설계
- 사용자 정의 프로토콜 구현
- 메시지 헤더 및 페이로드 구조 설계

## 🐛 트러블슈팅

### 1. "Address already in use" 오류
```python
# 서버 소켓에 SO_REUSEADDR 옵션 추가
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
```

### 2. 연결 타임아웃 오류
```python
# 클라이언트 소켓에 타임아웃 설정
client_socket.settimeout(10.0)  # 10초 타임아웃
```

### 3. 데이터 인코딩 오류
```python
# 문자열 → 바이트: encode()
message.encode('utf-8')

# 바이트 → 문자열: decode()
data.decode('utf-8')
```

## 📚 핵심 개념 요약

### TCP vs UDP
| 특징 | TCP | UDP |
|------|-----|-----|
| 연결 방식 | 연결 지향 | 연결 없음 |
| 신뢰성 | 높음 | 낮음 |
| 속도 | 느림 | 빠름 |
| 순서 보장 | 보장 | 보장 안됨 |
| 사용 예시 | 웹, 이메일 | 게임, 스트리밍 |

### 동시성 처리 방식
1. **단일 스레드**: 한 번에 하나의 클라이언트만 처리
2. **멀티 스레드**: 각 클라이언트를 별도 스레드에서 처리
3. **비동기**: 이벤트 루프 기반 단일 스레드 동시성

### 소켓 상태 전이
```
[생성] → [바인딩] → [리스닝] → [수락] → [연결] → [데이터 전송] → [종료]
```

## 🔍 성능 비교 실습

각 서버 방식의 성능을 비교해보세요:

1. **부하 테스트**: 동시 클라이언트 수 증가시켜 테스트
2. **메모리 사용량**: 각 방식의 메모리 사용량 비교
3. **응답 시간**: 클라이언트 응답 시간 측정

## 💡 실습 팁

1. **로그 추가**: 각 단계별 로그를 추가하여 동작 과정 이해
2. **에러 처리**: 다양한 예외 상황에 대한 처리 추가
3. **설정 파일**: 호스트, 포트 등을 설정 파일로 분리
4. **단위 테스트**: 각 기능별 테스트 케이스 작성 

---

## 🌐 웹서버 아키텍처와 우리 실습 코드 비교

### 📌 비동기 TCP 서버와 실제 웹서버의 관계

**질문**: 우리의 `async_server.py`가 실제 웹서버가 사용하는 방식인가요?

**답변**: **부분적으로 맞습니다!** 현대의 고성능 웹서버들(Nginx, Node.js)은 우리와 동일한 이벤트 루프 기반 비동기 방식을 사용합니다.

### 🏗️ 주요 웹서버 아키텍처 분석

#### **1. Apache HTTP Server - 다중 처리 모듈 (MPM)**

##### 🔄 **Prefork MPM** (프로세스 기반)
```
Master Process
├── Worker Process 1 ── 클라이언트 A
├── Worker Process 2 ── 클라이언트 B  
├── Worker Process 3 ── 클라이언트 C
└── Worker Process N ── 클라이언트 N
```

**특징 및 우리 실습과의 관계:**
- 각 클라이언트마다 별도의 프로세스 생성
- 안정성이 높지만 메모리 사용량이 높음
- **우리의 `server.py`(단일 클라이언트)와 유사한 개념**

##### 🧵 **Worker MPM** (스레드 기반)
```
Master Process
├── Worker Process 1
│   ├── Thread 1 ── 클라이언트 A
│   ├── Thread 2 ── 클라이언트 B
│   └── Thread N ── 클라이언트 N
└── Worker Process 2
    ├── Thread 1 ── 클라이언트 X
    └── Thread N ── 클라이언트 Y
```

**특징 및 우리 실습과의 관계:**
- 프로세스 내에서 다중 스레드로 처리
- **우리의 `multi_client_server.py`와 동일한 방식!** ✅

##### ⚡ **Event MPM** (이벤트 기반 하이브리드)
```
Master Process
├── Worker Process 1 (Event Loop)
│   ├── Keep-Alive 연결들 (이벤트 처리)
│   └── Thread Pool ── 실제 요청 처리
└── Worker Process 2 (Event Loop)
    ├── Keep-Alive 연결들
    └── Thread Pool
```

**특징 및 우리 실습과의 관계:**
- **우리의 `async_server.py`와 매우 유사!** ✅
- Keep-Alive 연결은 이벤트 루프로 처리
- 실제 요청 처리는 스레드 풀 사용

#### **2. Nginx - 이벤트 기반 아키텍처**

```
Master Process
├── Worker Process 1 (Event Loop)
├── Worker Process 2 (Event Loop) 
├── Worker Process 3 (Event Loop)
└── Worker Process N (Event Loop)
```

**특징 및 우리 실습과의 관계:**
- **우리의 `async_server.py`와 거의 동일한 패턴!** ✅
- 각 워커 프로세스가 이벤트 루프 실행
- 비동기 I/O로 수천 개의 동시 연결 처리
- 메모리 사용량이 매우 적음

#### **3. Node.js - 단일 스레드 이벤트 루프**

```
Main Thread (Event Loop)
├── 클라이언트 A (비동기 처리)
├── 클라이언트 B (비동기 처리)
├── 클라이언트 C (비동기 처리)
└── Thread Pool (I/O 작업용)
```

**특징 및 우리 실습과의 관계:**
- **우리의 `async_server.py`와 거의 동일한 패턴!** ✅
- 단일 스레드에서 모든 요청 처리
- libuv 라이브러리 사용

### 📊 성능 및 특성 비교

| 아키텍처 | 동시 연결 | 메모리 사용 | CPU 사용 | 우리 실습 파일 |
|----------|-----------|-------------|----------|---------------|
| **프로세스 기반** | 낮음 (~1K) | 높음 | 높음 | `server.py` |
| **스레드 기반** | 중간 (~5K) | 중간 | 중간 | `multi_client_server.py` |
| **이벤트 기반** | 높음 (~10K+) | 낮음 | 낮음 | **`async_server.py`** ✅ |

### 🔍 코드 레벨 비교

#### **우리의 `async_server.py`:**
```python
async def handle_client(reader, writer):
    while True:
        data = await reader.read(1024)  # 비동기 I/O
        # 에코 처리
        writer.write(response.encode('utf-8'))
        await writer.drain()
```

#### **Nginx의 실제 구조 (개념적 유사성):**
```c
// Nginx 이벤트 루프 (단순화)
while (1) {
    epoll_wait(epfd, events, maxevents, timeout);  // 이벤트 대기
    
    for (각 이벤트) {
        if (읽기 가능) {
            parse_http_request();     // HTTP 파싱
            serve_static_file();      // 파일 서빙
        }
        if (쓰기 가능) {
            send_http_response();     // HTTP 응답
        }
    }
}
```

#### **Node.js HTTP 서버:**
```javascript
const server = http.createServer(async (req, res) => {
    // 우리의 handle_client와 유사한 비동기 처리
    const data = await processRequest(req);
    res.end(data);
});
```

### 🎯 실제 프로덕션에서의 사용

#### **우리의 비동기 방식을 사용하는 웹서버들:**
- **Nginx**: 세계에서 가장 많이 사용되는 웹서버
- **Node.js**: JavaScript 런타임 환경
- **Python uvicorn**: FastAPI 등 ASGI 애플리케이션 서버
- **Go HTTP 서버**: 고루틴 기반 동시성

#### **전통적인 방식을 사용하는 웹서버들:**
- **Apache with PHP**: WordPress 등 대부분의 PHP 사이트
- **IIS**: Windows 기반 웹서버
- **Tomcat**: Java 웹 애플리케이션 서버

### 💡 실제 웹서버와의 차이점

#### **우리 코드가 가진 것:**
- ✅ **이벤트 루프 기반 비동기 I/O** (핵심!)
- ✅ **높은 동시성 처리 능력**
- ✅ **낮은 메모리 사용량**
- ✅ **현대 웹서버와 동일한 아키텍처 패턴**

#### **실제 웹서버가 추가로 가진 것:**
- HTTP 프로토콜 파싱 (`GET /index.html HTTP/1.1`)
- 정적 파일 서빙 (HTML, CSS, JS 파일)
- 가상 호스트, SSL/TLS, 압축, 캐싱
- 리버스 프록시, 로드 밸런싱
- 보안, 인증, 로깅, 미들웨어

### 🚀 실습으로 성능 확인하기

#### **비동기 서버 동시 연결 테스트:**
```bash
# 터미널 1: 비동기 서버 실행
python async_server.py

# 터미널 2: 동시 연결 테스트
for i in {1..100}; do
    echo "Client $i" | nc localhost 65434 &
done
```

#### **각 서버 방식별 성능 비교:**
```bash
# 1. 단일 클라이언트 서버
python server.py
# → 한 번에 하나의 클라이언트만 처리

# 2. 멀티 스레드 서버  
python multi_client_server.py
# → 스레드 수만큼 동시 처리

# 3. 비동기 서버
python async_server.py
# → 수천 개의 동시 연결 처리 가능
```

### ✅ 결론

**우리의 `async_server.py`는 현대 고성능 웹서버의 핵심 아키텍처를 정확히 구현하고 있습니다!**

1. **Nginx, Node.js와 동일한 이벤트 루프 방식**
2. **높은 동시성과 낮은 리소스 사용량**
3. **실제 프로덕션에서 널리 사용되는 패턴**

### 📚 추가 학습 방향

실습 코드를 더 발전시키고 싶다면:

1. **HTTP 서버 구현**: `async_server.py`에 HTTP 프로토콜 파싱 추가
2. **정적 파일 서빙**: HTML, CSS, JS 파일 서빙 기능
3. **미들웨어 패턴**: 요청/응답 처리 체인 구현
4. **웹소켓 지원**: 실시간 양방향 통신 구현
5. **리버스 프록시**: 백엔드 서버로 요청 전달

**우리 코드는 이러한 고성능 웹서버들의 "심장부"를 학습하기에 완벽한 예제입니다!** 🎉

## 🎯 웹 개발자를 위한 소켓 기반 추가 학습 방향

현재 프로젝트의 `async_server.py`를 기반으로 각 방향을 상세히 설명합니다.

### 1. **HTTP 서버 구현** 📡

#### **현재 상태:**
```python
# async_server.py - 단순 에코 서버
data = await reader.read(1024)
response = f"Async Echo: {message}"
writer.write(response.encode('utf-8'))
```

#### **HTTP 프로토콜 파싱 추가:**
```python
async def handle_http_client(reader, writer):
    # HTTP 요청 파싱
    request_line = await reader.readline()
    request_line = request_line.decode('utf-8').strip()
    
    # GET /index.html HTTP/1.1 파싱
    method, path, version = request_line.split()
    
    # 헤더 파싱
    headers = {}
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        key, value = line.decode('utf-8').split(':', 1)
        headers[key.strip()] = value.strip()
    
    # HTTP 응답 생성
    response = f"""HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: {len(html_content)}

{html_content}"""
    
    writer.write(response.encode('utf-8'))
    await writer.drain()
```

**학습 포인트:**
- HTTP 요청/응답 구조 이해
- 프로토콜 파싱 로직 구현
- 상태 코드, 헤더 처리

### 2. **정적 파일 서빙** 📁

#### **파일 시스템 연동:**
```python
import os
import mimetypes

async def serve_static_file(path):
    # 보안: 경로 검증
    if '..' in path or path.startswith('/'):
        return create_404_response()
    
    file_path = os.path.join('static', path)
    
    # 파일 존재 확인
    if not os.path.exists(file_path):
        return create_404_response()
    
    # MIME 타입 결정
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        mime_type = 'application/octet-stream'
    
    # 파일 읽기
    with open(file_path, 'rb') as f:
        content = f.read()
    
    # HTTP 응답 생성
    response = f"""HTTP/1.1 200 OK
Content-Type: {mime_type}
Content-Length: {len(content)}

""".encode('utf-8') + content
    
    return response
```

**학습 포인트:**
- 파일 시스템 보안 (디렉토리 트래버설 방지)
- MIME 타입 처리
- 바이너리 파일 처리

### 3. **미들웨어 패턴** 🔄

#### **요청/응답 처리 체인:**
```python
class Middleware:
    def __init__(self, app):
        self.app = app
    
    async def __call__(self, request, response):
        # 전처리
        await self.before_request(request)
        
        # 다음 미들웨어/핸들러 호출
        await self.app(request, response)
        
        # 후처리
        await self.after_request(request, response)

class LoggingMiddleware(Middleware):
    async def before_request(self, request):
        print(f"[{datetime.now()}] {request.method} {request.path}")
    
    async def after_request(self, request, response):
        print(f"[{datetime.now()}] Response: {response.status_code}")

class AuthMiddleware(Middleware):
    async def before_request(self, request):
        if request.path.startswith('/admin'):
            if not self.is_authenticated(request):
                raise UnauthorizedError()

# 미들웨어 체인 구성
app = LoggingMiddleware(
    AuthMiddleware(
        StaticFileHandler(
            RouteHandler()
        )
    )
)
```

**학습 포인트:**
- 관심사 분리 (로깅, 인증, 라우팅)
- 체인 오브 리스폰시빌리티 패턴
- 크로스 커팅 관심사 처리

### 4. **웹소켓 지원** 🔄

#### **실시간 양방향 통신:**
```python
import hashlib
import base64

async def handle_websocket(reader, writer):
    # 웹소켓 핸드셰이크
    request_headers = await parse_http_headers(reader)
    
    # Sec-WebSocket-Key 처리
    websocket_key = request_headers.get('Sec-WebSocket-Key')
    accept_key = create_websocket_accept_key(websocket_key)
    
    # 핸드셰이크 응답
    response = f"""HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: {accept_key}

"""
    writer.write(response.encode('utf-8'))
    await writer.drain()
    
    # 웹소켓 프레임 처리
    while True:
        frame = await read_websocket_frame(reader)
        if frame.opcode == 0x8:  # Close frame
            break
        elif frame.opcode == 0x1:  # Text frame
            # 브로드캐스트 또는 개별 응답
            await broadcast_message(frame.payload)

def create_websocket_accept_key(key):
    WEBSOCKET_MAGIC = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
    return base64.b64encode(
        hashlib.sha1((key + WEBSOCKET_MAGIC).encode()).digest()
    ).decode()
```

**학습 포인트:**
- 프로토콜 업그레이드 핸드셰이크
- 웹소켓 프레임 구조 이해
- 실시간 메시징 시스템

### 5. **리버스 프록시** 🔄

#### **백엔드 서버로 요청 전달:**
```python
async def handle_proxy_request(reader, writer):
    # 클라이언트 요청 파싱
    request = await parse_http_request(reader)
    
    # 로드 밸런싱: 백엔드 서버 선택
    backend_server = select_backend_server()
    
    # 백엔드 서버로 연결
    backend_reader, backend_writer = await asyncio.open_connection(
        backend_server['host'], backend_server['port']
    )
    
    # 요청 전달
    backend_writer.write(request.to_bytes())
    await backend_writer.drain()
    
    # 응답 받기
    response = await backend_reader.read(4096)
    
    # 클라이언트로 응답 전달
    writer.write(response)
    await writer.drain()
    
    # 연결 정리
    backend_writer.close()
    await backend_writer.wait_closed()

def select_backend_server():
    # 라운드 로빈, 가중치 기반 등 로드 밸런싱 로직
    backends = [
        {'host': 'localhost', 'port': 8001},
        {'host': 'localhost', 'port': 8002},
        {'host': 'localhost', 'port': 8003}
    ]
    return backends[get_next_backend_index()]
```

**학습 포인트:**
- 프록시 서버 구조 이해
- 로드 밸런싱 알고리즘
- 마이크로서비스 아키텍처

## 🎯 실제 구현 순서 추천

### **1단계: HTTP 서버**
```python
# async_http_server.py
async def handle_http_client(reader, writer):
    # HTTP 요청 파싱 + 간단한 응답
```

### **2단계: 정적 파일 서빙**
```python
# static/ 디렉토리 생성
# HTML, CSS, JS 파일 서빙
```

### **3단계: 미들웨어 추가**
```python
# 로깅, 인증, 라우팅 미들웨어
```

### **4단계: 웹소켓 지원**
```python
# 실시간 채팅 서버 구현
```

### **5단계: 리버스 프록시**
```python
# 마이크로서비스 간 통신
```

## 📊 실제 프로덕션과의 연결

| 학습 방향 | 실제 사용 예시 |
|-----------|----------------|
| **HTTP 서버** | Nginx, Apache의 HTTP 파싱 엔진 |
| **정적 파일** | CDN, 웹서버의 파일 서빙 |
| **미들웨어** | Express.js, Django, Flask 미들웨어 |
| **웹소켓** | Socket.IO, 실시간 채팅, 게임 서버 |
| **리버스 프록시** | Nginx, HAProxy, 로드 밸런서 |

## 🚀 실습 프로젝트 아이디어

### **초급 프로젝트**
1. **간단한 HTTP 서버**: GET 요청 처리 + HTML 응답
2. **정적 파일 서버**: 이미지, CSS, JS 파일 서빙
3. **에코 챗봇**: 사용자 입력에 대한 응답 서버

### **중급 프로젝트**
1. **RESTful API 서버**: JSON 요청/응답 처리
2. **실시간 채팅**: 웹소켓 기반 그룹 채팅
3. **파일 업로드 서버**: 멀티파트 폼 데이터 처리

### **고급 프로젝트**
1. **마이크로서비스 게이트웨이**: 여러 백엔드 서비스 라우팅
2. **스트리밍 서버**: 대용량 파일 스트리밍
3. **로드 밸런서**: 여러 백엔드 서버 간 부하 분산

## 💡 개발 도구 및 라이브러리

### **성능 측정 도구**
```bash
# 부하 테스트
ab -n 1000 -c 10 http://localhost:8000/

# 연결 모니터링
netstat -an | grep :8000

# 메모리 사용량
ps aux | grep python
```

### **유용한 Python 라이브러리**
```python
# HTTP 파싱
import http.server
import urllib.parse

# 비동기 HTTP 클라이언트
import aiohttp

# 웹소켓 라이브러리
import websockets

# 성능 프로파일링
import cProfile
import asyncio
```

## 🎓 학습 목표 및 성과

### **핵심 학습 목표**
1. **소켓 프로그래밍 마스터**: TCP/UDP 소켓 완전 이해
2. **비동기 프로그래밍**: 이벤트 루프와 코루틴 활용
3. **네트워크 프로토콜**: HTTP, WebSocket 프로토콜 구현
4. **서버 아키텍처**: 확장 가능한 서버 설계 패턴
5. **성능 최적화**: 동시성과 처리량 최적화

### **기대 성과**
- **웹 프레임워크 내부 동작 원리 완전 이해**
- **고성능 서버 아키텍처 설계 능력 확보**
- **실시간 애플리케이션 개발 역량 향상**
- **네트워크 관련 문제 해결 능력 강화**

**이 학습 과정을 통해 Nginx, Node.js, Django, Flask 등의 내부 동작 원리를 완전히 이해하고, 나만의 웹서버를 구현할 수 있게 됩니다!** 🚀