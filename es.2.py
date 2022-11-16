#sapendo che una funzione è un blocco dati in cui poter inserire più dati stampabili solo quando la funzione viene richiamata, per richiamare i contenuti bisogna:

def funzione1(): #definire la propria funzione e porre del vuoto tra delle parentesi
  print("contenuto funzione1") #anche se si usa il comando print scrivendo i contenuti della funzione avremo la stampa solo e unicamente se si scriverà manualmente il nome dato alla funzione

funzione1()

#Gli argomenti sono specificati dopo il nome della funzione, tra parentesi. Puoi aggiungere tutti gli argomenti che vuoi, separandoli semplicemente con una virgola.
def funzione1(colore):
  print(colore + " gatto")

funzione1("rosso")
funzione1("nero")
funzione1("tricolore")

#una funzione deve essere chiamata con il numero corretto di argomenti, quindi bisogna chiamare la funzione con il numero di argomenti, non di più e non di meno
def my_function(nome, cognome, età):
  print(nome + " " + cognome + " " + età)

my_function("laura", "ottino,", "18 anni")

#nel caso non conoscessi il contenuto della funzione e si voglia stamparlo comunque, basta aggiungere *davanti al nome della funzione
def my_function(*informazioni):
  print(*informazioni)

my_function("laura", "ottino", "18 anni", "vive a Milano")

#nel momento in cui gli argomenti nella funzione sono in disordine e li si vuole stampare ordinatamente, allora dobbiamo definire ogni nome a ogni argomento 
def my_function(bimbo1, bimbo3, bimbo4, bimbo2):
  print(bimbo1, bimbo2, bimbo3, bimbo4)

my_function(bimbo1 = "Emil", bimbo2 = "Tobias", bimbo3 = "Linus", bimbo4 = "Charlie")

#quando gli argomenti nella funzione sono in disordine e si vuole stampare un determinato nome in una determinata posizione bisogna usare **
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
