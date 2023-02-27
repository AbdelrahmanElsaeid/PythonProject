
#------------------------Print the frequency of each character in String-----------------
string = "Hello my name is Mohamed and I work at school"
d = {}
l = []
for letter in string:
    l.append(letter)
for i in l:
    if i==' ':
        l.remove(i)     
for i in l:
    if i in d:
        continue
    else:
        c = 0
        for j in l:
            if i==j:
                c = c+1
                d[i]= c

print(d)    
        



