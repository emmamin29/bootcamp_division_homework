"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    num = int(input())
    sum=0
    fac = 1
    #합 출력
    for i in range(num+1):
        sum += i
    print(sum)

    #팩토리얼
    for i in range(num):
        num2= i+1
        fac *=num2  
    print(fac)
    return


if __name__ == '__main__':
    main()
