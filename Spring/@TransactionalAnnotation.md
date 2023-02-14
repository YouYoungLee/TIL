# 트랜잭션
- 데이터베이스의 상태를 변경하는 작업 또는 한번에 수행되어야 하는 연산들을 의미한다.
- begin,commit 을 자동으로 수행해준다
- 예외 발생 시 rollback 처리를 자동으로 수행해준다
- 트랜잭션은 4가지의 성질을 가지고 있다.
1. 원자성(Atomicity)
- 한 트랜잭션 내에서 실행한 작업들은 하나의 단위로 처리한다. 즉, 모두 성공 또는 모두 실패
2. 일관성(Consistency)
- 트랜잭션은 일관성 있는 데이터베이스 상태를 유지한다. (data integrity 만족 등)
3. 격리성(Isolation)
- 동시에 실행되는 트랜잭션들이 서로 영향을 미치지 않도록 격리해야한다.
4. 영속성(Durability)
- 트랜잭션을 성공적으로 마치면 결과가 항상 저장되어야 한다.

# 처리 방법
- 스프링에서는 간단하게 어노테이션 방식으로 @Transactional을 메소드, 클래스, 인터페이스 위에 추가하여 사용하는 방식이 일반적이다. 이 방식을 선언적 트랜잭션이라 부르며, 적용된 범위에서는 트랜잭션 기능이 포함된 프록시 객체가 생성되어 자동으로 commit 혹은 rollback을 진행해준다.

# 옵션

1. isolation

- 트랜잭션에서 일관성없는 데이터 허용 수준을 설정한다

2. propagation

- 트랜잭션 동작 도중 다른 트랜잭션을 호출할 때, 어떻게 할 것인지 지정하는 옵션이다

3. noRollbackFor

- 특정 예외 발생 시 rollback하지 않는다.

4. rollbackFor

- 특정 예외 발생 시 rollback한다.

5. timeout

- 지정한 시간 내에 메소드 수행이 완료되지 않으면 rollback 한다. (-1일 경우 timeout을 사용하지 않는다)

6. readOnly

- 트랜잭션을 읽기 전용으로 설정한다.

# 그래서 왜 rollbackFor = Exception.class ?
- @Transactional 은 기본적으로 Unchecked Exception, Error 만을 rollback하고 있다.
그렇기 때문에 모든 예외에 대해서 rollback을 진행하고 싶을 경우
(rollbackFor = Exception.class) 를 붙여야 한다는 것을 깨달았다.
그 이유는 Checked Exception 같은 경우는 예상된 에러이며
Unchecked Exception, Error 같은 경우는 예상치 못한 에러이기 때문이란 것을 알게 되었다.

### JPA를 사용하면 트랜잭션 범위 안에서 Dirty Checking이 동작한다. 따라서 save()메서드를 호출하지 않아도 값이 알아서 수정되고 반영된다. save()는 엔티티를 추가할 때, update 했을 때는 따로 안써줘도 된다.

# Dirty Checking
- Dirty란 상태의 변화가 생긴 정도로 이해 즉 Dirty Checking이란 상태 변경 검사 입니다.
- JPA에서는 트랜잭션이 끝나는 시점에 변화가 있는 모든 엔티티 객체를 데이터베이스에 자동으로 반영해줍니다. 이 때 변화가 있다는 기준은 최초 조회 상태입니다. 
- JPA에서는 엔티티를 조회하면 해당 엔티티의 조회 상태 그대로 스냅샷을 만들어 놓습니다. 그리고 트랜잭션이 끝나는 시점에는 이 스냅샷과 비교해서 다른점이 있다면 Update Query를 데이터베이스로 전달합니다.
- 당연히 이런 상태 변경 검사의 대상은 영속성 컨텍스트가 관리하는 엔티티에만 적용 됩니다.
1. detach된 엔티티(준영속)
2. DB에 반영되기 전 처음 생성된 엔티티(비영속)
- 등 준영속/비영속 상태의 엔티티는 Dirty Checking 대상에 포함되지 않습니다. 즉, 값을 변경해도 데이터베이스에 반영되지 않는다.
- @DynamicUpdate로 변경 필드만 반영되도록 할 수 있다.
