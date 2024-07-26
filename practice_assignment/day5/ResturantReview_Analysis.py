import pandas as pd
from scipy import stats

# 데이터 로드
file_path = 'Restaurant reviews.csv'
data = pd.read_csv(file_path)

# 1. 데이터의 종류와 속성
categorical_columns = ['Restaurant', 'Reviewer', 'Review', 'Metadata', 'Time']
continuous_columns = ['Rating', 'Pictures']

# Rating 열을 숫자형으로 변환 (오류 방지를 위해)
data['Rating'] = pd.to_numeric(data['Rating'], errors='coerce')
data['Pictures'] = pd.to_numeric(data['Pictures'], errors='coerce')

# 연속형 데이터 기술 통계
continuous_stats = data[continuous_columns].describe()

# 범주형 데이터의 빈도수
categorical_value_counts = {column: data[column].value_counts() for column in categorical_columns}

# 2. 데이터 탐색 (EDA)
# 결측치 확인
missing_values = data.isnull().sum()

# 중복 확인
duplicates = data.duplicated().sum()

# 7514 열 삭제
data_cleaned = data.drop(columns=['7514'])

# 결측치가 있는 행 삭제
data_cleaned = data_cleaned.dropna()

# 중복된 행 삭제
data_cleaned = data_cleaned.drop_duplicates()

# 결측치와 중복 데이터 확인
missing_values_cleaned = data_cleaned.isnull().sum()
duplicates_cleaned = data_cleaned.duplicated().sum()

# 3. 기초통계
# 왜도와 첨도 계산
skewness = data_cleaned[continuous_columns].skew()
kurtosis = data_cleaned[continuous_columns].kurt()

# 4. 상관관계와 인과관계
# 상관관계 계산
correlation = data_cleaned[continuous_columns].corr()

# 5. 가설검정과 A/B 테스트
# 그룹 A와 그룹 B 데이터 나누기
group_a = data_cleaned[data_cleaned['Restaurant'] == 'Beyond Flavours']['Rating']
group_b = data_cleaned[data_cleaned['Restaurant'] == 'Dine O China']['Rating']

# t-test 수행
t_stat, p_value = stats.ttest_ind(group_a, group_b)

# 결과 출력
print("Continuous Data Statistics:\n", continuous_stats)
print("\nMissing values before cleaning:\n", missing_values)
print("Number of duplicate rows before cleaning:", duplicates)
print("\nMissing values after cleaning:\n", missing_values_cleaned)
print("Number of duplicate rows after cleaning:", duplicates_cleaned)
print("\nSkewness:\n", skewness)
print("Kurtosis:\n", kurtosis)
print("\nCorrelation between Rating and Pictures:\n", correlation)
print("\nT-statistic:", t_stat)
print("P-value:", p_value)

# 필요한 경우 범주형 데이터의 빈도수도 출력
for column, value_counts in categorical_value_counts.items():
    print(f"\nValue counts for {column}:\n{value_counts}\n")