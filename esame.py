class ExamException(Exception):
    pass


class CSVFile():
    
    def __init__(self, name):
        self.name = name
        
        if not isinstance(name,str):
            raise ExamException('la variabile name dell\'oggetto non è una stringa')
        
    def get_data(self):
        #controlli legati all'esistenza e all'apertura del file, non al contenuto
        try:
            file = open(self.name,'r')
            file.readline()
        except:
            raise ExamException('c\'è stato un problema in apertura o lettura del file')
            
        #io voglio aprire il file, prendere i valori dalle prime due colonne e metterli in una lista di due elementi
        coppia_valori = []
        
        file = open(self.name,'r')
        
        for i,line in enumerate(file):
            
            tmp = []
            elements = line.split(',') 
            #se non ho due elementi nella linea passo alla linea successiva
            if len(elements) < 2:
                continue
                
            if elements[0]!='date':
                data = elements[0]
                value = elements[1]
                value = value.strip()
                tmp.append(data)
                tmp.append(value)
                coppia_valori.append(tmp)

        file.close()
        #questa get_data restituisce una lista di liste contenenti in posizione 0 la data e in posizione 1 il valore, entrambi sotto forma di stringa.
        return coppia_valori 


class CSVTimeSeriesFile(CSVFile):
    def __init__(self,name):
        super().__init__(name)

    def date_test(self,coppia_valori):
        ok_coppia_valori = []
        prev_year = -1
        prev_month = -1
        for i in range(len(coppia_valori)):
            #se non splitta non è una data e si passa oltre, ma potrebbero essere rimaste ancora cose brutte
            try:
                date = coppia_valori[i][0].split('-')
            except:
                continue
            #provo se ho diviso in due elementi
            if len(date) != 2:
                continue
            try:
                date[0] = int(date[0])
            except:
                continue
            if date[0] < 0: #l'anno non può essere <0
                continue
            try: #passo al mese
                date[1] = int(date[1])
            except:
                continue
            if date[1] not in range(1,13):#verifico che il mese esista
                continue
            #ora so di star lavorando con [yyyy,mm], entrambi valori numerici. Verifico l'ordine
            if prev_year != -1:#è -1 solo al primo passaggio
                if date[0]<prev_year:#se l'anno è minore del precedente c'è un errore
                    raise ExamException('le date non sono in ordine')
            if prev_month != -1:#se non è il primo elemento che verifico
                if date[0] == prev_year:#se sono nello stesso anno il mese deve essere successivo, altrimenti non è un problema
                    if date[1] <= prev_month:
                        raise ExamException('le date non sono in ordine o sono duplicate')
            prev_year = date[0]
            prev_month = date[1]
            ok_coppia_valori.append(coppia_valori[i])

        return ok_coppia_valori
    
    def get_data(self):
        coppia_valori = super().get_data()
        #controllo che il secondo valore sia numerico facendo il cast ad int e salvo solo i valori numerici, cancellando gli altri
        num_only = []        
        for i in range(len(coppia_valori)):
            try:
                coppia_valori[i][1] = int(coppia_valori[i][1])
                if coppia_valori[i][1] > 0:
                    num_only.append(coppia_valori[i])
            except:
                pass
        coppia_valori = num_only
        #ora devo verificare le date
        coppia_valori = self.date_test(coppia_valori)
        return coppia_valori


def test_years(years):
    #verifico che years sia una lista, abbia due valori numerici e questi siano consecutivi (nel caso fossero invertiti li scambia)
    if not isinstance(years,list):
        raise ExamException('years non è una lista')
    if not len(years)==2:
        raise ExamException('non ho due valori di years da valutare')
    if not isinstance(years[0],int) or not isinstance(years[1],int):
        try:
            years[0] = int(years[0])
            years[1] = int(years[1])
        except:
            raise ExamException('non ho valori numerici in years')
    if years[0] < 0 and years[1]<0:
        raise ExamException('gli anni non possono essere negativi')
    if years[1]<years[0]:
        tmp = years[1]
        years[1]=years[0]
        years[0]=tmp
    if not years[0] == years[1] - 1:
        raise ExamException('i valori di years non sono consecutivi')


def twelve_months(list):
    #a partire dai valori che ho li metto in una lista contenente 12 valori, uno per mese
    twelve = [None,None,None,None,None,None,None,None,None,None,None,None]
    for i in range(len(list)):
        for j in range(12):
            if (list[i][0][1])==j+1:
                twelve[j]=list[i][1]
    return twelve


def diff_months(values):
    difference = []
    for i in range(11):
        if values[i+1]!=None and values[i]!=None:
            difference.append(values[i+1] - values[i])
        else:
            difference.append(None)
    return difference


def detect_similar_monthly_variations(time_series, years):
    #time series mi viene passata già clean, devo verificare years
    test_years(years)
    #a questo punto so che i dati con cui lavoro sono buoni da utlizzare
    #trasformo la data da stringa a lista di numeri con cui posso lavorare
    #inserisco i valori dell'anno x in low, dell'anno x+1 in high
    low = []
    high = []
    for i in range(len(time_series)):
        date = time_series[i][0].split('-') 
        date[0] = int(date[0])
        date[1] = int(date[1])
        time_series[i][0] = date
        if time_series[i][0][0] == years[0]:
            low.append(time_series[i])  
        if time_series[i][0][0] == years[1]:
            high.append(time_series[i])
    if len(low)==0 or len(high)==0:
        raise ExamException('uno dei due anni non è presente tra i dati')
    #ora ho due liste con i valori dei due anni in questione
    low = twelve_months(low)
    high = twelve_months(high)
    #faccio la differenza tra i valori di mesi successsivi
    low = diff_months(low)
    high = diff_months(high)
    #salvo in una lista la differenza tra un anno e l'altro
    variazione = []
    for i in range(11):
        if low[i]!=None and high[i]!=None:
            variazione.append(low[i]-high[i])
        else:
            variazione.append(None)
    #assegno True o False alle varie differenze 
    for i in range(11):
        if variazione[i] != None:
            if variazione[i]<=2 and variazione[i]>=-2:
                variazione[i] = True
            else:
                variazione[i] = False
        else:
            variazione[i] = False
            
    return variazione