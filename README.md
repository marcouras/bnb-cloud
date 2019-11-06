
 Corso Cloud Computing
===============
Progetto del sito vetrina di un BnB
------------------------------------

La struttura del progetto ricalca quella di un progetto AppEngine
abilitando le i servizi di terze parti i.e. Flask.
La sopracitata struttura può essere fatta in automatico da Pycharm, l'IDE
Python di JetBrains.

## Models
All'interno di questo package sono presenti i file python che descrivono
come sono fatte le tabelle sul database, che in questo caso è il 
Google Cloud Datastore.

## Data Access
In questo package sono presenti i file Python che servono per accedere i dati
sul database.
#### Google cloud platform

Per l'hosting sito e del database dobbiamo utilizzare servizi Cloud. Abbiamo scelto di usare [Google Cloud Platform](https://cloud.google.com) (GCP). Per proseguire nel tutorial è necessario avere un account Google (per crearne uno seguire questo [link](https://accounts.google.com/SignUp)).

Una volta effettuato l'accesso, è necessario creare un progetto su [GCP console](https://console.cloud.google.com). 

In questo [video](https://www.youtube.com/watch?v=hgGWa0NHYyM) è possibile vedere tutti i passaggi elencati in questa sezione, ovvero come effetture la distribuzione (deploy) dell'applicazione con i servzi GCP.

Creazione del progetto: 
![Creazione progetto](https://github.com/Maupin1991/SCB-bot-telegram/blob/master/images/create_project.png "Create Project")

Annotare l'ID del progetto (Attenzione: potrebbe essere diverso dal nome perché gli ID sono univoci).

Completati i passaggi su GCP, si passa ora a configurare il progetto. Sarà necessario scaricare questo repository e modificare alcuni file di configurazione.

Il primo passo è quello di installare il software development kit (sdk) per Google App Engine, il quale è ocntenuto all'interno della Google Cloud Platform SDK e Python. Qui si trova il [tutorial](https://cloud.google.com/appengine/docs/standard/python/download) con i link utili e le istruzioni.

Seguire poi [questo tutorial](https://cloud.google.com/appengine/docs/standard/python/getting-started/deploying-the-application) per effettuare il deploy dell'applicazione.
