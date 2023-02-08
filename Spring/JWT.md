# JWT란
- ESM Trading API 인증방식은 public/private key를 이용한 JWT(JSON Web Token) 인증 방식이다. HMAC 해싱 방식으로 생성된 Secret Key를 사용하여 header와 payload를 해싱한 signature를 생성하여 JWT를 만든다. 이 때 생성된 token은 Http헤더를 통해 API 인증 서버로 전송하여 처리된다.

# JWT 구조
- JWT(JSON Web Token)구조는 dot(.)으로 구분된 세 부분으로 구성된다. Header(xxxxx)/Payload(yyyy)/Signature(zzzzz)로 구성되어 있고 발급된 토큰을 보면 xxxxx.yyyyy.zzzzz구조를 확인할 수 있다.

# Header
- JWT의 첫번째 파트, 토큰의 타입과 사용중인 알고리즘 방식 두 부분으로 구성된다.

# Payload
- 토큰의 두 번째 파트, 클레임을 포함하는 영역이다. 클레임은 엔티티(일반적으로 사용자) 및 추가 데이터에 대한 설명이다. 클레임은 Registered, Public, Privae 세 가지 타입이 있다

# Signature
- Signature 생성 시 인코딩 된 Header, 인코딩 된 payload, secret key, 헤더에 지정된 알고리즘 방식이 필요하다.

# JWT 작동 방식
1. 애플리케이션 또는 클라이언트가 auth서버에 권한을 요청
2. 권한이 부여되면 auth서버는 애플리케이션에 acess토큰을 반환
3. 애플리케이션은 access토큰을 사용하여 protected resource에 접근