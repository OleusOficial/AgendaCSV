
import csv

decision = 0
def printMenu():
    print ("\nBIENVENIDO A TU AGENDA")
    print("\nMENU")
    print("\n----------------------------------------------------")
    print("| 1.-Leer Contactos | 2.-Agregar Contacto | 3.-Salir")
    print("----------------------------------------------------")

def readContacts():
    with open("nombre.csv","r") as file:
        data = csv.reader(file,delimiter = ",") 
        for line in data:
            print line 
def addContact(name,email):
    with open("nombre.csv","a") as file:
        data = csv.writer(file,delimiter = ",") 
        data.writerow([name,email])
        print ("\nContacto Agregado")
 
while decision != 3:
    printMenu()
    decision = input("Elige un opcion: ") 
    if decision == 1:
        readContacts()
    elif decision == 2:
        name = raw_input("Ingresa el nombre:\n")
        email = raw_input("Ingresa el email:\n")
        addContact(name,email)
    elif decision == 3:
        print("Ha salido de la agenda")
    else:
        print("Opcion invalida")