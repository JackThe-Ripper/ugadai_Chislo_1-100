import random
from random import randint

print('Я загадал число от 0 до 100. Попробуй угадай!')

x = randint(0, 100)
answer = int(input('Я думаю это число '))

while answer != x:
    if x > answer:
        print('Больше!')
    else:
        print('Меньше!')
    answer = int(input('Я думаю это число '))
print('Угадал!')
