## 주의 !! ##
## 미해결 ##

import sys
from collections import defaultdict
input = sys.stdin.readline

while True :
    words = input().rstrip()
    if not words : break

    temp = ''
    dic = defaultdict(int)
    state = 0
    for i in range(len(words)) :
        if words[i] == '(' :
            st = []
            state = 1
            continue

        elif words[i] == ')' :
            print(st)
            for w in st :
                print(dic[w[0]],w[1]*int(words[i+1]))
                dic[w[0]] += w[1]*int(words[i+1])
            st.clear()
            temp = ''
            state = 0
            continue

        if state : # 괄호 열려있을 때
            if words[i].isupper() :
                if temp :
                    st.append((temp,1))

                temp = ''
                temp += words[i]

            elif words[i].islower() :
                temp += words[i]
                if i+1 < len(words) and words[i+1].isdecimal() :
                    continue
                else :
                    st.append((temp,1))
                    temp = ''


            elif temp and words[i].isdecimal() :

                if i+1 < len(words) and words[i+1].isdecimal() :
                    st.append((temp,int(words[i]+words[i+1])))
                else :
                    st.append((temp, int(words[i])))
                temp = ''

        else :

            if words[i].isupper() :
                if temp :
                    if dic[temp] :
                        dic[temp] += 1
                    else :
                        dic[temp] = 1
                temp = ''
                temp += words[i]

            elif words[i].islower() :
                temp += words[i]
                if i + 1 < len(words) and words[i+1].isdecimal():
                    continue
                else:
                    dic[temp] += 1
                    temp = ''

            elif temp and words[i].isdecimal() :
                if i+1 < len(words) and words[i+1].isdecimal() :
                    dic[temp] += int(words[i]+words[i+1])
                else :
                    dic[temp] += int(words[i])
                temp = ''

    if temp :
        dic[temp] += 1

    itemList = []
    for key in dic.keys() :
        itemList.append(key)

    itemList.sort()
    ans = ''
    for item in itemList :
        if dic[item] == 1 :
            p = item
        else :
            p = str(dic[item]) + item
        ans += (p + '+')

    print(ans[:-1])
