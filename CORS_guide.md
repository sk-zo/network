# CORS(Cross-Origin Resource Sharing) 완벽 가이드

## CORS란?

**CORS(Cross-Origin Resource Sharing)**는 웹 브라우저에서 **다른 도메인, 포트, 프로토콜로의 요청을 제어하는 보안 정책**입니다.

## Origin(출처)이란?

Origin은 **프로토콜 + 도메인 + 포트**의 조합입니다:

```
https://example.com:8080/page
 ┬       ┬           ┬
프로토콜  도메인      포트
```

### 같은 Origin 예시:
```
현재 페이지: https://example.com:8080/index.html
요청 대상:   https://example.com:8080/api/users  ✅ 같은 Origin
```

### 다른 Origin 예시:
```
현재 페이지: https://example.com:8080/index.html
요청 대상들:
- http://example.com:8080/api     ❌ 프로토콜 다름 (https vs http)
- https://other.com:8080/api      ❌ 도메인 다름
- https://example.com:3000/api    ❌ 포트 다름
- https://example.com/api         ❌ 포트 다름 (기본포트 443 vs 8080)
```

## CORS가 필요한 이유

### 보안 위협 예시:
```html
<!-- 악성 사이트 evil.com의 페이지 -->
<script>
// 사용자가 모르게 은행 사이트에 요청
fetch('https://mybank.com/transfer', {
    method: 'POST',
    body: JSON.stringify({to: 'attacker', amount: 1000000})
});
</script>
```

- **CORS 없다면**: 악성 사이트가 마음대로 다른 사이트에 요청 가능
- **CORS 있다면**: 브라우저가 차단해서 보안 유지

## CORS 동작 과정

### 1. Simple Request (단순 요청)
특정 조건을 만족하는 요청:
- 메서드: GET, HEAD, POST만
- 헤더: Accept, Content-Type 등 기본 헤더만
- Content-Type: text/plain, application/x-www-form-urlencoded, multipart/form-data만

```javascript
// Simple Request 예시
fetch('http://api.example.com/users', {
    method: 'GET'
});
```

**과정:**
1. 브라우저가 요청에 `Origin` 헤더 추가
2. 서버가 `Access-Control-Allow-Origin` 헤더로 응답
3. 브라우저가 허용 여부 판단

### 2. Preflight Request (사전 요청)
복잡한 요청 전에 OPTIONS 요청을 먼저 보냄:

```javascript
// Preflight가 필요한 요청
fetch('http://api.example.com/users', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'  // 이 헤더 때문에 Preflight 필요
    },
    body: JSON.stringify({name: 'John'})
});
```

**과정:**
```
1. OPTIONS 요청 (Preflight)
   Browser → Server: OPTIONS /users
   Origin: http://mysite.com
   Access-Control-Request-Method: POST
   Access-Control-Request-Headers: Content-Type

2. 서버 응답
   Server → Browser: 200 OK
   Access-Control-Allow-Origin: *
   Access-Control-Allow-Methods: GET, POST, PUT
   Access-Control-Allow-Headers: Content-Type

3. 실제 POST 요청 (Preflight 성공시)
   Browser → Server: POST /users
   Content-Type: application/json
   {"name": "John"}
```

## CORS 헤더 종류

### 서버에서 보내는 헤더:
```
Access-Control-Allow-Origin: *                    # 모든 도메인 허용
Access-Control-Allow-Origin: https://mysite.com   # 특정 도메인만 허용
Access-Control-Allow-Methods: GET, POST, PUT      # 허용할 HTTP 메서드
Access-Control-Allow-Headers: Content-Type, Authorization  # 허용할 헤더
Access-Control-Allow-Credentials: true            # 쿠키 포함 요청 허용
Access-Control-Max-Age: 3600                      # Preflight 결과 캐시 시간
```

### 브라우저에서 보내는 헤더:
```
Origin: https://mysite.com                        # 요청의 출처
Access-Control-Request-Method: POST               # 실제 사용할 메서드
Access-Control-Request-Headers: Content-Type     # 실제 사용할 헤더
```

## 🚨 중요: CORS vs 서버 보안의 차이점

### CORS = 브라우저 정책 (허가증)

**CORS는 서버의 요청 처리를 막지 않습니다!** 대신 브라우저에게 "이 응답을 JavaScript에게 전달해도 된다"는 허가증을 보내는 것입니다.

#### CORS 헤더가 없을 때:
```
1. 브라우저 → 서버: 요청 전송 ✅
2. 서버: 요청 처리 ✅  
3. 서버 → 브라우저: 응답 전송 ✅
4. 브라우저: CORS 헤더 확인 → 없음 → JavaScript 접근 차단 ❌
```

#### CORS 헤더가 있을 때:
```
1. 브라우저 → 서버: 요청 전송 ✅
2. 서버: 요청 처리 ✅
3. 서버 → 브라우저: 응답 + CORS 헤더 전송 ✅
4. 브라우저: CORS 헤더 확인 → 있음 → JavaScript 접근 허용 ✅
```

### 서버 미들웨어 = 실제 보안 (실제 차단)

실제 서버 보안은 미들웨어에서 담당합니다:

```python
def handle_request(request):
    # 1. 서버 차원의 보안 검사 (실제 차단)
    auth_result = auth_middleware(request)
    if auth_result:
        return auth_result  # 401, 403 등으로 요청 자체를 거부
    
    rate_result = rate_limit_middleware(request)
    if rate_result:
        return rate_result  # 429 등으로 요청 자체를 거부
    
    # 2. 비즈니스 로직 실행
    result = process_business_logic(request)
    
    # 3. 응답 생성
    response = HTTPResponse.json(200, result)
    
    # 4. 브라우저 정책 설정 (차단이 아닌 허가)
    response.headers['Access-Control-Allow-Origin'] = 'https://myapp.com'
    
    return response
```

### 역할 분담 표

| 구분 | 서버 미들웨어 | CORS 헤더 |
|------|---------------|-----------|
| **목적** | 실제 보안/접근 제어 | 브라우저 정책 우회 |
| **대상** | 모든 클라이언트 | 브라우저만 |
| **효과** | 요청 자체를 차단 | 응답 전달 여부 결정 |
| **적용 시점** | 요청 처리 전 | 응답 생성 후 |
| **우회 가능성** | Postman으로도 차단됨 | Postman에서는 무시됨 |

### 실제 보안 아키텍처

```
Client Request
     ↓
🛡️ Server Firewall (IP 차단)
     ↓
🛡️ Load Balancer (DDoS 방어)
     ↓
🛡️ API Gateway (Rate Limiting, API Key)
     ↓
🛡️ Auth Middleware (JWT, Session)
     ↓
🛡️ Authorization (권한 체크)
     ↓
💼 Business Logic (실제 처리)
     ↓
📦 Response + CORS Headers
     ↓
🌐 Browser (CORS 정책 적용)
     ↓
JavaScript Application
```

## Python 웹 서버에서 CORS 구현

### HTTPResponse 클래스에 CORS 헤더 추가:
```python
class HTTPResponse:
    def __init__(self, status_code=200, body="", headers=None):
        self.status_code = status_code
        self.body = body
        self.headers = headers or {}
        
        # CORS 헤더 자동 추가
        self.headers.setdefault('Access-Control-Allow-Origin', '*')
        self.headers.setdefault('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.headers.setdefault('Access-Control-Allow-Headers', 'Content-Type, Authorization')
```

### OPTIONS 요청 처리:
```python
def options_handler(request):
    """CORS preflight 요청 처리"""
    return HTTPResponse(200, "", {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, Authorization"
    })

routes = {
    ('GET', '/'): index,
    ('POST', '/'): post_index,
    ('OPTIONS', '/'): options_handler,  # OPTIONS 요청 추가
}
```

## 실제 개발에서의 CORS 설정

### 개발 환경:
```python
# 모든 도메인 허용 (개발용)
'Access-Control-Allow-Origin': '*'
```

### 프로덕션 환경:
```python
# 특정 도메인만 허용 (보안)
'Access-Control-Allow-Origin': 'https://myapp.com'
```

## CORS vs Postman

**Postman이 CORS 에러가 없는 이유:**
- Postman은 브라우저가 아니라 **독립적인 HTTP 클라이언트**
- CORS는 **브라우저의 보안 정책**이므로 Postman에는 적용되지 않음
- 서버 입장에서는 브라우저든 Postman이든 똑같은 HTTP 요청

이것이 바로 **"Postman에서는 되는데 브라우저에서는 안 된다"**는 현상의 원인입니다!

## 디버깅 방법

### 브라우저 개발자 도구에서 확인:
1. **Network 탭**에서 POST 요청을 확인
2. **Response Headers**에 CORS 헤더가 있는지 확인:
   ```
   Access-Control-Allow-Origin: *
   Content-Type: application/json; charset=utf-8
   ```
3. **Console 탭**에서 CORS 관련 에러 메시지 확인

### 일반적인 CORS 에러 메시지:
```
Access to fetch at 'http://localhost:8080/' from origin 'http://localhost:3000' 
has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is 
present on the requested resource.
```

## 요약

- **CORS**는 브라우저의 보안 정책으로 다른 Origin으로의 요청을 제어
- **Same Origin Policy**를 완화하여 필요한 경우에만 cross-origin 요청 허용
- **CORS 헤더는 브라우저에게 보내는 허가증**이지, 서버의 실제 보안 차단이 아님
- **실제 보안은 서버 미들웨어**에서 담당 (API 키, 인증, 권한 등)
- **Postman 등 독립 클라이언트**는 CORS 정책의 영향을 받지 않음
- **개발환경에서는 관대하게, 프로덕션에서는 엄격하게** 설정하는 것이 일반적