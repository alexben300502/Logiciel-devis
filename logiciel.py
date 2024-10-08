import tkinter as tk
from tkinter import ttk  # Importer ttk pour utiliser Combobox

# Fonction appelée lorsque l'utilisateur clique sur les boutons
def recuperer_informations():
    rideaux = entree_rideaux.get()  # Récupère la largeur des rideaux
    hauteur = entree_hauteur.get()  # Récupère la hauteur des rideaux
    type_tringle = combobox_type_tringle.get()  # Récupère le type de tringle
    type_confection = combobox_type_confection.get()  # Récupère le type de confection
    ampleur = combobox_ampleur.get()  # Récupère l'ampleur sélectionnée
    
    # Vérifier que tous les champs précédents sont remplis avant de remplir les nouveaux champs
    if rideaux and hauteur and type_tringle and type_confection and ampleur:
        # Remplir les champs en bas une fois que toutes les informations sont fournies
        entree_tarif_confection.config(state='normal')
        entree_tarif_confection.insert(0, "Calculé")
        
        entree_tarif_tringle.config(state='normal')
        entree_tarif_tringle.insert(0, "Calculé")
        
        entree_tarif_tissu.config(state='normal')
        entree_tarif_tissu.insert(0, "Calculé")
        
        entree_quantite_tissu.config(state='normal')
        entree_quantite_tissu.insert(0, "Calculé")
    else:
        print("Veuillez remplir tous les champs précédents.")

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("LOGICIEL")
fenetre.geometry("600x450")  # Augmenter la taille pour afficher tous les champs

# Ligne pour la largeur des rideaux
label_rideaux = tk.Label(fenetre, text="Largeur rideaux (en m) : ")
label_rideaux.grid(row=0, column=0, padx=10, pady=10)

entree_rideaux = tk.Entry(fenetre)
entree_rideaux.grid(row=0, column=1, padx=10, pady=10)

bouton_valider_rideaux = tk.Button(fenetre, text="Valider", command=recuperer_informations)
bouton_valider_rideaux.grid(row=0, column=2, padx=10, pady=10)

# Ligne pour la hauteur des rideaux
label_hauteur = tk.Label(fenetre, text="Hauteur rideaux (en m) : ")
label_hauteur.grid(row=1, column=0, padx=10, pady=10)

entree_hauteur = tk.Entry(fenetre)
entree_hauteur.grid(row=1, column=1, padx=10, pady=10)

bouton_valider_hauteur = tk.Button(fenetre, text="Valider", command=recuperer_informations)
bouton_valider_hauteur.grid(row=1, column=2, padx=10, pady=10)

# Ligne pour le type de tringle
label_type_tringle = tk.Label(fenetre, text="Type de tringle ?")
label_type_tringle.grid(row=2, column=0, padx=10, pady=10)

combobox_type_tringle = ttk.Combobox(fenetre)
combobox_type_tringle['values'] = ("A", "B", "C")  # Ajouter les options dans le combobox
combobox_type_tringle.grid(row=2, column=1, padx=10, pady=10)
combobox_type_tringle.set('')  # Laisser le combobox vide au démarrage

bouton_valider_type_tringle = tk.Button(fenetre, text="Valider", command=recuperer_informations)
bouton_valider_type_tringle.grid(row=2, column=2, padx=10, pady=10)

# Ligne pour le type de confection
label_type_confection = tk.Label(fenetre, text="Type de confection ?")
label_type_confection.grid(row=3, column=0, padx=10, pady=10)

combobox_type_confection = ttk.Combobox(fenetre)
combobox_type_confection['values'] = ("E", "F", "G")  # Ajouter les options dans le combobox
combobox_type_confection.grid(row=3, column=1, padx=10, pady=10)
combobox_type_confection.set('')  # Laisser le combobox vide au démarrage

bouton_valider_type_confection = tk.Button(fenetre, text="Valider", command=recuperer_informations)
bouton_valider_type_confection.grid(row=3, column=2, padx=10, pady=10)

# Ligne pour l'ampleur
label_ampleur = tk.Label(fenetre, text="Ampleur ?")
label_ampleur.grid(row=4, column=0, padx=10, pady=10)

combobox_ampleur = ttk.Combobox(fenetre)
combobox_ampleur['values'] = ("1,50", "2", "2,50")  # Ajouter les options dans le combobox
combobox_ampleur.grid(row=4, column=1, padx=10, pady=10)
combobox_ampleur.set('')  # Laisser le combobox vide au démarrage

bouton_valider_ampleur = tk.Button(fenetre, text="Valider", command=recuperer_informations)
bouton_valider_ampleur.grid(row=4, column=2, padx=10, pady=10)

# Ajouter les champs dépendants en bas, qui seront remplis seulement une fois que les autres champs sont remplis
label_tarif_confection = tk.Label(fenetre, text="Tarif vente confection :")
label_tarif_confection.grid(row=5, column=0, padx=10, pady=10)

entree_tarif_confection = tk.Entry(fenetre)
entree_tarif_confection.grid(row=5, column=1, padx=10, pady=10)
entree_tarif_confection.config(state='disabled')  # Désactiver l'entrée au début

label_tarif_tringle = tk.Label(fenetre, text="Tarif tringle :")
label_tarif_tringle.grid(row=6, column=0, padx=10, pady=10)

entree_tarif_tringle = tk.Entry(fenetre)
entree_tarif_tringle.grid(row=6, column=1, padx=10, pady=10)
entree_tarif_tringle.config(state='disabled')  # Désactiver l'entrée au début

label_tarif_tissu = tk.Label(fenetre, text="Tarif vente tissus :")
label_tarif_tissu.grid(row=7, column=0, padx=10, pady=10)

entree_tarif_tissu = tk.Entry(fenetre)
entree_tarif_tissu.grid(row=7, column=1, padx=10, pady=10)
entree_tarif_tissu.config(state='disabled')  # Désactiver l'entrée au début

label_quantite_tissu = tk.Label(fenetre, text="Quantité tissu :")
label_quantite_tissu.grid(row=8, column=0, padx=10, pady=10)

entree_quantite_tissu = tk.Entry(fenetre)
entree_quantite_tissu.grid(row=8, column=1, padx=10, pady=10)
entree_quantite_tissu.config(state='disabled')  # Désactiver l'entrée au début

# Démarrer la boucle principale
fenetre.mainloop()
