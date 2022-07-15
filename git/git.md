# GIT

 git=분산버전관리 프로그램
 Git≠github

CLI=커멘더라인 명령어로 작업하는거
명령어를 통해 사용자와 컴퓨터가 상호작용하는 방식

GUI=문서 폴더만들기등 보통하는거
그래픽을 통해 사용자와 컴퓨터가 상호작용하는 방식

CLI를 쓰는 이유 컴퓨터의 리소스를 줄요줌(경제적)

# CLI 명령어

touch
파일을 생성하는 명령어

Mkdir 
새 폴더를 생성하는 명령어

ls
현재 작업 중인 디렉토리의 폴더/파일 목록을 보여주는 명령어

cd
현재 작업 중인 디렉토리를 변경하는 명령어

start,open
폴더/파일을 여는 명령어 window 에서는 start mac에서는 open

rm
파일을 삭제하는 명령어 -r 옵션을 주면 폴더 삭제 가능

절대 경로
루트 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것
윈도우 바탕화면의 절대 경로 -C:/Users/ssafy/Desktop

상대 경로
현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것
 현재 작업하고 있는 디렉토리가 C://Users일 때
윈도우 바탕 화면으로의 상대 경로는 ssafy/Desktop
./: 현재 작업하고 있는 폴더   ../:현재 작업하고 있는 폴더의 부모 폴더

[https://www.markdownguide.org/cheat-sheet/](https://www.markdownguide.org/cheat-sheet/)

# git 명령어

git init 명령어로 로컬 저장소를 생성
.git 디렉토리에 버전 관리에 필요한 모든 것이 들어있음

특정 버전은 커밋으로 남긴다
특정 버전으로 남긴다 → “커밋(commit)한다”

커밋의 3가지 영역
- working Directory : 내가 작업하고 있는 실제 디렉토리
- staging Area : 커밋(commit)으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳
- Repository : 커밋(commit)들이 저장되는 곳

working   에서 staging으로 갈때는 git add 명령어
staging  에서 repository으로 갈때는 git commit 명령어

git status 
현재 git으로 관리되고 있는 파일들의 상태를 알 수 있어요

git diff A B
A랑 B를 비교

## git 올릴 때
1. git add .
2. git commit -m”(이름)”
3. git remote add origin {remote_repo}
4. git push -u origin master
5. git push

바로 vs코드 열기 code .

git clone 주소복사 하면 바로 열 수 있음.
