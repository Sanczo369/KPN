from tkinter import *
from PIL import ImageTk, Image
def main():
    root=Tk()
    root.title('GRA "PAPIER, KAMIEŃ, NOŻYCZKI"')
    root.iconbitmap("logo.ico")
    root.geometry("641x522")
    img1=ImageTk.PhotoImage(Image.open("papier.jpg"))
    img2=ImageTk.PhotoImage(Image.open("kamien.jpg"))
    img3=ImageTk.PhotoImage(Image.open("nozyczki.jpg"))

    #  element
    tilte_label=Label(root, text='GRA "PAPIER, KAMIEŃ, NOŻYCZKI"', font=("Comic Sans MS", 20, "bold"))
    choose_label=Label(root,text="PROSZĘ, WYBIERZ:",font=("Arial", 10))
    frame= LabelFrame(root, pady=10, padx=10)
    pick1=Button(frame, image=img1)
    pick2=Button(frame, image=img2)
    pick3=Button(frame, image=img3)

    tilte_label.grid(row=0, columnspan=2, sticky=N)
    choose_label.grid(row=1, columnspan=2)
    frame.grid(row=2,columnspan=2)
    pick1.grid(row=1, column=1)
    pick2.grid(row=1, column=2)
    pick3.grid(row=1, column=3)

    # play button
    play_btn = Button(frame, text="PLAY", font=("Arial", 20, "bold"), borderwidth=2, relief="solid", padx=100, pady=5)
    play_btn.grid(row=3, columnspan=4,pady=20)

    # score element
    score = LabelFrame(root, text="AKTUALNE WYNIKI", pady=10, padx=10)
    game_label = Label(score, text="liczba gier:")
    win_label = Label(score, text="wygranych:")
    lose_label = Label(score, text="przegranych:")
    draw_label = Label(score, text="remisów:")
    # score element position
    score.grid(row=4, column=1, sticky=E)
    game_label.grid(row=0, column=0, sticky=W)
    win_label.grid(row=1, column=0, sticky=W)
    lose_label.grid(row=2, column=0, sticky=W)
    draw_label.grid(row=3, column=0, sticky=W)

    # game result element
    result = LabelFrame(root, text="WYNIKI GRY", pady=10, padx=190)
    player_pick_label = Label(result, text="Twój wybór:")
    ai_pick_label = Label(result, text="Wybór komputera:")
    winer_label = Label(result, text="Zwycięzca gry:",font=("Arial",15))
    # game result position
    result.grid(row=4, column=0, sticky=W)
    player_pick_label.grid(row=0, column=0)
    ai_pick_label.grid(row=1, column=0)
    winer_label.grid(row=2, column=0)





    root.mainloop()
if __name__ == '__main__':
    main()