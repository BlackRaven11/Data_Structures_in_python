def open_russian_doll(doll):
  if doll == 1:
    print('doll = 1 --> All Dolls are opened!')
  else:
    print('doll = ' , doll , ' opened!')
    open_russian_doll(doll-1)
    
myDoll = int(input('Enter the number of Dolls: '))      
open_russian_doll(myDoll)
        