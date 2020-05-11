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
    def extract_en2sp(n, r):
        while n < r:
            next(dicc)
            n = n + 1
        for line in dicc:
            print(line[1])
            break

    def extract_en2ch(n = 0, r = 0):
        while n < r:
            next(dicc)
            n = n + 1
        for line in dicc:
            print(line[2])
            break
        
    def en2sp():
        user_word = input('enter word: ')
        if user_word == 'bathroom':
            extract_en2sp(0,1)
        elif user_word == 'rent':
            extract_en2sp(0,2)
        elif user_word == 'sound':
            extract_en2sp(0,3)
        elif user_word == 'chocolate':
            extract_en2sp(0,4)
        elif user_word == 'candy':
            extract_en2sp(0,5)

    def en2ch():
        user_word = input('enter word: ')
        if user_word == 'bathroom':
            extract_en2ch(0,1)
        elif user_word == 'rent':
            extract_en2ch(0,2)
        elif user_word == 'sound':
            extract_en2ch(0,3)
        elif user_word == 'chocolate':
            extract_en2ch(0,4)
        elif user_word == 'candy':
            extract_en2ch(0,5)

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
