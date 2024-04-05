import tkinter as tk

def get_regle_from_input(entry_regle_base):
    """Extrait les règles saisies par l'utilisateur, les nettoie, et les stocke dans un dictionnaire avec un numéro de règle unique."""
    regle_str = entry_regle_base.get("1.0", tk.END)
    regles = regle_str.splitlines()
    regle_dict = {}
    for index, regle in enumerate(regles):
        regle = regle.strip()
        if regle:
            cond, conc = regle.split("=>")
            conds = tuple(cond.strip() for cond in cond.split(","))
            conc = conc.strip()
            # Stocke les règles avec un numéro unique (index + 1 pour commencer à 1)
            if conds in regle_dict:
                regle_dict[conds].append((conc, index + 1))  # Utilisez index + 1 pour le numéro de la règle
            else:
                regle_dict[conds] = [(conc, index + 1)]
    return regle_dict

def chainage_av(regle_dict, fait, but, result_entry):
    """Applique les règles basées sur la base de faits actuelle, en affichant le numéro de chaque règle appliquée."""
    while True:
        progress_made = False
        for conditions, conclusions in sorted(regle_dict.items(), key=lambda item: (-len(item[0]), item[1][0][1])):
            for conclusion, rule_number in conclusions:
                if all(cond in fait for cond in conditions) and conclusion not in fait:
                    fait.add(conclusion)
                    # Affiche le numéro de la règle avec les prémisses et la conclusion
                    result_entry.insert(tk.END, f"==>Appliquer la Règle {rule_number}: de prémisses {conditions} avec conclusion {conclusion} .\n")
                    result_entry.insert(tk.END, f"La nouvelle base de faits est {fait}\n")
                    progress_made = True
                    if but in fait:
                        result_entry.insert(tk.END, "But atteint.\n")
                        return
                    break
            if progress_made: break
        if not progress_made:
            result_entry.insert(tk.END, "Aucune règle supplémentaire ne peut être appliquée.\n")
            return

# L'initialisation de l'interface utilisateur Tkinter et le reste du code pour exécuter le programme restent inchangés.

# La suite du code pour configurer l'interface utilisateur Tkinter et exécuter le programme reste inchangée.
def run_program(entry_regle_base, fait_entry, but_entry, result_entry):
    """Initialise le processus de chaînage avant avec les entrées utilisateur."""
    regle_dict = get_regle_from_input(entry_regle_base)
    fait = set(fait_entry.get().split(','))
    but = but_entry.get()
    result_entry.delete('1.0', tk.END)
    chainage_av(regle_dict, fait, but, result_entry)

# Ici, vous devez réintégrer la configuration de l'interface Tkinter qui a été omise pour la brièveté.

# Configuration de l'interface utilisateur tkinter...
root = tk.Tk()
root.title("Résultat de chainage_av")

label_regle_base = tk.Label(root, text="Entrer les règles de base (Condition:Conclusion):")
entry_regle_base = tk.Text(root, width=40, height=10)
fait_label = tk.Label(root, text="Entrer la base de faits (séparés par des virgules):")
fait_entry = tk.Entry(root)
but_label = tk.Label(root, text="Entrer le but:")
but_entry = tk.Entry(root)
result_entry = tk.Text(root, width=80, height=20)
run_button = tk.Button(root, text="Exécuter le programme", command=lambda: run_program(entry_regle_base, fait_entry, but_entry, result_entry) , bg='#ADD8E6')

label_regle_base.pack(pady=10)
entry_regle_base.pack(pady=15)
fait_label.pack(pady=5)
fait_entry.pack(pady=5)
but_label.pack(pady=5)
but_entry.pack(pady=5)
result_entry.pack(pady=10)
run_button.pack(pady=5)

root.mainloop()
