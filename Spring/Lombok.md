# Why Lombok?
- Lombok 라이브러리를 사용하면, Getter,Setter 메서드로 코드를 어지럽게 작성할 필요도, 생성자를 작성할 필요도 없다. 딱 필드만 남게되므로 오히려 코드의 가독성이 높아진다.
# Lombok Annotations
1. @ToString
- 자동으로 ToString()를 사용할 수 있는 어노테이션이다
- ToString이란 객체가 가지고 있는 정보나 값들을 문자열로 만들어 리턴하는 메소드
- Object클래스에 있는 toString()메소드를 오버라이딩하여 사용(재정의)
2. @Getter and @Setter
- 자동으로 getter(),setter()를 사용할 수 있는 어노테이션이다.
3. @NoArgsConstructor
- 인자값이 없는 기본 생성자를 사용할 수 있는 어노테이션이다
- 무조건 완전한 상태의 객체를 생성할 수 있도록 도움을 준다는 의미
4. @AllArgsConstructor
- VO 객체에 있는 모든 필드를 인자로 받는 생성자를 사용할 수 있는 어노테이션이다
5. Data
- @ToString, @EqualsAndHashCode, @Getter, @Setter, @RequiredArgsConstructor 를 모두 자동으로 사용할 수 있는 어노테이션이다.

# 무분별한 Setter 남용
- Setter는 그 의도가 분명하지 않고 객체를 언제든지 변경할 수 있는 상태가 되어서 객체의 안정성이 보장받기 힘들다.

# @RequiredArgsConstructor 지양
- 의존 관계를 주입하기 위해 사용하는 어노테이션
- 의존 주입 방식은 총 3가지가 있다.
1. 생성자 주입 방식
2. 필드 주입 방식
3. Setter 주입 방식
- 공식 레퍼런스에서는 생성자 주입 방식 권장
- 왜냐하면 필수적인 의존성을 모두 만족해야만 객체를 생성할 수 있도록 강제할 수 있기 때문이다.