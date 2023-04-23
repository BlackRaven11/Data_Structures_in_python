def open_Russian_Doll(doll):
  if doll == 1:
    print('doll = 1 --> All Dolls are opened!')
  else:
      print('doll = ' , doll)
      open_Russian_Doll(doll-1)
      
open_Russian_Doll(4)
        