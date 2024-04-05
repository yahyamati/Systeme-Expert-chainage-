import tkinter as tk
from tkinter import scrolledtext

def backward_chaining(facts, goal, rules):
    messages = []

    def attempt_to_prove_goal(current_goal, applied_rules=[]):
        if current_goal in facts:
            messages.append(f"Le but '{current_goal}' est déjà un fait connu.")
            return True

        rule_applied = False
        for rule_number, (premise, conclusion) in enumerate(rules, start=1):
            if conclusion == current_goal and rule_number not in applied_rules:
                if all(p in facts for p in premise):
                    if current_goal not in facts:
                        facts.append(current_goal)
                    messages.append(f"Le but '{current_goal}' est atteint; règle traitée: {rule_number}; nouvelle base de faits: {facts}")
                    return True
                else:
                    missing_premises = [p for p in premise if p not in facts]
                    messages.append(f"Le nouveau but est : {missing_premises}")
                    all_premises_proven = True
                    for mp in missing_premises:
                        if not attempt_to_prove_goal(mp, applied_rules + [rule_number]):
                            all_premises_proven = False
                            break
                        elif mp not in facts:
                            facts.append(mp)
                    if all_premises_proven:
                        if current_goal not in facts:
                            facts.append(current_goal)
                        messages.append(f"Après avoir prouvé les prémisses, le but '{current_goal}' est atteint avec la règle {rule_number}; nouvelle base de faits: {facts}")
                        return True
                    else:
                        rule_applied = True

        if not rule_applied:
            messages.append(f"'Backtracking':Impossible d'atteindre le but '{current_goal}' avec les règles et faits actuels .")
        return rule_applied

    success = attempt_to_prove_goal(goal)
    return success, messages

class BackwardChainingApp:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Chaînage Arrière ")

        # Zone pour les faits
        tk.Label(root, text="Faits (séparés par des virgules)").pack()
        self.facts_entry = tk.Entry(root, width=100)
        self.facts_entry.pack()

        # Zone pour les règles avec ScrolledText pour saisie ligne par ligne
        tk.Label(root, text="Règles (une règle par ligne, format A,B=>C)").pack()
        self.rules_text = scrolledtext.ScrolledText(root, height=10, width=100)
        self.rules_text.pack()

        # Zone pour l'objectif
        tk.Label(root, text="Objectif").pack()
        self.goal_entry = tk.Entry(root, width=100)
        self.goal_entry.pack()

        # Bouton pour exécuter le chaînage arrière
        self.execute_button = tk.Button(root, text="Exécuter le Chaînage Arrière", command=self.execute_backward_chaining , bg='#ADD8E6' )
        self.execute_button.pack(pady=20)

        # Zone de texte pour afficher les messages
        self.text_area = scrolledtext.ScrolledText(root, height=20, width=100)
        self.text_area.pack(pady=10)

    def execute_backward_chaining(self):
        facts = [fact.strip() for fact in self.facts_entry.get().split(',') if fact.strip()]
        goal = self.goal_entry.get().strip()
        rules_str = self.rules_text.get("1.0", tk.END).strip().split('\n')
        rules = [(rule.split('=>')[0].split(','), rule.split('=>')[1]) for rule in rules_str if '=>' in rule]
        rules = [([p.strip() for p in premise], conclusion.strip()) for premise, conclusion in rules]

        success, messages = backward_chaining(facts, goal, rules)
        self.text_area.delete('1.0', tk.END)
        if success:
            self.text_area.insert(tk.INSERT, "Résultat : BUT est atteint.\n")
        else:
            self.text_area.insert(tk.INSERT, "Résultat : BUT non atteint.\n")
        for message in messages:
            self.text_area.insert(tk.INSERT, message + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = BackwardChainingApp(root)
    root.mainloop()
