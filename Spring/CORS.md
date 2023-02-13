# CORS
- 브라우저에서 보안적인 이유로 cross-origin HTTP 요청들을 제한합니다. 그래서 cross-origin 요청을 하려면 서버의 동의가 필요합니다. 만약 서버가 동의한다면 브라우저에서는 요청을 허락하고, 동의하지 않는다면 브라우저에서 거절합니다. 이러한 허락을 구하고 거절하는 메커니즘을 HTTP-header를 이용해서 가능한데, 이를 CORS(Cross-Origin Resource Sharing)라고 부릅니다. 그래서 브라우저에서 cross-origin 요청을 안전하게 할 수 있도록 하는 메커니즘입니다.

## cross-origin 이란 다음 중 한 가지라도 다른 경우를 말합니다.
1. 프로토콜 - http와 https는 프로토콜이 다르다
2. 도메인 - domain.com과 other-domain.com은 다르다
3. 포트 번호 = 8080 포트와 3000포트는 다르다

# Simple requests인 경우
1. 서버로 요청
2. 서버의 응답이 왔을 때 브라우저가 요청한 Origin과 응답한 헤더 Access-Control-Request-Headers의 값을 비교하여 유효한 요청이라면 리소스를 응답한다.

## 서버에서 Access-Control-Allow-Origin 헤더에 허용할 출처를 기재해서 클라이언트에 응답하면 되는 것이었다. 

## Origin : Protocol + Host + Port

# SOP(Same - Origin Policy) - 동일 출처 정책
- 동일한 출처에 대한 정책 
- 동일한 출처에서만 리소스를 공유할 수 있다

## 출처를 비교하는 로직은 서버에 구현된 스펙이 아닌 브라우저에 구현된 스펙이다

# TIP
- 클라이언트 단 코드에서 API 요청을 하는게 아니라, 서버 단 코드에서 다른 출처의 서버로 API 요청을 하면 CORS 에러로부터 자유로워 진다. 그래서 이를 이용한 프록시(Proxy)서버라는 것이 있따.

1. 예비 요청
- 예비 요청을 보내 서버와 잘 통신 되는지 확인한 후 본 요청을 보낸다
- 예비 요청의 역할은 본 요청을 보내기 전에 브라우저 스스로 안전한 요청인지 미리 확인하는 것이다.
- 예비요청을 보내는 것을 Preflight라고 부르며, 이 예비요청의 HTTP 메소드를 GET이나 POST가 아닌 OPTIONS라는 요청이 사용된다는 것이 특징이다.

2. 단순 요청(Simple Request)
- 예비 요청(Prefilght)을 생략하고 바로 서버에 직행으로 본 요청을 보낸 후 서버가 이에 대한 응답의 헤더에 Access-Control-Allow-Origin 헤더를 보내주면 브라우저가 CORS정책 위반 여부를 검사하는 방식이다 다만 심플한 만큼 특정 조건을 만족하는 경우에만 예비 요청을 생략할 수 있다.
- 요청의 메소드는 GET,HEAD,POST중 하나여야 한다.
- Accept, Accept-Language, Content-Language, Content-Type, DPR, Downlink, Save-Data, Viewport-Width, Width 헤더일 경우 에만 적용된다.
- Content-Type 헤더가 application/x-www-form-urlencoded, multipart/form-data, text/plain중 하나여야한다. 아닐 경우 예비 요청으로 동작된다.
## 단순 요청이 일어나는 상황은 드물다 왜냐하면 대부분 HTTP API 요청은 text/xml 이나 application/json 으로 통신하기 때문에 3번째 Content-Type이 위반되기 때문이다. 따라서 대부분의 API 요청은 그냥 예비 요청(preflight)으로 이루어진다 라고 이해하면 된다

3. 인증된 요청 (Credentialed Request)
- 인증된 요청은 클라이언트에서 서버에게 자격 인증 정보(Credential)를 실어 요청할 때 사용되는 요청이다
- 여기서 말하는 자격 인증 정보란 세션 ID가 저장되어 있는 쿠키(Cookie) 혹은 Authorization헤더에 설정하는 토큰 값 등을 일컫는다.

# CORS를 해결하는 방법 총정리
1. Chrome 확장 프로그램 이용
- 'Allow CORS:Access-Control-Allow-Origin' 크롬 확장 프로그램을을 설치 해준다. 로컬 환경에서 API를 테스트시, CORS 문제를 해결할 수 있다.
2. 프록시 사이트 이용하기
- 프록시란 클라이언트와 서버 사이의 중계 대리점이라고 보면 된다.
- 모든 출처를 허용한 서버 대리점을 통해 요청을 하면 된다. 다만 api 요청 횟수 제한을 두어 실전에서는 사용하기 무리이다.
3. 서버에서 Access-Control-Allow-Origin 헤더 세팅하기
- 직접 서버에서 HTTP 헤더 설정을 통해 출처를 허용하게 설정하는 가장 정석적인 해결책이다.
- 각 서버의 문법에 맞게 위의 HTTP 헤더를 추가해 주면 된다