# 생성자의 단점
- 생성자에는 제약이 하나 있는데, 선택적 매개변수가 많을 경우에 대응이 어렵다. 
- 코드를 읽을 때 각 값의 의미가 무엇인지 헷갈린다 
- 매개변수가 몇개인지 세어보며 항상 확인해야한다. 
- 타입이 같은 매개변수가 연속으로 있으면 버그 발생 가능성이 높아진다
- 실수로 매개변수의 순서가 바뀌더라도 컴파일러가 해당 에러를 잡지 못하여 런타임 에러로 이어지게된다.

# Builder패턴이란?
- 빌더 패턴(Builder pattern)이란 복합 객체의 생성 과정과 표현 방법을 분리하여 동일한 생성 정찰에서 서로 다른 표현 결과를 만들 수 있게 하는 패턴입니다.
# 빌더 패터 장점
1. 어떤 필드에 어떤 값을 채워야 할지 명확히 지정할 수 있음
2. 필수 및 선택인자가 많아질수록 생성자 방식보다 가독성이 좋다
3. 자바빈 패턴(setter를 이용하는 방식)보다 안전함
4. setter 생성을 방지하기 때문에 객체를 변경할 수 없음(불변성 보장)