# Работа со словарями
my_dict = {'Sasha': 1996, 'Dasha': 1995, 'Liza': 2017, 'Sonya': 2022}
print(my_dict)
print(my_dict['Sasha'])
my_dict['Dima'] = 2004
print(my_dict)
my_dict.update({'Lesha': 1979, 'Tanya': 1977})
print(my_dict)
del (my_dict['Dima'])
print(my_dict)

# Работа с множествами
my_set = {'Sasha', 'Dasha', 'Liza', 'Sonya', 'Sasha', 'Dasha', 'Liza', 'Sonya'}
print(my_set)
print(my_set.add('Lesha'))
print(my_set.add('Tanya'))
print(my_set)
print(my_set.discard('Lesha'))
print(my_set)