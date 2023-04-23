def open_russian_doll(doll):
  if doll == 1:
    print('doll = 1 --> All Dolls are opened!')
  else:
    print('doll = ' , doll)
    open_russian_doll(doll-1)
      
open_russian_doll(4)
        