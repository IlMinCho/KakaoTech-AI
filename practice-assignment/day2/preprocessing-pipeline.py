# 07/03/2024 by ilmin cho
# KakaoTech AI, Day3

import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# 데이터 로드 함수
def load_data(file_path):
    return pd.read_csv(file_path)

# 결측값 처리 함수
def preprocess_data(df):
    # 'Date of Birth' 열로부터 'Age' 계산
    df['Date of Birth'] = pd.to_datetime(df['Date of Birth'], format='%Y-%m-%d', errors='coerce')
    df['Age'] = (pd.to_datetime('today') - df['Date of Birth']).dt.days // 365
    
    # 'Time' 열을 초 단위로 변환
    df['Time'] = pd.to_timedelta(df['Time']).dt.total_seconds()
    
    # 결측값 처리
    imputer = SimpleImputer(strategy='mean')
    df[['Age', 'Time']] = imputer.fit_transform(df[['Age', 'Time']])
    df['Country'].fillna('Unknown', inplace=True)
    
    return df

# 평균 나이 계산 함수
def calculate_average_age(df):
    return df['Age'].mean()

# 나라별 평균 속도 계산 함수
def calculate_average_speed_by_country(df):
    return df.groupby('Country')['Time'].mean().reset_index()

# 전체 파이프라인 구축
def data_pipeline(file_path):
    # 1. 데이터 로드
    data = load_data(file_path)
    
    # 2. 데이터 전처리
    data = preprocess_data(data)
    
    # 3. 평균 나이 계산
    average_age = calculate_average_age(data)
    
    # 4. 나라별 평균 속도 계산
    average_speed_by_country = calculate_average_speed_by_country(data)
    
    return average_age, average_speed_by_country

# 데이터 파일 경로
file_path = 'data.csv'

# 파이프라인 실행
average_age, average_speed_by_country = data_pipeline(file_path)

# 결과 출력
print(f"Average age of marathon runners: {average_age:.2f}")
print("\nAverage speed by country (in seconds):\n", average_speed_by_country)