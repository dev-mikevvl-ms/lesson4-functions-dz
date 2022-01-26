import sys
from MVVlStd import teSep_s

tTskMsg_s = '''
Задача 4. МОДУЛЬ 2 файл borndayforewer.py
Предлагается модернизировать программу из прошлого дз используя
 хотя бы 1-у функцию, подробности в файле
'''
print(teSep_s, tTskMsg_s, f'{sys.version=}', teSep_s, 'Result:', '',  sep='\n')
"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

# year = input('Ввведите год рождения А.С.Пушкина:')
# while year != '1799':
#     print("Не верно")
#     year = input('Ввведите год рождения А.С.Пушкина:')

# day = input('Ввведите день рождения Пушкин?')
# while day != '6':
#     print("Не верно")
#     day = input('В какой день июня родился Пушкин?')
# print('Верно')

def tAnswQueInPWChe_fif(la1stQue_s, laAnsw_s, laOthQue_s=None,
    laFailMsg_s='Не верно', laOkMsg_s='Верно'):
  li_s = input(f'{la1stQue_s}')
  while li_s != laAnsw_s:
    if laFailMsg_s: print(laFailMsg_s)
    li_s = input(f'{laOthQue_s if laOthQue_s else la1stQue_s}')
  else:
    if laOkMsg_s: print(laOkMsg_s)
    return True

tRes_l = []   
tRes_l.append(tAnswQueInPWChe_fif('Ввведите год рождения А.С.Пушкина:',
    '1799', laOkMsg_s=None))
tRes_l.append(tAnswQueInPWChe_fif('Ввведите день рождения Пушкин?', '6',
  'В какой день июня родился Пушкин?'))
tRes_l


print(teSep_s)