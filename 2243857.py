import csv
import os

FILENAME = 'account_book.csv'

# CSV 파일 초기화 (없으면 만들기)
def init_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['날짜', '분류', '내용', '금액'])  # 헤더

# CSV 내용 전체 초기화 (헤더만 유지)
def reset_file():
    with open(FILENAME, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['날짜', '분류', '내용', '금액'])  # 헤더
    print("📂 가계부 내역이 초기화되었습니다.\n")

# 현재 총 잔액 계산
def get_current_balance():
    total = 0
    if not os.path.exists(FILENAME):
        return total
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        next(reader, None)  # 헤더 건너뛰기
        for row in reader:
            try:
                amount = int(row[3])
                if row[1] == '수입':
                    total += amount
                elif row[1] == '지출':
                    total -= amount
            except:
                continue
    return total

# 수입/지출 입력
def add_entry():
    date = input("날짜 (예: 2025-06-07): ")
    
    # 분류를 번호로 선택
    while True:
        print("분류 선택:")
        print("1. 수입")
        print("2. 지출")
        category_input = input("선택 (1/2): ")
        if category_input == '1':
            category = '수입'
            break
        elif category_input == '2':
            category = '지출'
            break
        else:
            print("❌ 잘못된 입력입니다. 다시 선택해주세요.\n")

    description = input("내용: ")
    amount_str = input("금액: ")

    try:
        amount = int(amount_str)
    except ValueError:
        print("❌ 금액은 숫자만 입력해야 합니다.\n")
        return

    if category == '지출':
        current_balance = get_current_balance()
        if amount > current_balance:
            print(f"❗️현재 잔액({current_balance}원)보다 많은 금액은 지출할 수 없습니다.\n")
            return

    with open(FILENAME, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, category, description, str(amount)])
    
    print("✅ 저장되었습니다.\n")

# 전체 내역 보기
def view_entries():
    print("\n📋 가계부 내역:")
    total = 0

    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        next(reader, None)  # 헤더 건너뛰기
        for row in reader:
            print(row)
            if row[1] == '수입':
                total += int(row[3])
            elif row[1] == '지출':
                total -= int(row[3])
    
    print(f"\n💵 현재 총액: {total} 원\n")

# 메뉴
def menu():
    init_file()
    while True:
        print("========== 가계부 메뉴 ==========")
        print("1. 내역 추가")
        print("2. 전체 내역 보기")
        print("3. 내역 초기화")
        print("4. 종료")
        choice = input("선택 (1/2/3/4): ")

        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            reset_file()
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.\n")

# 실행
if __name__ == '__main__':
    menu()

