# 개념
- Docker는 컨테이너 기반의 오픈소스 가상화 플랫폼입니다. 다양한 프로그램, 실행환경을 컨테이너로 추상화하고 동일한 인터페이스를 제공하여 프로그램의 배포 및 관리를 단순하게 해줍니다. 백엔드 프로그램, 데이터베이스 서버, 메시지 큐등 어떤 프로그램도 컨테이너로 추상화할 수 있고 조립 PC, AWS, Azure,Google cloud등 어디에서든 실행할 수 있습니다.

# 가상화를 사용하는 이유
- 서버 관리자 입장에서 CPU사용률이 10%대 밖에 되지 않는 활용도가 낮은 서버들의 리소스 낭비일 수 밖에 없습니다. 그렇다고 모든 서비스를 한 서버안에 올린다면 안정성에 문제가 생길수도 있습니다. 그래서 안정성을 높이며 리소스도 최대한 활용할 수 있는 방법으로 나타난게 서버 가상화입니다. 

# 컨테이너란?
- 컨테이너 가상화 기술 중 하나로 대표적으로 LXC(Linux Container)가 있습니다. 기존 OS를 가상화 시키던 것과 달리 컨테이너는 OS레벨의 가상화로 프로세스를 격리시켜 동작하는 방식으로 이루어집니다. 개별 Software의 실행에 필요한 실행환경을 독립적으로 운용할 수 있도록 기반환경 또는 다른 실행환경과의 간섭을 막고 실행의 독립성을 확보해주는 운영체계 수준의 격리 기술을 말합니다.

# 이미지(Image)
- 이미지는 컨테이너 실행에 필요한 파일과 설정값등을 포함하고 있는 것으로 상태값을 가지지 않고 변하지 않습니다.