class Eroller:
    def __init__(self, marka, seb, telj) -> None:
        self.marka = marka #szöveg
        self.maxseb = int(seb) #egész szám, a maximális sebesség km/h -ban
        self.teljesitmeny = int(telj) #a teljesítmény Watt-ban