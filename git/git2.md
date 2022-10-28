# Git undoing
## 세가지 분류
1. Working Directory
- Working Directory에서 수정한 파일 내용은 이전 커밋 상태로 되돌리기
- git restore
2. Staging Area 작업 단계
- Staging Area에 반영된 파일을 Working Directory로 되돌리기
- git rm --cached
- git restore --staged
3. Repository 작업 단계
- 커밋을 완료한 파일을 Staging Area로 되돌리기
- git commit --amend

## git restore
- 이미 버전 관리가 되고 있는 파일만 되돌리기 기능
- git restore를 통해 되돌리면, 해당 내용을 복원할 수 없으니 주의할 것!
- git restore {파일 이름}
- [참고]git 2.23.0 버전 이전에는 git checkout -- {파일 이름}

## Stagint Area
- Staging Area에 반영된 파일을 Working Directory로 되돌리기 (== Unstage)
1. root-commit이 없는 경우 : git rm --cached
2. root-commit이 있는 경우 : git restore --staged
- git rm --cached {파일이름}
- "the contents are restored from HEAD"
- root-commit이 있는 경우 사용(Git 저장소에 한 개 이상의 커밋이 있는 경우)
- git restore --staged {파일 이름}
- [참고]git 2.23.0 버전 이전에는 git reset HEAD {파일 이름}

### git commit --amend
- 커밋을 완료한 파일을 Staging Area로 되돌리기
- 상황 별로 두 가지 기능으로 나뉨
1. Staging Area에 새로 올라온 내용이 없다면, 직전 커밋의 메시지만 수정
2. Staging Area에 새로 올라온 내용이 있다면, 직전 커밋을 덮어쓰기
- amend(수정하다) 즉, 이전 커밋을 수정해서 새 커밋으로 남김 커밋 내용을 수정하거나 수정 사항을 새로 커밋에 추가하고 싶을 때 사용 수정 사항을 반영하기 위해 새로운 커밋을 생성하지 않아도 됨
## Git reset
- 시계를 마치 과거로 돌리는 듯한 행위로, 프로젝트를 특정 커밋(버전) 상태로 되돌림
- 특정 커밋으로 되돌아 갔을 때, 해당 커밋 이후로 쌓았던 커밋들은 전부 사라짐
- git reset [옵션] {커밋 ID}
1. 옵션은 soft mixed hard 중 하나를 작성
2. 커밋 ID는 되돌아가고 싶은 시점의 커밋 ID를 작성

## git reset의 세 가지 옵션
1. --soft
- 해당 커밋으로 되돌아가고
- 되돌아간 커밋 이후의 파일들은 Staging Area로 돌려 놓음
2. --mixed
- 해당 커밋으로 되돌아가고
- 되돌아간 커밋 이후의 파일들은 Working Directory로 돌려 놓음
- git reset 옵션의 기본 값
3. --hard
- 해당 커밋으로 되돌아가고
- 되돌아간 커밋 이후의 파일들은 모두 Working Directory에서 삭제 -> 따라서 사용 시 주의할 것!
- 기존의 Untracked 파일은 사라지지 않고 Untracked로 남아 있음 
## git reflog
- git reset의 hard 옵션은 Working Directory 내용까지 삭제하므로 위험할 수 있음
- git reflog 명령어를 이용하면 reset하기 전의 comit 상태로 되돌아 감
## git revert
- 과거를 없었던 일로 만드는 행위로, 이전 커밋을 취소한다는 새로운 커밋을 생성함
- git revert {커밋 ID}
- 커밋 ID는 취소하고 싶은 커밋 ID를 작성
## git branch
- 브랜치는 나뭇가지라는 뜻으로, 여러 갈래로 작업 공간을 나누어 독립적으로 작업할 수 있도록 도와주는 Git의 도구
## 장점
1. 브랜치는 독립 공간을 형성하기 때문에 원본(master)에 대해 안전함
2. 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적인 개발이 가능함
3. Git은 브랜치를 만드는 속도가 굉장히 빠르고, 적은 용량을 소모함
## 조회
1. git branch
2. git branch -r
## 생성
1. git branch {브랜치 이름}
2. git branch {브랜치 이름} {커밋 ID}
## 삭제
1. git branch -d {브랜치 이름}
2. git branch -D {브랜치 이름}
## git switch
- 현재 브랜치에서 다른 브랜치로 이동하는 명령어
- git switch {브랜치 이름}
- git switch -c {브랜치 이름}
- git switch -c {브랜치 이름} {커밋 ID}
- switch하기 전에, 해당 브랜치의 변경 사항을 반드시 커밋 해야함을 주의 할 것!
- 다른 브랜치에서 파일을 만들고 커밋 하지 않은 상태에서 switch를 하면 브랜치를 이동했음에도 불구하고 해당 파일이 그대로 남아 있게 됨
## git merge
- 분기된 브랜치들을 하나로 합치는 명령어
- master 브랜치가 상용이므로, 주로 master 브랜치에 병합
- git merge {합칠 브랜치 이름}
- 병합하기 전에 브랜치를 합치려고 하는 즉, 메인 브랜치로 switch 해야함
- 병합에는 세 종류가 존재
1. Fast-Forward
2. 3-way Merge
3. Merge Conflict

## Fast Forward
- 마치 빨리감기 처럼 앞으로 당기기
## 3-way Merge
- 각 브랜치의 커밋 두 개와 공통 조상 하나를 사용하여 병합하는 방법
## Merge Conflict
- 수정하고 다시 add commit 한다
## git-flow
- 2010년 Vincent Driessen이 제안한 git 브랜치 전략
## HEAD
- "This is a pointer to the local branch you're currently on"
- HEAD가 현재 브랜치의 최신 커밋을 가리킨다고 할 수 있음
- git log 혹은 cat.git/HEAD를 통해서 현재 HEAD가 어떤 브랜치를 가리키는지 알 수 있음
## 원복 원격 저장소를 그대로 내 원격 저장소에 복제 (이러한 행위를 Fork라고 함)
## 이후 Pull Request를 통해 원본 원격 저장소에 반영될 수 있도록 요청함




## 정리
- 결국 어떤 브랜치 전략을 사용할 것인지는 팀에서 정리하는 문제
- 브랜치를 자주 생성하는 것을 강력히 권장하며, main(master) 브랜치 하나로만 작업하는 형태는 지양해야 함
