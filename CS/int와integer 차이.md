# int는 변수의 타입(data type)이다.
- 변수(variable)는 '값을 저장할 수 있는 메모리 상의 공간'을 의미 합니다.
- 자료형은 data의 type에 따라 값이 저장될 공간의 크기와 저장 형식을 정의한 것 이라고 볼 수 있습니다.
# Integer는 무엇인가
1. 매개변수로 객체를 필요로 할 때
2. 기본형 값이 아닌 객체로 저장해야할 때
3. 객체 간 비교가 필요할 때
- 기본형을 객체로 다루기 위해 사용하는 클래스들을 래퍼 클래스(wrapper class)라고 합니다
- 그리고 Integer는 init의 레퍼클래스 라고 할 수 있습니다.

# 정리
1. int:자료형(primitive type)
- 산술 연산 가능함
- null로 초기화 불가
2. Integer : 래퍼 클래스(Wrapper class)
- Unboxing하지 않을 시 산술 연산 불가능함
- null 값 처리 가능!