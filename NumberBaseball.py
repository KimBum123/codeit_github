#깃허브 공부!!

import random
from tkinter import *
import tkinter.messagebox as msgbox

window = Tk()
window.title("숫자야구 게임")

def manual():
    msgbox.showinfo("설명서", """
    <숫자야구게임>

랜덤으로 각 자리 숫자가 겹치지 않은 세자리 수를 생성합니다.
사용자가 숫자를 입력했을때 생성된 숫자와
자리와 숫자가 모두 같으면 Strike
자리는 다르지만 숫자가 맞다면 Ball
자리와 숫자 모두 다르다면 Out입니다

입력한 숫자가 정답보다 큰지 작은지
Up, Down 으로 알려줍니다

예시) 정답: 123  사용자입력: 324

1 Strike 1 Ball 1 Out.  //  Down

""")

try_count = 1
randnum = []

def gameStart():
    game_window = Toplevel(window)

    titleLabel = Label(game_window, text="숫자를 맞춰보세요!", font=("bold", 20))
    titleLabel.pack()

    guessField = Entry(game_window)
    guessField.pack(side="left")

    global randnum
    randnum= []
    while len(randnum) < 3:
        num = random.randint(1, 9)
        if num not in randnum:
            randnum.append(num)

    #answer = Label(game_window, text=randnum)
    #answer.pack()

    def guessing():
        user_input = str(guessField.get())
        global try_count
        s_count = 0
        b_count = 0
        o_count = 0

        for i in range(0, 3):
            for j in range(0, 3):
                if (user_input[i] == str(randnum[j]) and i == j):
                    s_count += 1

                elif (user_input[i] == str(randnum[j]) and i != j):
                    b_count += 1
        o_count = 3 - (s_count + b_count)

        hint_playernum = [int(i) for i in user_input]
        hint_randnum = [int(i) for i in randnum]

        if (s_count != 3 and hint_playernum > hint_randnum):
            msgbox.showinfo("결과", "%d 스트라이크\n%d 볼\n%d 아웃\nDown!" % (s_count, b_count, o_count))

        elif (s_count != 3 and hint_playernum < hint_randnum):
            msgbox.showinfo("결과", "%d 스트라이크\n%d 볼\n%d 아웃\nUp!" % (s_count, b_count, o_count))

        elif (s_count == 3):
            msgbox.showinfo("결과", "정답입니다!\n시도횟수: %d" % (try_count))

        try_count += 1

    def reset():
        global randnum
        randnum = []
        while len(randnum) < 3:
            num = random.randint(1, 9)
            if num not in randnum:
                randnum.append(num)

        global try_count
        try_count = 1

        #answer["text"] = randnum

    reset_button = Button(game_window,command = reset, text="재시작", font=("bold", 20))
    reset_button.pack(side='right')

    try_button = Button(game_window, command=guessing, text="입력", font=("bold", 20))
    try_button.pack(side='right')


title = Label(window, text="숫자야구 게임에 오신걸 환영합니다!", font=("bold", 20))
title.pack(side=TOP)
b1 = Button(window, command=manual, text="게임 설명서", font=("bold", 25))
b1.pack(fill=X)
b2 = Button(window, command=gameStart, text="게임 시작!", font=("bold", 25))
b2.pack(fill=X)

window.mainloop()