#노마드코더 파이썬 챌린지 4일차 코드를 만들어 보았다
#이게 정확한 답인지는 모르겠다
#단순한 계산기를 만들었고 if문과 while문을 활용했다



























playing = True

while playing:
    first = int(input("choose number"))

    second = int(input("choose another number"))

    op = input("choose an operation \n options are: + , -, * or /. \n write 'exit' to finish.")
    
    if op == '+':
        print(first + second)

    elif op == '-':
        print(first - second)

    elif op == '*':
        print(first * second)

    elif op == '/':
        print(first / second)
    
    if op == 'exit':
    	playing = False
      
      
      
      
