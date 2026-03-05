'''
구조화 데이터 파일
- CSV : 표(스프레드 시트) 형태 데이터
- JSON : API/설정 파일/로그 등에서 자주 쓰는 데이터 교환 포맷
'''

from paths import DATA_DIR
import csv

def demo_csv_write_read_sum():
    '''
    csv 파일 기본 흐름
    1) writer로 CSV 생성
    2) DictReader로 읽기
    3) amount 합계 계산
    '''
    
    ledger_csv = DATA_DIR / "ledger_sample.csv"
    rows = [
        ("2025-01-03", "식비", "김밥", "card", 3500, "점심"),
        ("2025-01-04", "교통", "버스", "card", 1500, "출근"),
        ("2025-01-05", "통신", "휴대폰", "acct", 30000, "12월")
    ]
    
    with open(ledger_csv, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "category", "item", "method", "amount", "note"])
        writer.writerows(rows)
        