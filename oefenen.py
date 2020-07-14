text = '7 days 24 hours'
a= 0
b= 0
for i in text.replace(' ',''):
    if i.isdigit():   
        a+=1
    else:
        b +=1
print(a,b) 

#isalpha harf sayar