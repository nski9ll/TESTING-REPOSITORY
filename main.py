dictionary = {'LOL':' odpowiedź na coś zabawnego',
              'CRINGE':'coś dziwnego lub wstydliwego',
              'ROFL':'odpowiedź na żart',
              'SHEESH':'lekka dezaprobata',
              'CREEPY':'straszny, złowieszczy',
              'AGGRO':'stać się agresywnym/zły'
}
word='sxjksdfojksdf'
while word != 'STOP':
    word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!), Wpisz STOP jeżeli chcesz zakonczyć program: ")
    if word in dictionary.keys():
        print(dictionary[word])
    else:
        print('Nie mamy jeszcze takiego słowa.. Ale wkrótce dodamy go!')
