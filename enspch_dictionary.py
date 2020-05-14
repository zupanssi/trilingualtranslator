import csv
'''
english,spanish,chinese
bathroom,baño,廁所
rent,alquilar,租
sound,sonido,聲音
chocolate,chocolate,巧克力
candy,golosina,糖果
'''
with open('enspch_dic.csv','r') as ite:
    dicc = csv.reader(ite)
    rowList = list(dicc)
        
    def en2sp():
        user_word = input('enter word: ')
        if user_word == rowList[1][0]:
            print(rowList[1][1])
        if user_word == rowList[2][0]:
            print(rowList[2][1])
        if user_word == rowList[3][0]:
            print(rowList[3][1])
        if user_word == rowList[4][0]:
            print(rowList[4][1])
        if user_word == rowList[5][0]:
            print(rowList[5][1])

    def en2ch():
        user_word = input('enter word: ')
        if user_word == rowList[1][0]:
            print(rowList[1][2])
        if user_word == rowList[2][0]:
            print(rowList[2][2])
        if user_word == rowList[3][0]:
            print(rowList[3][2])
        if user_word == rowList[4][0]:
            print(rowList[4][2])
        if user_word == rowList[5][0]:
            print(rowList[5][2])

    mode = input(
        '''
select translation mode:
1.english ->spanish
2.english -> chinese
'''
)

    if mode == '1':
        en2sp()
    elif mode == '2':
        en2ch()
