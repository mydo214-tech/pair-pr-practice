def review_notice():
    # 사용자에게 입력을 받는다.
    user_input = input("정수를 입력하세요: ")

    # 입력값이 정수인지 확인한다.
    if user_input.isdigit():
        number = int(user_input)
        # 짝수인지 홀수인지 확인한다.
        if number % 2 == 0:
            print(f"{number}은(는) 짝수입니다.")
        else:
            print(f"{number}은(는) 홀수입니다.")
    else:
        print("유효한 정수를 입력하세요.")

review_notice()
