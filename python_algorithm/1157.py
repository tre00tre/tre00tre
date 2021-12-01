str = input().upper()
word = list(set(str))

cnt_list = []

for x in word:
    cnt = str.count(x)
    cnt_list.append(cnt)
    
if cnt_list.count(max(cnt_list)) > 1 :
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    print(word[max_index])



# 틀림 뭐 틀렸는지 찾기
str = input().upper()
word = list(set(str))

cnt = []

for i in word:
    cnt.append(str.count(i))
    
if cnt.count(max(cnt)) > 1 :
    print('?')
else:
    print(word[cnt.index(max(cnt))])
