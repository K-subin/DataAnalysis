# 주어진 문서(위키피디아 문장 데이터셋)에서 가장 많이 등장하는 단어 1000개가 각각 몇 번 등장했는지 조사하고, 지프의 법칙을 따르는지 알아보기

### Task 0. 데이터 준비
위키피디아 문장 데이터셋 : https://www.kaggle.com/mikeortman/wikipedia-sentences

### Task 1. 문서를 입력받아 자주 등장하는 단어 1000개를 자주 등장하는 순서대로 출력하는 python 프로그램 작성하기
Task 1.1. 각 단어에는 영어 알파벳과 숫자만 존재한다고 가정

Task 1.2. 모든 알파벳은 소문자로 변경

Task 1.3. 예) 길동 is one of Tom’s best friends. → [‘is’, ‘one’, ‘of’, ‘tom’, ‘s’, ‘best’, ‘friends’]

### Task2. matplotlib을 활용하여 각 단어의 출현 횟수 순위(x축)와 각 단어의 출현 횟수(y축)를 log scale에서 출력하고, 지프의 법칙을 따르는지 확인하기

Task2.1. 지프의 법칙 : n = ck^-s (k : 단어의 출현 횟수 순위, n : 단어의 출현 횟수, c,s : 상수)

Task2.2. 주어진 데이터에 대해서 상수 c와 s의 값을 대략적으로 구해보기

Task2.3. plt.savefig()를 통해 파일로 결과 그래프 출력

Task2.4. 대략적으로 계산한 상수 c와 s를 stdout으로 출력
