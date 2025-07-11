# 🌐 PHP 엔진 학습을 위한 네트워킹 학습 가이드

## 📚 학습 목표
PHP 엔진이 네트워크 요청을 어떻게 처리하는지 이해하고, 웹서버와 PHP 간의 통신 과정을 깊이 있게 파악하기

---

## 🎯 1단계: 기초 네트워킹 개념 (완료 ✅)

### 완료된 학습 내용
- [x] TCP/IP 4계층 모델 이해
- [x] 포트의 개념과 역할  
- [x] 커널 vs 사용자 공간의 역할 구분
- [x] TCP 3-way handshake 과정
- [x] Sequence/Acknowledgment 번호 동작 원리
- [x] 커널과 웹서버 간 데이터 전달 구조

### 관련 학습 자료
- `network.md` - TCP/IP 계층 구조와 역할
- `tcp_handshake_seq_ack.md` - TCP 연결 과정 상세
- `kernel_webserver_socket_flow.md` - 데이터 전달 흐름
- `port.md` - 포트 개념과 관리

---

## 🔧 2단계: 소켓 프로그래밍 기초

### 학습 목표
- 소켓 API 동작 원리 이해
- 블로킹/논블로킹 I/O 개념 습득
- 소켓 버퍼 관리 메커니즘 파악

### 세부 학습 항목
- [ ] **소켓 생성과 바인딩 과정**
  - `socket()` - 소켓 생성
  - `bind()` - 포트 바인딩
  - `listen()` - 연결 대기
  - `accept()` - 클라이언트 연결 수락

- [ ] **데이터 송수신**
  - `send()` / `recv()` 함수 동작 원리
  - 소켓 버퍼와 TCP 윈도우 크기
  - 부분 전송/수신 처리 방법

- [ ] **I/O 모델**
  - 블로킹 I/O vs 논블로킹 I/O
  - `O_NONBLOCK` 플래그 사용법
  - EAGAIN/EWOULDBLOCK 에러 처리

### 실습 과제
```c
// 간단한 TCP 서버 구현
// 1. 소켓 생성 및 바인딩
// 2. 클라이언트 연결 수락
// 3. HTTP 요청 수신 및 응답 전송
```

---

## 🌐 3단계: HTTP 프로토콜 심화

### 학습 목표
- HTTP 요청/응답 구조 완전 이해
- 헤더 파싱 과정 습득
- 연결 관리 메커니즘 파악

### 세부 학습 항목
- [ ] **HTTP 메시지 구조**
  ```http
  GET /index.php HTTP/1.1
  Host: localhost
  User-Agent: Mozilla/5.0
  
  [메시지 본문]
  ```

- [ ] **요청/응답 파싱**
  - 첫 번째 줄 (Request Line / Status Line) 분석
  - 헤더 필드 파싱 알고리즘
  - 본문 길이 결정 (Content-Length vs Transfer-Encoding)

- [ ] **연결 관리**
  - HTTP/1.0 vs HTTP/1.1 차이점
  - Keep-Alive와 Connection 헤더
  - 파이프라이닝과 HOL 블로킹

- [ ] **HTTP/2 기초**
  - 바이너리 프로토콜 개념
  - 스트림과 멀티플렉싱
  - 헤더 압축 (HPACK)

### 실습 과제
```php
// HTTP 요청 파서 구현
// 1. 요청 라인 분석
// 2. 헤더 파싱
// 3. 본문 추출
```

---

## 🚀 4단계: 웹서버 동작 원리

### 학습 목표
- 웹서버 아키텍처 패턴 이해
- Apache vs Nginx 비교 분석
- FastCGI/PHP-FPM 통신 구조 파악

### 세부 학습 항목
- [ ] **웹서버 아키텍처**
  - 프로세스 모델 (Apache prefork)
  - 스레드 모델 (Apache worker)
  - 이벤트 루프 (Nginx, Node.js)

- [ ] **Apache vs Nginx**
  - 동시 연결 처리 방식
  - 메모리 사용량 비교
  - 모듈 시스템 차이점

- [ ] **FastCGI/PHP-FPM**
  - CGI → FastCGI 발전 과정
  - PHP-FPM 프로세스 풀 관리
  - 유닉스 소켓 vs TCP 소켓 통신

- [ ] **로드 밸런싱**
  - 리버스 프록시 개념
  - 라운드 로빈, 최소 연결 알고리즘
  - 헬스 체크와 장애 처리

### 실습 과제
```bash
# Apache + PHP-FPM 설정
# 1. 가상 호스트 설정
# 2. FastCGI 모듈 구성
# 3. 성능 모니터링
```

---

## 🔗 5단계: PHP 엔진과 네트워크 연동

### 학습 목표
- PHP 내부 네트워크 처리 메커니즘 이해
- SAPI와 웹서버 연동 구조 파악
- PHP 네트워크 함수들의 동작 원리 습득

### 세부 학습 항목
- [ ] **PHP SAPI (Server API)**
  - Apache 모듈 vs FastCGI SAPI
  - 요청/응답 처리 라이프사이클
  - 메모리 관리와 가비지 컬렉션

- [ ] **PHP 네트워크 함수**
  - `fopen()` / `file_get_contents()` 내부 구현
  - `curl` 확장 모듈 동작 원리
  - `stream_context` 사용법

- [ ] **PHP-FPM 세부 구조**
  - 마스터/워커 프로세스 관리
  - 요청 큐잉과 백프레셔
  - 프로세스 풀 튜닝

- [ ] **세션 저장소**
  - 파일 기반 vs 메모리 기반 세션
  - Redis/Memcached 연동
  - 세션 클러스터링

### 실습 과제
```php
// PHP 네트워크 프로그래밍
// 1. 소켓 클라이언트 구현
// 2. HTTP 클라이언트 라이브러리 작성
// 3. 비동기 I/O 처리
```

---

## ⚡ 6단계: 성능 최적화 및 고급 주제

### 학습 목표
- 네트워크 성능 병목점 식별
- 최적화 기법 적용
- 확장성 있는 아키텍처 설계

### 세부 학습 항목
- [ ] **성능 분석**
  - 네트워크 지연 시간 측정
  - 처리량(Throughput) vs 응답 시간
  - CPU vs I/O 바운드 식별

- [ ] **최적화 기법**
  - 커넥션 풀링과 재사용
  - HTTP/2 푸시와 멀티플렉싱
  - 압축 (gzip, brotli) 활용

- [ ] **캐싱 전략**
  - 브라우저 캐시 제어
  - CDN과 에지 캐싱
  - 애플리케이션 레벨 캐싱

- [ ] **PHP 성능 최적화**
  - OPcache 튜닝
  - 메모리 사용량 최적화
  - 데이터베이스 연결 풀링

### 실습 과제
```bash
# 성능 테스트 및 튜닝
# 1. Apache Bench (ab) 부하 테스트
# 2. PHP-FPM 설정 최적화
# 3. 모니터링 대시보드 구축
```

---

## 🔍 7단계: 실전 디버깅 및 모니터링

### 학습 목표
- 네트워크 문제 진단 능력 배양
- 프로덕션 환경 모니터링 구축
- 장애 대응 프로세스 수립

### 세부 학습 항목
- [ ] **패킷 분석**
  - Wireshark 고급 필터링
  - TCP 플로우 분석
  - SSL/TLS 디버깅

- [ ] **시스템 모니터링**
  - `netstat`, `ss`, `lsof` 명령어
  - 소켓 상태 모니터링
  - 네트워크 인터페이스 통계

- [ ] **PHP 디버깅**
  - 네트워크 오류 로깅
  - 스택 트레이스 분석
  - 메모리 누수 탐지

- [ ] **성능 프로파일링**
  - Xdebug 프로파일링
  - New Relic, DataDog 연동
  - 알림 시스템 구축

### 실습 과제
```bash
# 모니터링 환경 구축
# 1. Prometheus + Grafana 설정
# 2. 로그 수집 및 분석
# 3. 장애 알림 시스템 구축
```

---

## 📈 학습 진행 체크리스트

### 1단계 (완료 ✅)
- [x] TCP/IP 4계층 모델
- [x] 포트와 소켓 개념
- [x] TCP 핸드셰이크
- [x] 커널-웹서버 데이터 흐름

### 2단계 (진행 중)
- [ ] 소켓 API 학습
- [ ] I/O 모델 이해
- [ ] 간단한 TCP 서버 구현

### 3단계 (대기 중)
- [ ] HTTP 프로토콜 심화
- [ ] 헤더 파싱 구현
- [ ] HTTP/2 기초 학습

### 4단계 이후
- [ ] 웹서버 아키텍처 분석
- [ ] PHP-FPM 연동 구조
- [ ] 성능 최적화 기법
- [ ] 모니터링 시스템 구축

---

## 🎓 학습 팁

### 효과적인 학습 방법
1. **이론 → 실습 → 디버깅** 순서로 진행
2. **실제 코드 작성**을 통한 체험적 학습
3. **Wireshark 패킷 캡처**로 실제 동작 확인
4. **PHP 소스코드 일부 분석**으로 내부 구현 이해

### 추천 실습 도구
- **Wireshark** - 패킷 분석
- **tcpdump** - 명령줄 패킷 캡처
- **Apache Bench (ab)** - 부하 테스트
- **strace** - 시스템 콜 추적

### 참고 자료
- 현재 프로젝트 학습 파일들
- PHP 공식 문서 (php.net)
- Apache/Nginx 공식 문서
- RFC 문서 (HTTP, TCP 관련)

---

## 🔥 다음 단계 추천

현재 1단계를 잘 완료하셨으니, **2단계의 소켓 프로그래밍 기초**부터 시작하시길 추천합니다. 

특히 다음 순서로 진행하시면 좋겠습니다:
1. **간단한 TCP 서버 C 코드 작성**
2. **소켓 버퍼 동작 실험**
3. **블로킹/논블로킹 I/O 테스트**

이 과정을 통해 PHP 엔진이 내부적으로 어떻게 네트워크 요청을 처리하는지 깊이 이해할 수 있을 것입니다!
