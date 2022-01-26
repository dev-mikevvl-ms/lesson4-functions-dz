# Mod:MVVlStd.py
teSep_s = '_' *80

def teInPWTypedWVali_fif(laWhatInPMsg_s, laInPValues_co=1, laValiInPMsg_s='',
    laVali_cll=None, laInPType_cll=int, laMaxInPTry_co=11) -> tuple:
  if laInPValues_co < 1: raise ValueError(f'laInPValues_co must be > 0, now:{laInPValues_co}')
  loTypeAValiFlsCo_l, loRes_l, loMaxTry_co = [0, 0], [], int(max(laInPValues_co, laMaxInPTry_co))
  if laValiInPMsg_s and laVali_cll:
    lo_s = f' - your value will be validated as({laValiInPMsg_s}) -'
  else: lo_s = ''
  loInPMsg_s = f"Please, Input{laWhatInPMsg_s}{lo_s} and press Enter: "
  for l_co in range(loMaxTry_co):
    li_s = input(loInPMsg_s)
    try:
      if laInPType_cll is not None:
        liChe_i = laInPType_cll(li_s)
      else: liChe_i = li_s
    except ValueError as leExc_o:
      loTypeAValiFlsCo_l[0] +=1; liChe_i = None
      print(f"\tERR: You input:'{li_s}' NOT pass check type w/func({laInPType_cll}",
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
# print(teInPWTypedWVali_fif(laInPValues_co=2, laInPType_cll=float, laMaxInPTry_co=1),
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
# tCndInPMsg_s = f' (по очереди по одной вводите любые цифры) a Integer OneOf{tValiV_t}'
# tRes_l = list(teInPWTypedWVali_fif(f' по очереди по одной любые цифры {tResLLen_co} раза',
#     laInPValues_co=tResLLen_co, laValiInPMsg_s=f'a Integer OneOf{tValiV_t}',
#     laVali_cll=lambda x: x in tValiV_t))
# tRes_l.sort()
# print(tRes_l)
