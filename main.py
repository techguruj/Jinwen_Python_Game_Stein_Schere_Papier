import fenster1
import tkinter as tk
import fenster2



user_name = [""]

root = tk.Tk()                                              # Erstellt ein Fenster1
app =fenster1.App(root,user_name)       # Erstellt ein Objekt der Klasse App
root.mainloop()                                         # Startet die Schleife des Fensters

root2 = tk.Tk()                                             # Erstellt ein Fenster2
app2 = fenster2.App(root2,user_name)    # Erstellt ein Objekt der Klasse App
root2.mainloop()                                            # Startet die Schleife des Fensters








