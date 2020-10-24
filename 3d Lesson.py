# Lists/ списки

#Method append дополняет список элементами

# list_ = []
# list_.append('wwww')
# print(list_)
# print(len(list_))
# list_.append('hello')
# print(list_)
# print(len(list_))
# string = ' '.join(list_)
# print(string)
# list_.append(['good', 'bye'])
# print(list_)
# print(len(list_))

#range(диапазон) создание списков каких то чисел

# list1 = list(range(1, 50, 4))
# print(list1)


#method insert получает два аргумента, первый это индекс(куда добавить), второй это сам элемент

# cars = ['mersedes', 'subaru', 'Honda']
# print(len(cars))
# cars.insert(0, 'toyota')
#ноль это индекс то есть это в какую часть надо вставить слово 0 в этом случае это место первого
# слова
# print(cars)
# list1 = list(range(1,5))
# cars.insert(2, list1)
# print(cars)
# # print(len(cars))
# list1 = []
# list1.append(cars)
# print(list1)
# print(len(list1))
# print(len(cars))

#method remove удаляет элемент по названию

# Laptops = ['lenovo', 'asus', 'aser', 'hp', 'acer']
# print('before remove', Laptops)
# Laptops.remove('acer')
# print('after remove', Laptops)

#Method pop удаляет и возвращает элемент/по умолчанию последний

# programming = ['c', 'python', 'js', 'go', 'java']
# print('before', programming)
# last_element = programming.pop()
# print('after', programming)
# print(last_element)

#Method index возвращает(находит индекс элемента) индекс элемента

# movies = ['звездные войны', 'джентельмены', 'why him?', 'godfather', '1+1']
# print(movies.index('1+1'))
#
# number_in_list = movies.index('1+1') далее идет манипуляция то есть можем прибавлять или умножать и тд номер индекса
# print(number_in_list)
# print(number_in_list ** number_in_list)
# print(type(number_in_list))


#Method count считает количество элементов

# list1 = ['apple', 'banana', 'pineapple', 'strawberry', 'apple']
# print(list1.count('banana'))
# string = 'hello world'
# print(string.count('l'))

# list2 = list(string) если стринг закинуть туда будет разделение на буквы в случае списка (list)
# print(list2)
# splited = string.split()  na slova delit
# print(splited)

#Method reverse разворачивает список в оратную сторону только к спискам относится
#
# list_ = [1,2,3,4,5,6]
# print(list_)
# list_.reverse()
# print(list_)

# Метод обратки со строкой
# string = 'Hello world'
# print(string[::-1]) перед вервым двоеточием это начало передв вторым это конец а треться цифра это направление-1
# это значит в обратную сторону
# Второй вариант
# string = 'hello world'
# simple = string[::-1]
# new = list(string)
# new.reverse()
# new_string = ''.join(new)
# print(new_string)
# print(simple)


#Method sort сортирует элементы в списке по ключу

# numbers = [3,2,5,4,1] #тут мы сортируем цифры по порядку
# print(numbers)
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)  #тут мы сортируем наоборот
# print(numbers)
# list21 = ['qrrrr', 'wee', 'ew', 'qerqwr']  #тут мы соритируем от самого маленкого слова к большому
# list21.sort(key=len)
# print(list21)

#Method copy копирует список

# list1 = ['apple', 'banana', 'pineapple', 'strawberry', 'apple']  #тут мы копируем алгоритм копирования
# new_list = list1.copy()
# print(new_list)
# print(list1)
#
# new_list.append('huina')   #тут мы вставили еще одно солова хуйего зачем
# print(new_list)
# print(list1)

#Method extend расширяет список дркгим списком(складывает)

# nums = [1,2,3]   #скалдываем то есть прибавляем списки
# nums2 = [4,5,6]
# # nums = nums + nums2
# # nums.extend(nums)  #второй варинат
# nums += nums2      # третий вариант
# print(nums)

# #Method clear очищает список
#
# nums = [1,2,3,4,5,6,7]
# print(nums)
# nums.clear()
# print(nums)

#
# nums = [1,2,3,4,5,6]
# print(nums[5])

