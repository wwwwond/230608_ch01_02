# (콘솔로부터) 입력을 받아서 입력값을 변수에 저장
# input 함수 사용하기
# input() in-put
# a = input() # input -> (실행창을 통해) 입력을 받으면 -> a라고 하는 변수에 저장
# print(a) # a를 출력
# input의 결과를 변수에 할당
# 가이드 메시지를 입력
# x = input("오늘은 무엇을 드셨습니까?")
# print(x)
# 입력은 input, 출력은 print.
# input(" 이곳에 작성된 문자열을") 프롬프트라 한다
# -> 사용자에게 입력받는 값의 용도를 알려줄 때 사용

# a = int(input('첫 번째 숫자 입력 : '))
# b = int(input('두 번째 숫자 입력 : '))
# # input을 통해서 입력 받은 값('문자열')을 정수로 변환
# print(a + b) # 정수끼리 연산을 하면 -> 정수.(숫자)
# print(type(a), type(b))
# # 입력 값을 변수 두 개에 저장하기
'''
* input 한 번에 값을 여러 개 입력 받으려면,
  input에 split을 사용하여 변수 여러 개에 저장.
  (각 변수는 콤마로 구분)
* 변수1, 변수2 = input().split()
* 변수1, 변수2 = input().split('기준문자열')
* 변수1, 변수2 = input('문자열').split()
* 변수1, 변수2 = input('문자열').split('기준문자열')
'''
# a, b = input('문자열 두 개를 입력하세요: ').split()
# # split() -> 입력받은 값(input)을 공백(스페이스) 기준으로 분리
# print(a)
# print(b)
# print(c)

# 두 숫자를 한 번에 입력 받아서 합 구하기
# a, b = input("숫자 두 개를 입력하세요(스페이스로 구분): ").split()
# print(a+b)
#
# a = int(a) # 문자열이 담긴 변수를, 정수로 변환한 뒤 다시 대입
# b = int(b) # 문자열이 담긴 변수를, 정수로 변환한 뒤 다시 대입
# print(a+b)

# map에 int와 input().split()을 넣으면 split의 결과를 모두 int로 변환(실수로 변환할 때는 int 대신 float를 넣음)
'''
변수1, 변수2 = map(int, input().split())
변수1, 변수2 = map(int, input().split('기준문자열'))
변수1, 변수2 = map(int, input('문자열').split())
변수1, 변수2 = map(int, input('문자열').split('기준문자열'))
'''
# map(짝지을 함수이름, 대상이 되는 여러 값을
a, b = map(int,input("숫자 두 개를 입력하세요 (스페이스로 구분):  ").split())
print(a + b)
a, b = map(int, input("숫자 두 개를 입력하세요 (콤마(,) 구분): ").split(','))
print(a + b)
