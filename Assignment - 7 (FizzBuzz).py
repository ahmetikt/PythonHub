list1 = list(range(1, 101))
# print(list1)
for i in list1:
    if i % 3 == 0 and not i % 15 == 0:
        print('Fizz')
    elif i % 5 == 0 and not i % 15 == 0:
        print('Buzz')
    elif i % 15 == 0:
        print('FizzBuzz')
    else:
        print(i)
