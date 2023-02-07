"""
Gestisce i dati e le operazioni relative al tesserato
"""
import pickle


class Tesserato:
       def __init__(self, id, nome, cognome, cf, email, telefono, luogo_nascita, eta, password, categoria, inizio_certificato, scadenza_certificato, gare_partecipate=0, gare_vinte=0):
        super(Tesserato, self).__init__()
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.email = email
        self.telefono = telefono
        self.luogo_nascita = luogo_nascita
        self.eta = eta
        self.password = password
        self.categoria = categoria
        self.gare_partecipate = gare_partecipate
        self.gare_vinte = gare_vinte
        self.inizio_certificato = inizio_certificato
        self.scadenza_certificato = scadenza_certificato


