import sys
from MVVlStd import teSep_s, teInPWTypedWVali_fif
# Mod:MVVlStd.py
# Distributed under the BSD license, version:BSD-3-Clause.
# Copyright © 2022 Mike Vl. Vlasov <dev.mikevvl@outlook.com>.
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# See:(https://opensource.org/licenses/BSD-3-Clause).

teSep_s = '_' *80

def teInPWTypedWVali_fif(laWhatInPMsg_s, laInPValues_co=1, laValiInPMsg_s='',
    laVali_cll=None, laInPTypeFlt_cll=int, laMaxInPTry_co=11,
    laAcceptEmptyInPAsDf_b=False, laDfV_s=None, laVerbose_i=None) -> tuple:
  if laInPValues_co < 1: raise ValueError(f'laInPValues_co must be > 0, now:{laInPValues_co}')
  loTypeAValiFlsCo_l, loRes_l, loMaxTry_co = [0, 0], [], int(max(laInPValues_co, laMaxInPTry_co))
  if laValiInPMsg_s and laVali_cll:
    lo_s = f' - your value will be validated as({laValiInPMsg_s}) -'
  else: lo_s = ''
  lo_s = f"Please, Input{laWhatInPMsg_s}{lo_s} and press Enter"
  if laAcceptEmptyInPAsDf_b and laDfV_s is not None:
    lo_s += f"(on default '{laDfV_s}')"
  loInPMsg_s = f"{lo_s}: "
  for l_co in range(loMaxTry_co):
    li_s = input(loInPMsg_s)
    if li_s == '' and laAcceptEmptyInPAsDf_b and laDfV_s is not None:
      li_s = laDfV_s # 2Do: Che: laDfV_s is str OR UpLi
    # if not li_s: ??User(Exit|Bre) ??laAcceptEmpty(As(Df|Bre))InP_b=False
    try:
      if laInPTypeFlt_cll is not None:
        liChe_i = laInPTypeFlt_cll(li_s)
      else: liChe_i = li_s
    except ValueError as leExc_o:
      loTypeAValiFlsCo_l[0] +=1; liChe_i = None
      print(f"\tERR: You input:'{li_s}' NOT pass check type w/func({laInPTypeFlt_cll}",
          f'- Exception:{type(leExc_o).__name__}({leExc_o}) raised.')
    else:
      if laVali_cll is not None:
        if laVali_cll(liChe_i):
          loRes_l.append(liChe_i)
          print(f"\tMSG: You input:'{liChe_i}' valid.")
        else:
          loTypeAValiFlsCo_l[1] +=1
          lo_s = f' because of NOT {laValiInPMsg_s}' if laValiInPMsg_s else ''
          print(f"\tERR: You input:'{liChe_i}' INVALID{lo_s}.")
      else:
        loRes_l.append(liChe_i)
        print(f"\tMSG: You input:'{liChe_i}'.")
        # if liChe_i == tPtt_i: tOk_co +=1
    # print(f'DBG: {loRes_l=}')
    if len(loRes_l) == laInPValues_co: break  
    if laMaxInPTry_co:
      if l_co == int(loMaxTry_co -1):
        if loRes_l:
          print(f"\tWRN: Rich max(laInPValues_co, laMaxInPTry_co):{loMaxTry_co}, return {tuple(loRes_l)} as User input.")
        else:
          raise ValueError(f'Rich max(laInPValues_co, laMaxInPTry_co):{loMaxTry_co} but loRes_l is Empty - nothing return as User input.')
      else:
        lo_s = '' if l_co == (loMaxTry_co -2) else 's'
        lo_s = f' and {loMaxTry_co - l_co -1} attempt{lo_s} left'
    else: lo_s = ''
    print(f'MSG: It remains to input {laInPValues_co - len(loRes_l)} more value{lo_s}.')
  return tuple(loRes_l)
# print(teInPWTypedWVali_fif(laInPValues_co=2, laInPTypeFlt_cll=float, laMaxInPTry_co=1),
#  teInPWTypedWVali_fif(laValiWhatInPMsg_s=tCndInPMsg_s,
#   laVali_cll=lambda x: x in tValiV_t)
#   )
# t_s = '' if tOk_co == 1 else 's'
# print(f"You input '{tPtt_i}' {tOk_co} time{t_s} of {tTime_co} attempts.")

# tTime_co, tPtt_i, tOk_co, tFls_co = 10, 5, 0, 0

# tResLLen_co = int(teInPWTypedWVali_fif(laVali_cll=lambda _i: 0 < _i < 10,
#     laWhatInPMsg_s=' Количество элементов будущего списка',
#     laValiInPMsg_s=' a Integer 0 < _i < 10')[0],
#     )
# print(f'В списке будет {tResLLen_co} элементов.')
# tValiV_t = tuple(range(0, 10))
# tValiV_t = ('Y', 'N')
# tCndInPMsg_s = f' (по очереди по одной вводите любые цифры) a Integer OneOf{tValiV_t}'
# tRes_l = list(teInPWTypedWVali_fif(f' по очереди по одной любые цифры {tResLLen_co} раза',
#     laInPValues_co=tResLLen_co, laValiInPMsg_s=f'a Integer OneOf{tValiV_t}',
#     laVali_cll=lambda x: x in tValiV_t))
# tValiV_t = ('Y', 'N')
# tRes_l = list(teInPWTypedWVali_fif(f' Ts 2 times',
#     laInPValues_co=2, laInPTypeFlt_cll=None, laDfV_s='Y',
#     laAcceptEmptyInPAsDf_b=True, laValiInPMsg_s=f'a character OneOf{tValiV_t}',
#     laVali_cll=lambda _s: _s.upper() in tValiV_t))
# tRes_l.sort()
# print(tRes_l)

tTskMsg_s = '''
Задача 5. МОДУЛЬ 3 файл use_functions.py
В файле дано описание программы. Предлагается реализовать программу
 по описанию используя любые средства
'''
print(teSep_s, tTskMsg_s, f'{sys.version=}', teSep_s, 'Result:', '',  sep='\n')
"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
glAccSum_n, glHstT_l = 0, []

def tRefillAcc_f():
  global glAccSum_n, glHstT_l
  loAdd_n = teInPWTypedWVali_fif(f' Ведите сумму на сколько пополнить счет',
      laInPTypeFlt_cll=float, laDfV_s='100',
      laAcceptEmptyInPAsDf_b=True, laValiInPMsg_s=f'положительное число с возм.десят.точкой',
      laVali_cll=lambda _n: 0 <= _n)[0]
  glAccSum_n += loAdd_n #DVL: input by teInPWTypedWVali_fif
  # print(f'DBG: На счету:({glAccSum_n:.2f}) и в истории покупок {len(glHstT_l)} зап.')
  return True

def tBuy_f():
  global glAccSum_n, glHstT_l
  loCost_n = teInPWTypedWVali_fif(f' Введите сумму покупки (на Вашем счету:{glAccSum_n:.2f})',
      laInPTypeFlt_cll=float, laDfV_s=str(min(100, glAccSum_n)),
      laAcceptEmptyInPAsDf_b=True, laValiInPMsg_s=f'положительное число с возм.десят.точкой',
      laVali_cll=lambda _n: 0 <= _n)[0]

  if glAccSum_n < loCost_n: #DVL: input by teInPWTypedWVali_fif
    print(f'Денег на Вашем счету:({glAccSum_n:.2f}) не хватает',
        f'для покупки на сумму:({loCost_n:.2f}).',
        'Пополните счет, пожалуйста.', sep='\n')
    return False
  
  loDesc_s = teInPWTypedWVali_fif(f' Введите название покупки', laInPTypeFlt_cll=None,
      laDfV_s="Еда", laAcceptEmptyInPAsDf_b=True)[0]
  
  # print(f'DBG: На счету:({glAccSum_n}) и в истории покупок {len(glHstT_l)} зап.')
  glAccSum_n -= loCost_n
  glHstT_l.append((loDesc_s, loCost_n)) #DVL: input by teInPWTypedWVali_fif
  # print(f'DBG: На счету:({glAccSum_n}) и в истории покупок {len(glHstT_l)} зап.')
  return True

def tVieHst_f():
  global glAccSum_n, glHstT_l
  print('', f'История покупок (всего {len(glHstT_l)} зап.):',
      *enumerate(glHstT_l, 1), '', sep='\n')

tMenu_d = {'1':('Пополнение счета', tRefillAcc_f),
    '2':('Покупка', tBuy_f),
    '3':('История покупок', tVieHst_f),
    '4':('Выход', None)}

while True:
    print(*(f'{_k}. {_v[0]}' for _k, _v in tMenu_d.items()), sep='\n')
    print(f'На счету:({glAccSum_n:.2f}) и в истории покупок {len(glHstT_l)} зап.')

    li_s = input('Выберите пункт меню: ')
    if li_s in tMenu_d:
      lo_cll = tMenu_d[li_s][1]
      if lo_cll is None: break
      else: loRes_b = lo_cll()
    else:
        print(f'Неверный пункт меню:"{li_s}"')

print(teSep_s)
