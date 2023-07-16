'''
*참고로 틀린 답안임*

1. 문자열 하나씩 입력받으면서 확인
 1) 닫는 괄호 뒤에 숫자가 나오면 여는 괄호가 나올때까지 거꾸로 탐색하면서 곱하기
 2) 대문자이면 원소의 시작이므로 이전 문자 확인 -> 영어면 1 생략되었으니까 1 넣어줌 / 숫자면 그대로 진행
 3) 여는 괄호, 닫는 괄호도 마찬가지로 이전 문자 확인해서 1 생략 여부 판단

2. 이후 원소와 개수를 분리한 후 사전 순으로 정렬하고 출력

근데 테케가 ((())) 이럴 줄은 몰랐음;; 세상엔 다양한 원소가 있구나...
'''

while True:
    try:
        words = input()
        rlt = []
        for word in words:
            # 숫자
            if word.isnumeric() and rlt[-1] == ')':
                rlt.pop()
                idx = -1
                while rlt[idx] != '(':
                    if rlt[idx].isnumeric():
                        rlt[idx] = str(int(rlt[idx]) * int(word))
                    idx -= 1
                rlt.pop(idx)
                continue
            # 대문자
            if word.isalpha() and word.isupper():
                if rlt and rlt[-1].isalpha():
                    rlt.append('1')
            # 여는 괄호
            elif word == '(':
                if rlt and rlt[-1].isalpha():
                    rlt.append('1')
            elif word == ')':
                if rlt and rlt[-1].isalpha():
                    rlt.append('1')
            rlt.append(word)
        if rlt[-1].isalpha():
            rlt.append('1')

        temp = {}
        l = r = 0
        while r != len(rlt):
            if rlt[r].isnumeric():
                ele = ''
                for i in range(l, r):
                    ele += rlt[i]
                num = ''
                while r != len(rlt) and rlt[r].isnumeric():
                    num += rlt[r]
                    r += 1
                if ele in temp.keys():
                    temp[ele] += int(num)
                else:
                    temp[ele] = int(num)
                l = r
            else:
                r += 1

        # 사전 순으로 정렬하고 출력 (숫자 1이면 생략)
        ans = ''
        for ele in sorted(list(temp.keys())):
            if temp[ele] != 1:
                ans += str(temp[ele])
            ans += ele + '+'
        print(ans[:-1])
    except EOFError:
        break