import string
import random
def encoding(s):
    l=len(s)
    N=3
    if(l>=3):
        ls=list(s)
        ls.pop(0)
        ls.append(s[0])
        str=""
        for e in ls:
            str+=e
        str1 = "".join(random.choices(string.ascii_lowercase , k=N))
        str2 = "".join(random.choices(string.ascii_lowercase , k=N))
        strR=str2+str+str1
        print(strR)
    else:
        str=s[::-1]
        print(str)
def decoding(s):
    l=len(s)
    str=""
    StrR=""
    if(l<3):
        str=s[::-1]
        print(str)
    else:
        ls=list(s)
        ls.pop(0)
        ls.pop(0)
        ls.pop(0)
        ls.pop(-1)
        ls.pop(-1)
        ls.pop(-1)
        for e in ls:
            str+=e
        ls=list(str)
        ls.pop(-1)
        ls.insert(0,str[-1])
        for e in ls:
            StrR+=e
        print(StrR)
while True:
    ch=int(input("Enter:\n 1 : for Encoding \n 2 : for decoding \n 3 : Exit\n"))
    if(ch==1):
        st=input("Enter a string for encoding\n")
        encoding(st)
    elif(ch==2):
        st=input("Enter a string for decoding\n")
        decoding(st)
    elif(ch==3):
        print("Programm end")
        quit()
    else:
        print("Wrong choice")
