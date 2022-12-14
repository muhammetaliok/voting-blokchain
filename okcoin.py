from hashlib import sha256
import time

class block:
    def __init__(self,timeStamp,data,previousHash=''):
        self.timeStamp = timeStamp
        self.data = data 
        self.previousHash = previousHash
        self.kuvvet = 0 
        self.hash = self.hesapla()
        

    def hesapla(self):
        while True:
            self.kuvvet = self.kuvvet+1
            ozet = sha256((str( self.timeStamp)+str(self.data)+str(self.previousHash)+str(self.kuvvet)).encode()).hexdigest()
            if ozet[0:2] == "00":
                break
                
        return ozet
class blockChain:
    def __init__(self):
        self.chain=[self.genesisOlustur()]

    def genesisOlustur(self):
        return block(time.ctime(),"Merhaba","")
    
    def blockEkle(self,data):
        node = block(time.ctime(),data,self.chain[-1].hash)
        self.chain.append(node)

    def kontrol(self):
        for i in range(len(self.chain)):
            if i!=0:
                ilk = self.chain[i-1].hash
                suan = self.chain[i].previousHash
                if ilk!=suan:
                    return "Zincir kopmuş"
                if sha256((str(self.chain[i].timeStamp)+str(self.chain[i].data)+str(self.chain[i].previousHash)+str(self.chain[i].kuvvet)).encode()).hexdigest() != self.chain[i].hash:
                    return "Zincir kopmuş"
        return "Sağlam"

    def listeleme(self):
        print("Blokchain")
        for i in range(len(self.chain)):
            print("Block => ",i,"\nHash = ",str(self.chain[i].hash),"\nZaman Damgası = ",str(self.chain[i].timeStamp),"\nData = ",str(self.chain[i].data),"\nKuvvet = ", str(self.chain[i].kuvvet),"\npreviousHash",str(self.chain[i].previousHash))
            print("-------------------------------------")
    
OkChain = blockChain()

while True:
    print("Lütfen Seçiminizi Yapınız \nBlock Eklemek için 1 \nBlockchain'i Görmek İçin 2 \nZinciri Kontrol Etmek İçin 3 \n Çıkmak için 4'ü seçin")
    data = input()
    if data == "1":
        print("Gönderilen miktarı giriniz: ")
        miktar = input()
        OkChain.blockEkle(miktar)
    elif data == "2":
        OkChain.listeleme()
    elif data == "3":
        print(str(OkChain.kontrol()))
    elif data == "4":
        break
                  

                    
        