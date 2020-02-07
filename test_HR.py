'''
Minion Game->
def minion_game(string):
    length = len(string)
    if length>0 and length<=10**6:
        vowels = 'AEIOU'
        sumv = 0
        sumc = 0
        for i in range(len(string)):
            #print(i)
            if string[i] in vowels: #Kevin
                    #print('vowels')
                    sumv = sumv+((length-i)*1)
            else:#stuart
                        #print('consonents')
                    sumc = sumc+(1*(length-i))
        #print(dv)
        if sumc>sumv:
            print('Stuart', sumc)
        elif sumc<sumv:
            print('Kevin', sumv)
        else:
            print('Draw')'''



'''def merge_the_tools(string, k):
    length_str = len(string)
    if length_str>=1 and length_str<=(10**4) and k>=1 and k<= length_str:
        for i in range(0,length_str,k):
            stri = string[i:i+k]
            av=''
            for j in stri:
                if j not in av:
                    av=av+j
            print(av)'''
            
'''def count_substring(string, sub_string):
    len_string = len(string)
    count=0
    len_sub_string = len(sub_string)
    if len_string>=1 and len_string<=200:
        for i in range(len_string):
            if string[i]==sub_string[0]:
                if string[i:i+len_sub_string]==sub_string:
                    count+=1          
    return count'''


'''
from collections import OrderedDict 
n = int(input())
if n>=1 and n<=10**5:
    list_of_words = OrderedDict()
    sum_of_len = 0
    count_of_words = 0
    for i in range(n):
        
        if sum_of_len<=10**6:
            av = str(input())
            sum_of_len = sum_of_len+len(av)
            if av not in list_of_words.keys():
                list_of_words[av]=1
            else:
                count_of_words+=1
                list_of_words[av]+=1
                
            
    print(len(list_of_words))
    for i in list_of_words.values():
        print(i, end = ' ')'''




'''# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
N=int(input())
if N>0 and N<=100:
    d = deque()

    for i in range(N):
        av = str(input())
        op = av.split(' ')[0]
        #print(op)
        try:
            val = int(av.split(' ')[1])
            exec("d.%s(%d)" % (op,val))
        except IndexError:
            exec("d.%s()" % (op))
        #print(val)
                        
    
    for j in d:
        print(j, end=' ')'''



'''def solve(s):
    if len(s)>0 and len(s)<1000:
        coolman = []
        av = s.split()
        for i in av:
            coolman.append(i.capitalize())
        cool = ' '.join(coolman)
    return cool '''


'''from collections import OrderedDict 
n = int(input())
if n>0 and n<=100:
    list_of_words = OrderedDict()
    for i in range(n):
        av = str(input())
        name = ' '.join(av.split()[:-1])
        val = int(av.split()[-1])
        
        if name not in list_of_words.keys():
            list_of_words[name]=val
        else:
            list_of_words[name]+=val

    for i in list_of_words.keys():
        print(i, list_of_words[i])'''



'''for t in range(int(input())):
    input()
    lst = [int(i) for i in input().split()]
    min_list = lst.index(min(lst))
    left = lst[:min_list]
    right = lst[min_list+1:]
    if left == sorted(left,reverse=True) and right == sorted(right):
        print("Yes")
    else:
        print("No")'''

n = str(input())
n = list(n)
from collections import Counter

keys = Counter(n).keys()
vals = Counter(n).values()
keys = list(keys)
vals = list(vals)

print(Counter(n).keys()) # equals to list(set(words))
print(Counter(n).values()) # counts the elements' frequency    
dict_={}
for i in range(len(vals)):
    dict_[keys[i]]= vals[i]
dict_1 = dict(sorted(dict_.items(), key = 
             lambda kv:(kv[1], kv[0]),reverse = True))

dict_1 = dict(sorted(dict_.items(), key = 
             lambda kv:(kv[1], kv[0]),reverse = True))


from collections import Counter
for each in Counter(sorted(input())).most_common(3): print(*each)


str = raw_input()
print any(c.isalnum()  for c in str)
print any(c.isalpha() for c in str)
print any(c.isdigit() for c in str)
print any(c.islower() for c in str)
print any(c.isupper() for c in str)




import time
time.time()
'abab'.replace('ab','12')

Exception 






i=1
while True:
    if i%5==0:
        break
    print(i)
    i+=1

x=(1,2,3)
y=(4,5,6)
z=x+y
print(z)
bool(5)


