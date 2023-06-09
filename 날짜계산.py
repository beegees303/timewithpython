from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_date_difference(date1, date2):
    format = "%Y-%m-%d"  # 날짜 형식 지정 (예: "YYYY-MM-DD")
    parsed_date1 = datetime.strptime(date1, format)
    parsed_date2 = datetime.strptime(date2, format)
    difference = parsed_date2 - parsed_date1
    return difference.days
def calculate_month_difference(date1, date2):
    format = "%Y-%m-%d"  # 날짜 형식 지정 (예: "YYYY-MM-DD")
    parsed_date1 = datetime.strptime(date1, format)
    parsed_date2 = datetime.strptime(date2, format)
    difference = relativedelta(parsed_date2, parsed_date1)
    months_difference = difference.years * 12 + difference.months
    return months_difference
def convert_to_year_month(months):
    years = months // 12
    remaining_months = months % 12

    if years == 0:
        return f"{remaining_months}개월"
    elif remaining_months == 0:
        return f"{years}년"
    else:
        return f"{years}년 {remaining_months}개월"

date1 = input("첫 번째 날짜를 입력하세요 (YYYY-MM-DD): ")
date2 = input("두 번째 날짜를 입력하세요 (YYYY-MM-DD, 엔터시 오늘): ")

if date2=="":
    today = datetime.today()
    date2 = today.strftime("%Y-%m-%d")

days_difference = calculate_date_difference(date1, date2)
months_difference=calculate_month_difference(date1,date2)

print("")

print("두 날짜 간의 일 수 차이:", days_difference,"일")
print("두 날짜 간의 월 수 차이:", months_difference,"개월")
print("두 날짜 간의 년 수 차이:", convert_to_year_month(months_difference))

input()
