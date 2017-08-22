# -*-coding:Latin-1 -*

class Send:
    def __init__(self, serv, port):
        import json
        import requests

        with open('.tmp') as json_data:
            d = json.load(json_data)
            print(d["hpMax"])

        r = requests.post("http://" + serv + ":" + port + "/login", data={'name':d["name"], 'hpMax':d["hpMax"], 'hp':d["hp"], 'attack':d["attack"], 'precision':d["precision"], 'lvl':d["lvl"],'Objects': d["Objects"], 'Usables': d["Usables"]})
        self.status = r.status_code
        self.reason = r.reason

if __name__ == "__main__":
    s = Send("10.70.3.76","3000")
    print(s.status, s.reason)
