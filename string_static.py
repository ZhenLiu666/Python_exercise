# 输入一行字符，分别统计出其中英文字母，空格，数字和其它字符的个数
import string

s=input(' input a string: ')
letter=0
space=0
digit=0
other=0
for c in s:
    if c.isalpha():
        letter+=1
    elif c.isspace():
        space+=1
    elif c.isdigit():
        digit+=1
    else:
        other+=1
print('There are %d letter, %d spaces, %d digits \
and %d other characters in your string.'\
     %(letter,space,digit,other))
    
