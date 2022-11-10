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

#