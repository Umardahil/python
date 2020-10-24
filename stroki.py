
# method split делит строку по разделителю на отдельные слова.

# text = 'Hello, World'
# print(text.split(','))

#method isdigit проверяет все ли символы в строке цифры/ определяет ложь ии истина

# num = input('enter a number: ')
# print(num.isdigit())

#Method isalpha проверяет является ли символы в стркое буквами

# text = input('input here: ')
# print(text.isalpha())

#Method isalnum проверяет все ли символы в строке цфиры или бкувы

# text= input('say: ')
# print(text.isalnum())

#Method replace заменяет часть строки

# string = 'Powel Nhui'
# print(string.replace('Powel', 'good'))
# print(string.replace('o', '*',))

#Method isupper проверят все ли символы в верхнем регистре(то есть с заглавными буквами)

# text= input('enter :')
# print(text.isupper())

#Method islower проверят все ли символы в нижнем регистре (то есть с мелнькой буквы)

# text = input('enter something: ')
# print(text.islower())

#Method isspace проверяет все ли символы пробелы, табы либо переводы строки

# text= input('something: ')
# print(text.isspace())

#Method istitle проверят является ли строка заглавной

# text1 = 'hi bla'
# text2 = 'Hi bla'
# print(text1.istitle())
# print(text2.istitle())

#Method Lower перевод букв в нижний регистр

# text = 'Hello World'
# text2 = text.lower()
# print(text2)
# print(text)

#Method upper переводит буквы в верхний регистр

# string = 'Hello suka'
# print(string.upper())

#Method startwith проверят начинается ли строка с определенных символов

# text = 'Hello suka'
# print(text.startwith('h'))

#Method emdwith проверят заканчивается ли строка на какие либо символы

# mail = 'ezample.com'
# print(mail.endswith('.com'))

#Method join склеивает строку из разных частей

# text = 'hello, my name is Blabla'
# text_splited = text.split()
# print(text_splited)
# text2 = '+'.join(text_splited)
# print(text2)

#Method ord определяет цифры символов на клаве

# print(ord('d'))
# print('a' < 'd')

#Method count считает количество символов в тексте(совпадений) которые мы передаем в скобках

# text ='Privet mir'
# print(text.count('e'))

#Method strip, lstip, rstrip удаляет  пробелы  в начале и конце строки
#
# text = '    Hello suka    '
# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())

#Method swapcase меняет регистр на противоположный

# text = 'Hello World'
# text2 = 'heLLo wOrld'
# print(text.swapcase())
# print(text2.swapcase())

#Срез строки начинается с нуля 1-начало 2-конец -3шаг через

# text = 'Helloo world'
# print(text[0:8:2])

#Алгоритм по проверке явл ли слово палиндромом

# text = input('enter something: ')
# if text == text[::-1]:
#     print('its right')
# else:
    # print('Its not right')

#Форматирование строк
#
# name = input('enter your fucking name: ')
# age = input("enter your fuckin age: ")
# print('Your name ' + name + '. your age' + age )  два разных способа
# # print(f'Your name {name}. your age {age}. ')    этот легче и быстрее (ф строка)
# # print('hello, %s' % name)    старый код
# print('hello, {}'.format(name)) еще  один варинат

# text ='''dljavjdbvjkbsvjjjjjjkdsbdvkjbsvjbdvjbskdbvkjbsvkjbsvbdsvbdsvdsbvkjbdsjvbdsjbvkjdbvs'''
# print(text)

# text = 'hello \t world'
# print(text)

