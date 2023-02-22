# 솔리디티에서 사용하는 데이터 위치(location)을 명시하지 않으면 컴파일 과정에서 에러를 발생시킨다. 레퍼런스 타입은 아래와 같다
1. Array(솔리디티에서는 bytes,string 타입을 special array로 취급한다)
2. Struct
3. Mapping
# 데이터 위치(location)
## Storage
- 모든 상태 변수를 저장한다. 즉, 블록체인에 저장되는 데이터는 모두 Storage에 저장된다
## Memory
- 함수 호출(External) 과정에 휘발성으로 존재하는 데이터를 잠시 저장하는 곳이다
- 수정이 가능하다
## Calldata
- 함수 호출 시 파라미터에 포함되는 데이터를 잠시 저장하는 곳이다
- 수정이 불가능하다

# calldata 와 memory의 동작 차이
- memory 키워드로 데이터를 가져올 경우의 순서를 살펴보면 이해하기 쉽다
1. calldata 형태로 데이터를 가지고 온다.
2. 새로운 memory에 데이터를 복사한다.
3. memory 형태의 데이터를 전달한다.

- 즉 calldata 키워드의 의미는 Data field에 포함된 데이터를 그대로 사용하겠따는 말이고, memory 키워드는 Data field를 통해 가져온 데이터에 대한 복사본을 만들어서 사용하겠다는 말이 된다

# 요약
1. 레퍼런스 타입 변수는 선언 시 데이터 위치(storage,memory,calldata)를 꼭 명시해야 한다
2. 상태 변수의 변경이 블록체인에 저장되어야 한다면 storage 키워드를 사용한다
3. 블록체인으로의 상태 변수 업데이트가 필요 없다면 memory,calldata를 사용한다. 단 변수 값의 수정이 이루어지지 않는 단순 읽기만 요구된다면, 가스비 절약을 위해서라도 calldata를 사용하는 것이 더 바람직하다


