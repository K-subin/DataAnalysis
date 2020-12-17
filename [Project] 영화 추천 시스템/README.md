### Task 1. 데이터 준비하기

Task 1-1. 파일을 다운로드 받고 ua.data 파일(학습데이터)과 ua.test 파일(검증데이터)의 내용을 불러와서 Tensor 데이터 생성하기

Task 1-2. u.item 파일로부터 영화 id와 title 불러오기


### Task 2. Latent Factor 모델을 이용하여 학습하기

Task 2-1. P, Q, bias_user, bias_item 등 파라미터 초기화하기

Task 2-2. regularization과 bias 적용하여 가설, 비용 설정하기

Task 2-3. torch.optim을 사용하여 학습하기

Task 2-4. 학습데이터와 검증데이터에 대해서 각각 RMSE값을 구하여 출력하기 (training RMSE, test RMSE)


### Task 3. 13번 User에게 추천하기 (knn search)

Task 3-1. 13번 user의 예상 별점이 가장 높은 영화 top 20개를 찾아서 id 및 영화이름 출력하기

Task 3-2. Latent Matrix P와 Q를 이용하여 13번 user와 cosine similarity가 가장 유사한 영화 top 20개를 찾아서 id 및 영화이름 출력하기


### Task 4. 영화 클러스터링하기 (k-means clustering)

Task 4-1. 다음을 만족하는 k-means clustering알고리즘 구현하기

각 영화가 속한 cluster를 정할 때, cosine similarity를 기준으로 정하기

Task 4-2. k=1, ..., 40 까지 바꿔가면서 cost 값을 계산하고 이를 matplotlib을 활용하여 그래프로 그리기

Task 4-3. 가장 적절해보이는 k 선택하기


### Task 5. 차원 축소 및 시각화 (PCA)

Task 5-1. P 행렬와 Q 행렬을 합쳐 Z행렬 만들기

Task 5-2. Z 행렬에서 PCA 수행하여 2차원 데이터로 줄인 Zp 만들기 (외부 library 사용)

Task 5-3. matplotlib을 활용하여 Zp의 scatter plot 그리기

Task 5-3-1. P행렬과 Q행렬의 점들을 서로 다른 색으로 그리기

Task 5-3-2. Task 3의 결과 점들을 다른 색으로 그려 강조하기

Task 5-3-3. Task 4에서 구한 cluster들을 각기 다른 색으로 그리기
