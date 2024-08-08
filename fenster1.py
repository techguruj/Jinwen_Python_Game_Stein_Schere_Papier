import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
from tkinter import ttk
import json
from collections import OrderedDict

class App:
    """
    Die App-Klasse repräsentiert das Erstanwendungsfenster.
    """

    def __init__(self, root, user_name):
        """
        Initialisiert die App mit einem Root-Fenster und einem Benutzernamen.

        Parameter:
        root (Tk): Das Root-Fenster.
        user_name (str): Der Name des Benutzers.
        """
        self.root = root
        self.user_name = user_name
        self.user_name[0] = ""

        self.ready = False
        # Titel einstellen
        root.title("Stein Papier Schere")
        # Fenstergröße einstellen
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Laden und Anzeigen des Bildes
        self.photo = Image.open('./pic/fight.jpg')
        self.photo = ImageTk.PhotoImage(self.photo)
        GLabel_723 = tk.Label(root, image=self.photo)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_723["font"] = ft
        GLabel_723["fg"] = "#333333"
        GLabel_723["justify"] = "center"
        GLabel_723["text"] = "bilder:stein papier schere"
        GLabel_723.place(x=0, y=140, width=603, height=359)

        # Laden der Highscores aus einer JSON-Datei
        with open('highScore.json') as json_file:
            self.score = json.load(json_file)
            self.sorted_score = OrderedDict(sorted(self.score.items(), key=lambda x: x[1], reverse=True))

        # Anzeigen der Top 3 Highscores
        GMessage_130 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_130["font"] = ft
        GMessage_130["fg"] = "#333333"
        GMessage_130["justify"] = "left"
        GMessage_130["text"] = "Top3:\n" + "1. " + list(self.sorted_score.keys())[0] + "\t\t" + str(
            list(self.sorted_score.values())[0]) + "\n" + "2. " + list(self.sorted_score.keys())[1] + "\t" + str(
            list(self.sorted_score.values())[1]) + "\n" + "3. " + list(self.sorted_score.keys())[2] + "\t\t" + str(
            list(self.sorted_score.values())[2])
        GMessage_130.place(x=400, y=10, width=175, height=120)

        # Anzeigen eines Labels, in dem der Benutzer seinen Namen aussprechen soll
        self.G_label_750 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.G_label_750["font"] = ft
        self.G_label_750["fg"] = "#333333"
        self.G_label_750["justify"] = "center"
        self.G_label_750["text"] = "Sprechen Sie Ihre Name"
        self.G_label_750.place(x=20, y=30, width=175, height=94)

        # Erstellen einer Schaltfläche, mit der der Benutzer die Anweisungen bestätigen kann
        GButton_768 = tk.Button(root)
        GButton_768["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_768["font"] = ft
        GButton_768["fg"] = "#000000"
        GButton_768["justify"] = "center"
        GButton_768["text"] = "Auskennen"
        GButton_768.place(x=230, y=30, width=108, height=30)
        GButton_768["command"] = self.GButton_768_command

        # Erstellen einer Schaltfläche, mit der der Benutzer das Spiel starten kann
        GButton_789 = tk.Button(root)
        GButton_789["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_789["font"] = ft
        GButton_789["fg"] = "#000000"
        GButton_789["justify"] = "center"
        GButton_789["text"] = "OK, Staten"
        GButton_789.place(x=230, y=90, width=109, height=30)
        GButton_789["command"] = self.GButton_789_command

        # Protokoll für das Schließen des Fensters festlegen
        root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        """
        Behandelt das Ereignis, wenn das Fenster geschlossen wird.
        """
        exit()

    def GButton_768_command(self):
        """
        Behandelt das Ereignis, wenn die Schaltfläche "Auskennen" angeklickt wird.
        """
        import googleRecognition
        self.user_name[0] = googleRecognition.holeText()
        self.G_label_750.config(text=self.user_name[0])

        if self.user_name[0] == "Google could not understand":
            self.ready = False
        elif self.user_name[0] in self.score.keys():
            self.G_label_750.config(text=self.user_name[0]+" bereits vorhanden, Andere Name bitte")
            self.ready = False
        else:
            self.ready = True

    def GButton_789_command(self):
        """
        Behandelt das Ereignis, wenn die Schaltfläche "OK, Staten" angeklickt wird.
        """
        if self.ready:
            self.root.destroy()