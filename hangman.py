import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
import random

# создание окна, названия и добавление иконки приложения
key = tk.Tk()
key.title('Hangman')
key.iconbitmap("png-transparent-drawing-hanging-rope-noose-rope-pencil-technic-monochrome.ico")

# функция для отображения правил игры
def info():
    showinfo(title='Rules of the game', message='The game makes a word and the screen displays as many underscores as there are letters in the word. The player needs to enter letters to guess the word. If the letter is in the word, then it fits into its place on the screen (if there are several such letters, then all fit), and if not, then the picture of the gallows is replenished with a new element. If a player does not have time to guess the word before the gallows is drawn completely, then he is considered "hanged".')

# функция для нажатия на кнопки
def press(num):
    global exp
    exp = str(num)
    equation.set(exp)

# функция для очистки
def clear():
    global exp
    exp = " "
    equation.set(exp)

# создаем картинку с висилицей
img = tk.PhotoImage(file='1small.png')
picture = tk.Label(image=img)
picture.grid(row=0, column=0, rowspan=50, columnspan=9)
place = tk.Label(background='#293a26', foreground='#293a26', text='.')
place.grid(row=1, column=9)
space = tk.Label(background='#293a26', font=("Courier", 44), foreground='white', text='')
space.grid(row=15, column=11, columnspan=10)

# создаем поле для ввода буквы
equation = tk.StringVar()
Dis_entry = ttk.Entry(key, width=15, justify='center', state= 'readonly', textvariable = equation)
Dis_entry.grid(row = 40, column = 14, columnspan = 3, ipadx = 10 , ipady = 10)
begin = False

# функция для начала игры
def start():
    global picture
    global main
    global count
    global list_of_guessed
    global letters_list
    global begin
    begin = True
    picture.destroy()
    img = tk.PhotoImage(file='1small.png')
    picture = tk.Label(image=img)
    picture.grid(row=0, column=0, rowspan=50, columnspan=9)
    words_to_guess = [
        'MONKEY', 'GARAGE', 'CARROT', 'APPLE', 'SPACE', 'PURPLE', 'BRICK', 'JUNE', 'KEY', 'CLOCK', 'BONE', 'MOTHER', 'WORLD', 'PART', 'FATHER', 'ANIMAL', 'ROUND', 'CASTLE', 'THING', 'CAT', 'CRAFT', 'NUMBER', 'FOOD', 'SHOW', 'SHOP', 'STORY', 'ROOM', 'PANDA', 'RIVER', 'STONE', 'MOON', 'REASON', 'WOMAN', 'SAND', 'TRUTH', 'PIE', 'HEART', 'FISH', 'BUTTON', 'RACE', 'TRIP', 'STORM', 'TOPIC', 'TREE', 'SKILL', 'MATH', 'MUSIC', 'PERSON', 'FILE', 'WORD', 'CATCH', 'DINNER', 'MONEY', 'LIFE', 'BOSS', 'OPTION', 'COAST', 'HORSE', 'PAUSE', 'HOPE', 'MODEL', 'MONTH', 'BEACH', 'GUITAR', 'SKIN', 'BOY', 'GARDEN', 'SYSTEM', 'UNCLE', 'EGG', 'KIND', 'SALT', 'PLACE', 'MARKET', 'WORTH', 'ROBBER', 'KILLER', 'KNIFE', 'THEORY', 'PINK', 'PLANT', 'MAGIC', 'PILLOW', 'SOFA', 'BED', 'LAMP', 'FLOWER', 'LEMON', 'BERRY', 'SUBWAY'
    ]
    word = random.choice(words_to_guess)
    n = len(word)
    screen = n * '_ '
    space.config(text=screen)
    main = word
    count = 0
    list_of_guessed = []
    letters_list = list(word)
    picture.mainloop()

# функция с процессом игры
def hangman(word):
    global picture
    global count
    global list_of_guessed
    global letters_list
    global begin
    new_screen = ''
    list_of_guessed.append(guess)
    victory = False
    for letter in word:
        if letter in list_of_guessed:
            if letter in letters_list:
                letters_list.remove(letter)
            if len(letters_list) == 0:
                victory = True
        else:
            break
    if not victory:
        if guess in word:
                for i in word:
                    if guess == i:
                        new_screen += i + ' '
                    else:
                        if i in list_of_guessed:
                            new_screen += i + ' '
                        else:
                            new_screen += '_ '
                space.config(text=new_screen)
        else:
            count += 1
            if count == 1:
                pic = '2small.png'
            if count == 2:
                pic = '3small.png'
            if count == 3:
                pic = '4small.png'
            if count == 4:
                pic = '5small.png'
            if count == 5:
                pic = '6small.png'
            if count == 6:
                pic = '7small.png'
            if count == 7:
                pic = '8small.png'
            if count == 8:
                pic = '9small.png'
            picture.destroy()
            img = tk.PhotoImage(file=pic)
            picture = tk.Label(image=img)
            picture.grid(row=0, column=0, rowspan=50, columnspan=9)
            if count == 8:
                showinfo(title='Loss', message=f'Unfortunatelly, you have been hanged. The word was {word}.')
                start()
                return 0
    else:
        if guess in word:
            for i in word:
                if guess == i:
                    new_screen += i + ' '
                else:
                    if i in list_of_guessed:
                        new_screen += i + ' '
            space.config(text=new_screen)
        showinfo(title='Victory!', message='Congratulations, you have guessed the word!')
        begin = False
    picture.mainloop()

# функция для кнопки Enter
def action():
    global exp
    global main
    global guess
    global list_of_guessed
    global begin
    if begin:
        if Dis_entry.get() in list_of_guessed:
            showerror(title='Do not repeat!', message='You have chosen this letter')
            return 0
        else:
            guess = Dis_entry.get()
        exp = " put another guess "
        equation.set(exp)
        hangman(main)
    else:
        showerror(title='Error!', message='You have to start the new game.')

# задаем параметры окна
key.geometry('1100x505')
key.configure(bg = '#293a26')

# создаем меню
mainmenu = tk.Menu(key)
key.config(menu=mainmenu)

filemenu = tk.Menu(mainmenu, activebackground='#5a714a', activeborderwidth=10, background='#293a26', bd=10, font=("Courier", 15), tearoff=0)
filemenu.add_command(label="New game", command=start)
filemenu.add_command(label="About", command=info)
filemenu.add_command(label="Exit", command=exit)

mainmenu.add_cascade(label="Menu", menu=filemenu)

# переменная для отображения данных на экране
exp = " "

# первая линия кнопок

q = ttk.Button(key,text = 'Q' , width = 6, command = lambda : press('Q'))
q.grid(row = 42, column = 10, ipadx = 6 , ipady = 10)

w = ttk.Button(key,text = 'W' , width = 6, command = lambda : press('W'))
w.grid(row = 42, column = 11, ipadx = 6 , ipady = 10)

E = ttk.Button(key,text = 'E', width = 6, command = lambda : press('E'))
E.grid(row = 42, column = 12, ipadx = 6 , ipady = 10)

R = ttk.Button(key,text = 'R' , width = 6, command = lambda : press('R'))
R.grid(row = 42, column = 13, ipadx = 6 , ipady = 10)

T = ttk.Button(key,text = 'T' , width = 6, command = lambda : press('T'))
T.grid(row = 42, column = 14, ipadx = 6 , ipady = 10)

Y = ttk.Button(key,text = 'Y' , width = 6, command = lambda : press('Y'))
Y.grid(row = 42, column = 15, ipadx = 6 , ipady = 10)

U = ttk.Button(key,text = 'U' , width = 6, command = lambda : press('U'))
U.grid(row = 42, column = 16, ipadx = 6 , ipady = 10)

I = ttk.Button(key,text = 'I' , width = 6, command = lambda : press('I'))
I.grid(row = 42, column = 17, ipadx = 6 , ipady = 10)

O = ttk.Button(key,text = 'O' , width = 6, command = lambda : press('O'))
O.grid(row = 42, column = 18, ipadx = 6 , ipady = 10)

P = ttk.Button(key,text = 'P' , width = 6, command = lambda : press('P'))
P.grid(row = 42, column = 19, ipadx = 6 , ipady = 10)

# вторая линия кнопок

A = ttk.Button(key,text = 'A' , width = 6, command = lambda : press('A'))
A.grid(row = 43, column = 10, ipadx = 6 , ipady = 10)

S = ttk.Button(key,text = 'S' , width = 6, command = lambda : press('S'))
S.grid(row = 43, column = 11, ipadx = 6 , ipady = 10)

D = ttk.Button(key,text = 'D' , width = 6, command = lambda : press('D'))
D.grid(row = 43, column = 12, ipadx = 6 , ipady = 10)

F = ttk.Button(key,text = 'F' , width = 6, command = lambda : press('F'))
F.grid(row = 43, column = 13, ipadx = 6 , ipady = 10)

G = ttk.Button(key,text = 'G' , width = 6, command = lambda : press('G'))
G.grid(row = 43, column = 14, ipadx = 6 , ipady = 10)

H = ttk.Button(key,text = 'H' , width = 6, command = lambda : press('H'))
H.grid(row = 43, column = 15, ipadx = 6 , ipady = 10)

J = ttk.Button(key,text = 'J' , width = 6, command = lambda : press('J'))
J.grid(row = 43, column = 16, ipadx = 6 , ipady = 10)

K = ttk.Button(key,text = 'K' , width = 6, command = lambda : press('K'))
K.grid(row = 43, column = 17, ipadx = 6 , ipady = 10)

L = ttk.Button(key,text = 'L' , width = 6, command = lambda : press('L'))
L.grid(row = 43, column = 18, ipadx = 6 , ipady = 10)

enter = ttk.Button(key,text = 'Enter' , width = 6, command = action)
enter.grid(row = 43, column = 19, ipadx = 6 , ipady = 10)

# третья линия кнопок

Z = ttk.Button(key,text = 'Z' , width = 6, command = lambda : press('Z'))
Z.grid(row = 44, column = 11, ipadx = 6 , ipady = 10)

X = ttk.Button(key,text = 'X' , width = 6, command = lambda : press('X'))
X.grid(row = 44, column = 12, ipadx = 6 , ipady = 10)

C = ttk.Button(key,text = 'C' , width = 6, command = lambda : press('C'))
C.grid(row = 44, column = 13, ipadx = 6 , ipady = 10)

V = ttk.Button(key,text = 'V' , width = 6, command = lambda : press('V'))
V.grid(row = 44, column = 14, ipadx = 6 , ipady = 10)

B = ttk.Button(key, text= 'B' , width = 6 , command = lambda : press('B'))
B.grid(row = 44, column = 15 , ipadx = 6 ,ipady = 10)

N = ttk.Button(key,text = 'N' , width = 6, command = lambda : press('N'))
N.grid(row = 44, column = 16, ipadx = 6 , ipady = 10)

M = ttk.Button(key,text = 'M' , width = 6, command = lambda : press('M'))
M.grid(row = 44, column = 17, ipadx = 6 , ipady = 10)

clear = ttk.Button(key, text = 'Clear' , width = 6, command = clear)
clear.grid(row = 44, column = 18, ipadx = 6 , ipady = 10)

key.mainloop()