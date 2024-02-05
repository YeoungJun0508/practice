

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y!=0:
        return x/y
    else:
        print("나눌 수 없습니다.")


def calculator():
    while True:
        num1= float(input("첫번째 숫자를 입력하시오."))
        operator = input("연산자를 입력하세요 (+, -, *, /): ")
        num2 = float(input("두번째 숫자를 입력하시오."))

        if operator =='+':
            result = add(num1,num2)
        elif operator =='-':
            result = subtract(num1,num2)
        elif operator =='*':
            result = multiply(num1,num2)
        elif operator == '/':
                result = divide(num1, num2)
        else:
            print("올바르지 않은 연산자입니다.")
            continue
        print(f"결과: {result}")

        u_input = input("더 계산하시겠습니까? (y/n):")
        if u_input.lower() != 'y':
            break


# 계산기 실행
calculator()