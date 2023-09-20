import tkinter as tk
from ludo_game import LudoGame

def main():
    root = tk.Tk()
    app = LudoGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()