import tkinter as tk
from tkinter import Toplevel, messagebox
import subprocess

# Fonction pour exécuter des scripts Python
def execute_python_script(script_path):
    try:
        subprocess.run(["python", script_path], check=True)
        # messagebox.showinfo("Succès", f"Le script {script_path} a été exécuté avec succès.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Erreur", f"Une erreur s'est produite lors de l'exécution du script {script_path}.")

# Création d'une nouvelle fenêtre Tkinter
def create_main_window():
    root = tk.Tk()
    root.title("Systémes Experts")
    root.configure(bg='#F0F0F0')  # Couleur de fond de la fenêtre

    # Configuration du cadre principal
    frame = tk.Frame(root, bg='#F0F0F0', padx=20, pady=20)
    frame.pack(padx=10, pady=10)

    # Bouton pour exécuter le premier script Python
    btn_execute_script1 = tk.Button(frame, text="Chainage avant",
                                    command=lambda: execute_python_script("Chainage_avantV1.py"),
                                    width=25, height=2, bg='#ADD8E6', font=('Arial', 10))
    btn_execute_script1.pack(pady=10)

    # Bouton pour exécuter le second script Python
    btn_execute_script2 = tk.Button(frame, text="Chainage arriére",
                                    command=lambda: execute_python_script("chainage_arriéreV1.py"),
                                    width=25, height=2, bg='#ADD8E6', font=('Arial', 10))
    btn_execute_script2.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_main_window()
