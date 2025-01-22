import pymysql  # MariaDB 연결을 위한 라이브러리
from datetime import datetime  # 현재 연도와 월 계산
from app.config import DB_CONFIG  # MariaDB 설정 정보

def save_to_db(product_list, store_name):
    """MariaDB에 크롤링 데이터를 저장"""
    try:
        conn = pymysql.connect(**DB_CONFIG)
        with conn.cursor() as cursor:
            # 데이터 삽입 쿼리
            sql = """
            INSERT INTO convenience_store_products 
            (store_name, year, month, product_name, price, image, event_info, tag)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            # 현재 연도와 월 가져오기
            current_year = datetime.now().year
            current_month = datetime.now().month

            # 데이터 삽입
            for product in product_list:
                cursor.execute(sql, (
                    store_name,                         # 편의점 이름
                    current_year,                       # 연도
                    current_month,                      # 월
                    product.get("name"),                # 상품 이름
                    product.get("price"),               # 상품 가격
                    product.get("image"),               # 이미지 URL
                    product.get("event"),               # 이벤트 정보 (1+1 등)
                    product.get("tag"),                 # 기타 태그 (new, best 등)
                ))
            conn.commit()
            print(f"총 {len(product_list)}개의 데이터를 DB에 저장했습니다.")
    except Exception as e:
        print("DB 저장 중 오류 발생:", e)
    finally:
        conn.close()