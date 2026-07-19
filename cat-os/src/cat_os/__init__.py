import time
import subprocess

def meow():
    print("Meow")
    time.sleep(1.5)
    print("Meow")

def nerd():
    print("Meow")
    time.sleep(1)
    print("My name is Luna!")
    time.sleep(3)
    print("I can help you with math.")
    time.sleep(3)
    print("Type +, -, *, or /")

    pmtdnc = input("Q: ")

    if pmtdnc in ['+', '-', '*', '/']:
        try:
            e, f = map(float, input("(Separate the numbers by a space) Q: ").split())

            if pmtdnc == '+':
                print(f"{e} + {f} = {e + f}")
            elif pmtdnc == '-':
                print(f"{e} - {f} = {e - f}")
            elif pmtdnc == '*':
                print(f"{e} * {f} = {e * f}")
            elif pmtdnc == '/':
                if f != 0:
                    print(f"{e} / {f} = {e / f}")
                else:
                    print("Error: Cannot divide by zero.")

        except ValueError:
            print("Error: Please enter two valid numbers separated by a space.")
def story(luna):
    print("Which one?\n cat or BFF")
    sc = input("Q: ")
    if sc == "cat":
        from pathlib import Path
        import tkinter as tk
        from PIL import Image, ImageTk

        root = tk.Tk()

        img_path = Path(__file__).parent / "8939a.jpeg"

        image = Image.open(img_path)
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(root, image=photo)
        label.image = photo
        label.pack()
        print("hi!")
        time.sleep(3)
        print("It's me luna!")
        time.sleep(3)
        print("i can help with anything like\nmath or i can talk to like right now!")
        time.sleep(7)
        print("and here me in a jpeg")
        time.sleep(3)
        root.after(3000, root.destroy)  # Closes after 3 seconds
        root.mainloop()
        print("now bye!")
        time.sleep(3)
        print("Meow!")
    elif sc == "BFF":
        print("i have a BFF it you!")
        time.sleep(3)
        print("Meow!")
def playA(cat):
    from pathlib import Path
    import tkinter as tk
    from PIL import Image, ImageTk

    root = tk.Tk()

    img_path = Path(__file__).parent / "8939a.jpeg"

    image = Image.open(img_path)
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack()
    print("hi!")
    time.sleep(3)
    print("It's me luna!")
    time.sleep(3)
    print("i can help with anything like\nmath or i can talk to like right now!")
    time.sleep(7)
    print("and here me in a jpeg")
    time.sleep(3)
    root.after(3000, root.destroy)  # Closes after 3 seconds
    root.mainloop()
    print("now bye!")
    time.sleep(3)
    print("Meow!")
def playB(BFF):
    print("i have a BFF it you!")
    time.sleep(3)
    print("Meow!")
def play(vid):
    import tkinter as tk
    import vlc
    from pathlib import Path

    root = tk.Tk()
    root.title("Luna")
    root.geometry("800x600")

    video_path = Path(__file__).parent / "9220a.mp4"

    # Quiet VLC instance
    instance = vlc.Instance("--quiet")

    player = instance.media_player_new()
    media = instance.media_new(str(video_path))

    player.set_media(media)

    root.update()
    player.set_xwindow(root.winfo_id())  # Linux/Raspberry Pi

    player.play()
    print("look it me!")
    time.sleep(2)
    print("the orange cat!\nand my other BFF")

    root.mainloop()