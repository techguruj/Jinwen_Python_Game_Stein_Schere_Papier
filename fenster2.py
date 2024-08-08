import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import time

"""
Die App-Klasse repräsentiert das Zweitanwendungsfenster.
"""
class App:
    """
    Die App-Klasse repräsentiert das Zweitanwendungsfenster.
    """
    def __init__(self, root, user_name):
        """Initialisiert die App mit dem gegebenen root und Benutzernamen.

        Parameter:
            root (root): Das Hauptfenster der Anwendung.
            user_name (str): Der Name des Benutzers.
        """

        # Initialisierung der Variablen
        self.root = root
        self.ichWahl = 2
        self.tonyWahl = 0
        self.ichPunkte = 0
        self.tonyPunkte = 0
        self.rundMode = 1
        self.user_name = user_name
        # setting title
        root.title("Stein Papier Schere")
        # setting window size
        width = 600
        height = 400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        #Label für die Punkte
        self.GLabel_549 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_549["font"] = ft
        self.GLabel_549["fg"] = "#333333"
        self.GLabel_549["justify"] = "left"
        self.GLabel_549["text"] = user_name[0] + " : " + str(self.ichPunkte)
        self.GLabel_549.place(x=20, y=60, width=95, height=35)

        #Label für die Punkte
        self.GLabel_148 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_148["font"] = ft
        self.GLabel_148["fg"] = "#333333"
        self.GLabel_148["justify"] = "left"
        self.GLabel_148["text"] = "Tony : " + str(self.tonyPunkte)
        self.GLabel_148.place(x=480, y=60, width=95, height=35)

        #RadioButtons für die Auswahl des Spielmodus
        self.radioVar = tk.IntVar()
        self.GRadio_982 = tk.Radiobutton(root, variable=self.radioVar)
        ft = tkFont.Font(family='Times', size=10)
        self.GRadio_982["font"] = ft
        self.GRadio_982["fg"] = "#333333"
        self.GRadio_982["justify"] = "left"
        self.GRadio_982["text"] = "Manuell        "
        self.GRadio_982.place(x=430,y=0,width=135,height=30)
        self.GRadio_982["value"] = 1
        self.GRadio_982["command"] = self.GRadio_982_command
        self.GRadio_982.select()

        #RadioButtons für die Auswahl des Spielmodus
        self.GRadio_700 = tk.Radiobutton(root, variable=self.radioVar)
        ft = tkFont.Font(family='Times', size=10)
        self.GRadio_700["font"] = ft
        self.GRadio_700["fg"] = "#333333"
        self.GRadio_700["justify"] = "left"
        self.GRadio_700["text"] = "Voice Control"
        self.GRadio_700.place(x=430,y=30,width=138,height=30)
        self.GRadio_700["value"] = 0
        self.GRadio_700["command"] = self.GRadio_700_command

        #Bild für mich
        self.photo1 = Image.open('./pic/bund.jpg')
        self.photo1 = ImageTk.PhotoImage(self.photo1)
        self.GLabel_598 = tk.Label(root, image=self.photo1)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_598["font"] = ft
        self.GLabel_598["fg"] = "#333333"
        self.GLabel_598["justify"] = "center"
        self.GLabel_598["text"] = "label1"
        self.GLabel_598.place(x=10, y=100, width=100, height=100)

        #Bild für die Auswahl
        self.photo3 = Image.open('./pic/x.jpg')
        self.photo3 = ImageTk.PhotoImage(self.photo3)
        self.GLabel_945 = tk.Label(root, image=self.photo3)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_945["font"] = ft
        self.GLabel_945["fg"] = "#333333"
        self.GLabel_945["justify"] = "center"
        self.GLabel_945["text"] = "label_Tony_wahl"
        self.GLabel_945.place(x=330, y=100, width=100, height=100)

        #Button für die Auswahl
        self.GButton_965 = tk.Button(root)
        self.GButton_965["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        self.GButton_965["font"] = ft
        self.GButton_965["fg"] = "#000000"
        self.GButton_965["justify"] = "left"
        self.GButton_965["text"] = "Sprechen \noder\nSpielen"
        self.GButton_965.place(x=250, y=2, width=99, height=84)
        self.GButton_965["command"] = self.GButton_965_command

        #Bild für Tony Auswahl
        self.photo2 = Image.open('./pic/x.jpg')
        self.photo2 = ImageTk.PhotoImage(self.photo2)
        self.GLabel_793 = tk.Label(root, image=self.photo2)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_793["font"] = ft
        self.GLabel_793["fg"] = "#333333"
        self.GLabel_793["justify"] = "center"
        self.GLabel_793["text"] = "label_ich_wahl"
        self.GLabel_793.place(x=160, y=100, width=100, height=100)

        #Bild für Tony
        self.photo4 = Image.open('./pic/tony.jpg')
        self.photo4 = ImageTk.PhotoImage(self.photo4)
        self.GLabel_12 = tk.Label(root, image=self.photo4)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_12["font"] = ft
        self.GLabel_12["fg"] = "#333333"
        self.GLabel_12["justify"] = "center"
        self.GLabel_12["text"] = "label4"
        self.GLabel_12.place(x=490, y=100, width=100, height=100)

        #Nachrichtenfeld
        self.GMessage_421 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=15)
        self.GMessage_421["font"] = ft
        self.GMessage_421["fg"] = "#333333"
        self.GMessage_421["justify"] = "left"
        self.GMessage_421["text"] = "Bitte spechen Sie Stein, Schere oder Papier an Microfon"
        self.GMessage_421.place(x=0, y=210, width=602, height=180)

        #Checkbuttons für die manuelle Auswahl stein
        self.checkVar473 = tk.IntVar()
        self.GCheckBox_473=tk.Checkbutton(root, variable=self.checkVar473)
        ft = tkFont.Font(family='Times',size=10)
        self.GCheckBox_473["font"] = ft
        self.GCheckBox_473["fg"] = "#333333"
        self.GCheckBox_473["justify"] = "left"
        self.GCheckBox_473["text"] = "Stein   "
        self.GCheckBox_473.place(x=0,y=0,width=70,height=25)
        self.GCheckBox_473["offvalue"] = "0"
        self.GCheckBox_473["onvalue"] = "1"
        self.GCheckBox_473["command"] = self.GCheckBox_473_command
        self.GCheckBox_473.select()

        #Checkbuttons für die manuelle Auswahl Papier
        self.checkVar707 = tk.IntVar()
        self.GCheckBox_707=tk.Checkbutton(root, variable=self.checkVar707)
        ft = tkFont.Font(family='Times',size=10)
        self.GCheckBox_707["font"] = ft
        self.GCheckBox_707["fg"] = "#333333"
        self.GCheckBox_707["justify"] = "left"
        self.GCheckBox_707["text"] = "Papier "
        self.GCheckBox_707.place(x=0,y=20,width=70,height=25)
        self.GCheckBox_707["offvalue"] = "0"
        self.GCheckBox_707["onvalue"] = "1"
        self.GCheckBox_707["command"] = self.GCheckBox_707_command

        #Checkbuttons für die manuelle Auswahl Schere
        self.checkVar928 = tk.IntVar()
        self.GCheckBox_928=tk.Checkbutton(root, variable=self.checkVar928)
        ft = tkFont.Font(family='Times',size=10)
        self.GCheckBox_928["font"] = ft
        self.GCheckBox_928["fg"] = "#333333"
        self.GCheckBox_928["justify"] = "left"
        self.GCheckBox_928["text"] = "Schere"
        self.GCheckBox_928.place(x=0,y=40,width=70,height=25)
        self.GCheckBox_928["offvalue"] = "0"
        self.GCheckBox_928["onvalue"] = "1"
        self.GCheckBox_928["command"] = self.GCheckBox_928_command

        #Fenster schließen
        root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        """
        Diese Methode wird aufgerufen, wenn das Fenster geschlossen wird.
        Es zeigt eine Nachrichtenbox an, die den Benutzer fragt,
        ob er wirklich beenden und die Punkte hochladen möchte.
        Wenn der Benutzer zustimmt, wird die Methode hochladenScore aufgerufen und das Fenster wird zerstört.
        """
        import tkinter.messagebox as messagebox
        if messagebox.askokcancel("Exit und Punkt Hochladen", f' HI, {self.user_name[0]} Du hast {self.ichPunkte} gewonnen.\nWillst du wirklich beenden und die Punkte hochladen?'):
            self.hochladenScore()
            self.root.destroy()

    def hochladenScore(self):
        """
        Lädt die Punktzahl des Benutzers hoch.

        Diese Methode öffnet die 'highScore.json'-Datei und liest die aktuellen Punktzahlen ein.
        Anschließend wird die Punktzahl des aktuellen Benutzers aktualisiert und die geänderten Punktzahlen
        werden wieder in die 'highScore.json'-Datei geschrieben.
        """
        import json
        with open('highScore.json') as json_file:
            self.score = json.load(json_file)

        self.score[self.user_name[0]] = self.ichPunkte
        json.dump(self.score, open('highScore.json', 'w'))



    def GCheckBox_707_command(self):
        """
        Diese Methode wird aufgerufen, wenn das Kontrollkästchen GCheckBox_707 ausgewählt wird.
        Es wählt GCheckBox_707 aus und hebt die Auswahl von GCheckBox_473 und GCheckBox_928 auf.
        """
        self.GCheckBox_707.select()
        self.GCheckBox_473.deselect()
        self.GCheckBox_928.deselect()

    def GCheckBox_473_command(self):
        """
        Diese Methode wird aufgerufen, wenn das Kontrollkästchen GCheckBox_473 ausgewählt wird.
        Es wählt GCheckBox_473 aus und hebt die Auswahl von GCheckBox_707 und GCheckBox_928 auf.
        """
        self.GCheckBox_473.select()
        self.GCheckBox_707.deselect()
        self.GCheckBox_928.deselect()

    def GCheckBox_928_command(self):
        """
        Diese Methode wird aufgerufen, wenn das Kontrollkästchen GCheckBox_928 ausgewählt wird.
        Es wählt GCheckBox_928 aus und hebt die Auswahl von GCheckBox_707 und GCheckBox_473 auf.
        """
        self.GCheckBox_928.select()
        self.GCheckBox_707.deselect()
        self.GCheckBox_473.deselect()

    def GRadio_982_command(self):
        pass

    def GRadio_700_command(self):
        pass

    def Clear_alleWahl(self):
        """
        Setzt die Auswahlbilder zurück.

        Diese Methode wird aufgerufen, um die Auswahlbilder auf den Standardzustand zurückzusetzen.
        Es lädt das Bild 'x.jpg' und setzt es als Bild für GLabel_793 und GLabel_945.
        """
        self.foto2 = Image.open('./pic/x.jpg')
        self.photo2 = ImageTk.PhotoImage(self.foto2)
        self.GLabel_793["image"] = self.photo2
        self.foto3 = Image.open('./pic/x.jpg')
        self.photo3 = ImageTk.PhotoImage(self.foto3)
        self.GLabel_945["image"] = self.photo3

    def manuell_spielen(self):
        """
        Führt das manuelle Spiel aus.

        Diese Methode wird aufgerufen, um das manuelle Spiel zu starten.
        Es überprüft, welche Kontrollkästchen ausgewählt sind und setzt die entsprechenden Variablen und Bilder.
        Anschließend wird die Methode spielenLogic aufgerufen, um das Spiel zu starten.
        """
        self.Clear_alleWahl()
        if self.checkVar473.get() == 1:
            self.ichWahl = 1
            self.foto2 = Image.open('./pic/einstein.jpg')
        elif self.checkVar707.get() == 1:
            self.ichWahl = 3
            self.foto2 = Image.open('./pic/papier.jpg')
        elif self.checkVar928.get() == 1:
            self.ichWahl = 2
            self.foto2 = Image.open('./pic/schere.jpg')

        self.photo2 = ImageTk.PhotoImage(self.foto2)
        self.GLabel_793["image"] = self.photo2

        self.spielenLogic()




    def voice_spielen(self):
        """
        Führt das Spiel mit Sprachsteuerung aus.

        Diese Methode wird aufgerufen, um das Spiel mit Sprachsteuerung zu starten.
        Es verwendet die Google-Erkennung, um die Sprachauswahl des Benutzers zu erkennen und zu verarbeiten.
        Es überprüft, ob die Sprachauswahl gültig ist (Stein, Schere oder Papier) und setzt die entsprechenden Variablen und Bilder.
        Anschließend wird die Methode spielenLogic aufgerufen, um das Spiel zu starten.
        """
        self.GCheckBox_473.deselect()
        self.GCheckBox_707.deselect()
        self.GCheckBox_928.deselect()

        import googleRecognition

        self.Clear_alleWahl()
        self.voicetext = googleRecognition.holeText()

        self.GMessage_421["text"] = "dein Wahl:\n" + self.voicetext
        if self.voicetext == "Google could not understand": return
        if self.voicetext not in ["Stein", "Schere", "Papier"]:
            self.GMessage_421["text"] = "dein Wort:  " + self.voicetext + "\nist nicht gültig,bitte nur Stein, Schere oder Papier sprechen"
            return
        if self.voicetext == "Stein":
            self.ichWahl = 1
            self.foto2 = Image.open('./pic/einstein.jpg')
        elif self.voicetext == "Schere":
            self.ichWahl = 2
            self.foto2 = Image.open('./pic/schere.jpg')
        elif self.voicetext == "Papier":
            self.ichWahl = 3
            self.foto2 = Image.open('./pic/papier.jpg')

        self.photo2 = ImageTk.PhotoImage(self.foto2)
        self.GLabel_793["image"] = self.photo2

        self.GMessage_421["text"] = "dein Wahl:\n" + self.voicetext
        self.spielenLogic()

    def spielenLogic(self):
        """
        Führt die Spiellogik aus.

        Diese Methode wird aufgerufen, um die Spiellogik auszuführen.
        Es generiert eine zufällige Auswahl für Tony (Stein, Schere oder Papier) und vergleicht sie mit der Auswahl des Benutzers.
        Abhängig vom Ergebnis des Vergleichs werden die Punkte des Benutzers oder von Tony erhöht und die entsprechenden Nachrichten und Bilder aktualisiert.
        """
        import random
        self.GMessage_421["text"] = ""

        self.tonyWahl = random.randint(1, 3)

        if self.tonyWahl == 1:
            self.foto3 = Image.open('./pic/einstein.jpg')
        elif self.tonyWahl == 2:
            self.foto3 = Image.open('./pic/schere.jpg')
        elif self.tonyWahl == 3:
            self.foto3 = Image.open('./pic/papier.jpg')

        self.photo3 = ImageTk.PhotoImage(self.foto3)
        self.GLabel_945["image"] = self.photo3

        if self.ichWahl == self.tonyWahl:
            self.GMessage_421["text"] = "Unentschieden,nochmal"

        # Die folgenden Bedingungen überprüfen die verschiedenen Möglichkeiten des Spiels und aktualisieren die Punkte und Nachrichten entsprechend.
        elif self.ichWahl == 1 and self.tonyWahl == 2:  # Stein vs Schere
            self.ichPunkte += 1
            self.GLabel_549["text"] = "Ich : " + str(self.ichPunkte)
            self.GMessage_421["text"] = "Ich gewinne"
            self.GLabel_549["text"] = self.user_name[0] + " : " + str(self.ichPunkte)
            self.GLabel_148["text"] = "Tony : " + str(self.tonyPunkte)

        elif self.ichWahl == 1 and self.tonyWahl == 3:  # Stein vs Papier
            self.tonyPunkte += 1
            self.GLabel_148["text"] = "Tony : " + str(self.tonyPunkte)
            self.GMessage_421["text"] = "Tony gewinne"
            self.GLabel_549["text"] = self.user_name[0] + " : " + str(self.ichPunkte)
            self.GLabel_148["text"] = "Tony : " + str(self.tonyPunkte)

        elif self.ichWahl == 2 and self.tonyWahl == 1:  # Schere vs Stein
            self.tonyPunkte += 1
            self.GLabel_148["text"] = "Tony : " + str(self.tonyPunkte)
            self.GMessage_421["text"] = "Tony gewinne"
            self.GLabel_549["text"] = self.user_name[0] + " : " + str(self.ichPunkte)
            self.GLabel_148["text"] = "Tony : " + str(self.tonyPunkte)

        elif self.ichWahl == 2 and self.tonyWahl == 3:  # Schere vs Papier
            self.ichPunkte += 1
            self.GLabel_549["text"] = "Ich : " + str(self.ichPunkte)
            self.GMessage_421["text"] = "Ich gewinne"
            self.GLabel_549["text"] = self.user_name[0] + " : " + str(self.ichPunkte)
            self.GLabel_148["text"] = "Tony : " + str(self.tonyPunkte)

        elif self.ichWahl == 3 and self.tonyWahl == 1:  # Papier vs Stein\
            self.ichPunkte += 1
            self.GLabel_549["text"] = "Ich : " + str(self.ichPunkte)
            self.GMessage_421["text"] = "Ich gewinne"
            self.GLabel_549["text"] = self.user_name[0] + " : " + str(self.ichPunkte)
            self.GLabel_148["text"] = "Tony : " + str(self.tonyPunkte)

        elif self.ichWahl == 3 and self.tonyWahl == 2:  # Papier vs Schere
            self.tonyPunkte += 1
            self.GLabel_148["text"] = "Tony : " + str(self.tonyPunkte)
            self.GMessage_421["text"] = "Tony gewinne"
            self.GLabel_549["text"] = self.user_name[0] + " : " + str(self.ichPunkte)
            self.GLabel_148["text"] = "Tony : " + str(self.tonyPunkte)

    def GButton_965_command(self):
        """
        Führt die entsprechende Spielaktion aus.

        Diese Methode wird aufgerufen, wenn der Button GButton_965 gedrückt wird.
        Zuerst wird die Methode Clear_alleWahl aufgerufen, um die Auswahlbilder zurückzusetzen.
        Dann wird überprüft, welcher Radiobutton ausgewählt ist (manuell oder Sprachsteuerung).
        Abhängig von der Auswahl wird entweder die Methode manuell_spielen oder voice_spielen aufgerufen.
        """
        self.Clear_alleWahl()
        if self.radioVar.get() == 1:
            self.manuell_spielen()
        else:
            self.voice_spielen()






