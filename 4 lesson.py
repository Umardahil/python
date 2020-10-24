#Dictionary.
# dict_with_pairs = {'ключ1': 'значение', 'ключ2': 'значение2'}
# dict_ = {3: 1, 3.4: 2, 3: 2}
# print(dict_)

# names = {'name1': 'john', 'name2': 'tom'}
# print(names['name1'])
# print(names['name2'])

# dictionary = dict.fromkeys(['key1', 'key2'])
# print(dictionary)
# dictionary2 = dict.fromkeys(['key1', 'key2'], ['val1', 'val2']) #V dannom sluchae my otnesli spisok k 1 i 2 key(val1
# # ival2 eto spisok)
# print(dictionary2)
 #Izvle4eniye dannyh iz slovorya

# test = {'name': 'john', 'lastname': 'snow'}
# print(test['name'])
# print(test['lastname'])
# print(test['key'])

  #Eto tipa toje dictionary
# dictionary = {}
# dictionary[1] = 1
# print(dictionary)
# dictionary['dictionary2'] = {2:2}
# print(dictionary)
# dictionary['dictionary2'][3] = 3
# print(dictionary)
# print(dictionary['dictionary2'][3])

#Method get получает по ключу значение

# cars = {'mers': '221', 'bmw': '750i', 'subaru': 'impreza'}
# print(cars.get('subaru')) 1sposob # oba sposoba iwut po klyuchu znachenie
# print(cars['subaru']) 2 sposob

#Method keys vivodit vse klyuchi

# cars = {'mers': '221', 'bmw': '750i', 'subaru': 'impreza'}
# print(cars.keys())
# cars_list = cars.keys()
# print(cars_list)
# print(len(cars))
# mersedes = cars.get('mers')
# print(mersedes)

#Method values vivodit vse znacheniya( to chto stoit posle klyucha)
#
# cars = {'mers': '221', 'bmw': '750i', 'subaru': 'impreza'}
# print(cars.values())
# print(type(cars.values()))


#Method pop udalyaet po key i vozvrawaet znachenie

# Suckmydick = {'bla': '1st', 'bla2': '2nd', 'bla3': '3rd'}
# print(Suckmydick)
# bla = Suckmydick.pop('bla')
# print(Suckmydick)
# print(bla)

#Method popitem vyrezaet posledniy key i ego znachenie

# cars = {'mers': '221', 'bmw': '750i', 'subaru': 'impreza'}
#
# deleted = cars.popitem()
# print(deleted)


#Method updates ob'edinyaet slovari v odin

# laptops = {'lenovo': 'yoga', 'mackbook': 'pro', 'asus': 'zephyrus'}
# laptops2 = {'dell': 'allienware'}
# laptops3 = {'mackbook33': 'air'}
# print(laptops)
# laptops.update(laptops2)
# laptops.update(laptops3)
# print(laptops)


#Method setdefault: vivodit znachenie klyucha

# dict_ = {'key1':1, 'key2': 2, 'key3': 3}
# new_dict = dict_.setdefault('key2') #1 sposob
# print(new_dict)
# new = dict_['key2']       #2 sposob
# print(new_dict)
# new2 = dict_.get('key2')       #3sposob
# print(new2)

#EWe odin sposob sozdaniya dictionary

# capitals = dict(russia = 'moscow', kyrgyzstan = 'bishkek', usa = 'ny')
# print(capitals)
# capitals = dict([('russia', 'moscow'), ('kyrgyzstan', 'bishkek')])
# print(capitals)

# Mnozhestvo/set udalyaet odinakovie znacheniya

# set_ = [1,2,3,4,5,6,4,3,2]
# print(set_)
# set_ = set(set_)
# print(set_)


#Method addn dobovlyaet element
# set_ = {1,2,3}
# print(set_)
# print(type(set_))
# set_.add(4)
# print(set_)

#Method remove udalyaet opr element
#
# set_ ={1,2,9,4,7,8,9}
# print(set_)
# set_.remove(1)
# print(set_)

# #Method discard tak je udalyaet
#
# set_ = {2,3,5,1,6,8,9}
#
# set_.discard(5)
# print(set_)

#Method pop virezaet element

# set_ = {1,2,3,4,5,6,7,8,9}
# print(set_.pop())