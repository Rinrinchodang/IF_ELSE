amt=int(input("enter the amount"))                      
note=note_2000=note_500=note_200=note_100=note50=note_20=0
if amt>=2000:
    note_2000=amt//2000
    amt=amt-note_2000*2000
    print("2000\t=\t",note_2000)
if amt>=500:
    note_500=amt//500
    amt=amt-note_500*500
    print("500\t=\t",note_500)
if amt>=200:
    note_200=amt//200
    amt=amt-note_200*200
    print("200\t=\t",note_200)
if amt>=100:
    Note_100=amt//100
    amt=amt-note_100*100
    print("100\t=\t",note_100)
if amt>=20:
    note_20=amt//20
    amt=amt-note_20*20
    print("20\t=\t",note_20)
else:
    print("invalid")