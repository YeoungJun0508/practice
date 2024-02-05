
def gugudan(dan):
    print("f{dan}단을 출력합니다:")
    for i in range(1,10):
        result = dan *i
        print(f"{dan} x {i} = {result}")

def main():
    try:
        dan = int(input("몇단을 출력할지 입력해주세요: "))
        gugudan(dan)
    except Error:
        print("1~9까지만 입력하시오. ")

if __name__=="__main__":
    main()