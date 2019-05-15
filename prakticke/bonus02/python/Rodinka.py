#! /usr/bin/env python3

class Rodinka:
    class Riesenie:
        def __init__(self, otec : str, matka : str, syn : str, dcera : str) -> None:
            self.otec = otec # type: str
            self.matka = matka # type: str
            self.syn = syn # type: str
            self.dcera = dcera # type: str
    def vyries(self) -> Riesenie:
        return Rodinka.Riesenie('', '', '', '')
