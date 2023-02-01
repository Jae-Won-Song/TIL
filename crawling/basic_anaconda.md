# Anaconda

- 머신러닝이나 데이터 분석 등에 사용하는 여러가지 패키지가 기본적으로 포함되어있는 파이썬 배포판

- 파이썬 가상 환경을 구축하는데도 유용하게 사용가능
---

## Anaconda 명령어

- ```conda env list``` : 가상환경 목록 보기
- ```conda create -n <가상환경이름> python=<버전>``` :  가상환경 생성
    - ex) conda create -n TestEnv python=3.7
- ```conda env remove -n <가상환경이름>``` : 가상환경 삭제
- ```conda activate <가상환경이름>``` : 가상환경 실행
- ```conda deactivate``` : 가상환경 종료
- ```conda list``` : 현재 가상환경에서 설치되어있는 패키지 보기
- ```conda install <패키지 이름>``` : 현재 가상환경에서 패키지 설치
    - ex1) conda install numpy
    - ex2) conda install numpy pandas
    - ex3) conda install tensorflow-gpu==1.13.1
- ```conda uninstall <패키지 이름>``` : 현재 가상환경에서 패키지 삭제
- ```conda create --name <복사하여 생성할 가상환경명> --clone <복사할 가상환경명>``` :
    - ex) conda create --name NewProject --clone OldProject : OldProject를 복사하여 NewProject로 생성함
- ```conda env create --file <yml파일명.yml or yaml>```: yml/yaml로 가상환경 생성
    - ex) conda env create --file environment.yml
- ```conda env update --file <yml파일명.yml or yaml> --prune``` : yml 덮어쓰기 (activate상태에서 사용가능)
    - ex) conda env update --file environment.yml --prune
- ```conda env create -f <yml파일명.yaml or yaml> , conda env export > <yml파일명.yml>``` : 현재 가상환경의 yml 생성
    - ex) conda env create -f environment.yml
    - ex) conda env export > environment.yaml
- ```python --version``` : 파이썬 버전 확인
- ```nvidia-smi``` : 드라이버 정보 표시 (+ CUDA 버전 표시)