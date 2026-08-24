import random

dicionario = {
    "processador": [
        {"nome": "Ryzen 5 5600", "preco": 850.00, "marca": "AMD", "pontos": 75},
        {"nome": "Core i5 12400F", "preco": 900.00, "marca": "Intel", "pontos": 78},
        {"nome": "Ryzen 7 5700X", "preco": 1200.00, "marca": "AMD", "pontos": 85},
        {"nome": "Core i5 13600K", "preco": 1800.00, "marca": "Intel", "pontos": 92},
        {"nome": "Ryzen 7 7800X3D", "preco": 2500.00, "marca": "AMD", "pontos": 100}
    ],

    "placa de video": [
        {"nome": "RX 6600", "preco": 1400.00, "marca": "AMD", "pontos": 70},
        {"nome": "RTX 4060", "preco": 2100.00, "marca": "NVIDIA", "pontos": 80},
        {"nome": "RX 7700 XT", "preco": 3000.00, "marca": "AMD", "pontos": 88},
        {"nome": "RTX 4070 Super", "preco": 4200.00, "marca": "NVIDIA", "pontos": 95},
        {"nome": "RTX 4090", "preco": 11000.00, "marca": "NVIDIA", "pontos": 100}
    ],

    "placa mae": [
        {"nome": "B450M Steel Legend", "preco": 600.00, "marca": "ASRock", "pontos": 65},
        {"nome": "B550M Aorus Elite", "preco": 750.00, "marca": "Gigabyte", "pontos": 75},
        {"nome": "B660M Gaming X", "preco": 850.00, "marca": "Gigabyte", "pontos": 80},
        {"nome": "TUF Gaming B650M", "preco": 1300.00, "marca": "ASUS", "pontos": 90},
        {"nome": "ROG Strix X670E", "preco": 3000.00, "marca": "ASUS", "pontos": 100}
    ],

    "memoria ram": [
        {"nome": "ValueRAM 8GB", "preco": 150.00, "marca": "Kingston", "pontos": 55},
        {"nome": "Fury Beast 16GB", "preco": 300.00, "marca": "Kingston", "pontos": 70},
        {"nome": "Vengeance 16GB", "preco": 350.00, "marca": "Corsair", "pontos": 75},
        {"nome": "Trident Z 32GB", "preco": 700.00, "marca": "G.Skill", "pontos": 90},
        {"nome": "Dominator 64GB", "preco": 1400.00, "marca": "Corsair", "pontos": 100}
    ],

    "ssd": [
        {"nome": "A400 480GB", "preco": 200.00, "marca": "Kingston", "pontos": 55},
        {"nome": "NV2 1TB", "preco": 400.00, "marca": "Kingston", "pontos": 70},
        {"nome": "970 EVO Plus 1TB", "preco": 550.00, "marca": "Samsung", "pontos": 82},
        {"nome": "SN850X 2TB", "preco": 900.00, "marca": "Western Digital", "pontos": 94},
        {"nome": "990 Pro 2TB", "preco": 1200.00, "marca": "Samsung", "pontos": 100}
    ],

    "gabinete": [
        {"nome": "Ninja Leaf", "preco": 250.00, "marca": "Pichau", "pontos": 55},
        {"nome": "H510", "preco": 450.00, "marca": "NZXT", "pontos": 70},
        {"nome": "4000D Airflow", "preco": 550.00, "marca": "Corsair", "pontos": 80},
        {"nome": "H7 Flow", "preco": 850.00, "marca": "NZXT", "pontos": 90},
        {"nome": "O11 Dynamic EVO", "preco": 1300.00, "marca": "Lian Li", "pontos": 100}
    ],

    "fonte": [
        {"nome": "MWE 500W", "preco": 300.00, "marca": "Cooler Master", "pontos": 60},
        {"nome": "CV650", "preco": 450.00, "marca": "Corsair", "pontos": 72},
        {"nome": "Core Reactor 750W", "preco": 650.00, "marca": "XPG", "pontos": 85},
        {"nome": "RM850x", "preco": 900.00, "marca": "Corsair", "pontos": 94},
        {"nome": "ROG Thor 1200W", "preco": 2000.00, "marca": "ASUS", "pontos": 100}
    ],

    "cooler": [
        {"nome": "Cooler Box", "preco": 80.00, "marca": "AMD", "pontos": 50},
        {"nome": "Hyper 212", "preco": 250.00, "marca": "Cooler Master", "pontos": 70},
        {"nome": "AK400", "preco": 300.00, "marca": "DeepCool", "pontos": 76},
        {"nome": "AK620", "preco": 450.00, "marca": "DeepCool", "pontos": 90},
        {"nome": "NH-D15", "preco": 850.00, "marca": "Noctua", "pontos": 100}
    ],

    "water cooler": [
        {"nome": "Gammaxx L120", "preco": 300.00, "marca": "DeepCool", "pontos": 60},
        {"nome": "MasterLiquid ML240L", "preco": 550.00, "marca": "Cooler Master", "pontos": 75},
        {"nome": "LS520", "preco": 700.00, "marca": "DeepCool", "pontos": 85},
        {"nome": "Kraken 240", "preco": 900.00, "marca": "NZXT", "pontos": 92},
        {"nome": "H150i Elite", "preco": 1500.00, "marca": "Corsair", "pontos": 100}
    ],

    "hd": [
        {"nome": "Barracuda 1TB", "preco": 280.00, "marca": "Seagate", "pontos": 55},
        {"nome": "Blue 1TB", "preco": 300.00, "marca": "Western Digital", "pontos": 60},
        {"nome": "Barracuda 2TB", "preco": 400.00, "marca": "Seagate", "pontos": 70},
        {"nome": "Blue 4TB", "preco": 650.00, "marca": "Western Digital", "pontos": 85},
        {"nome": "IronWolf 8TB", "preco": 1300.00, "marca": "Seagate", "pontos": 100}
    ],

    "ventoinha": [
        {"nome": "RF120", "preco": 50.00, "marca": "DeepCool", "pontos": 55},
        {"nome": "SickleFlow 120", "preco": 80.00, "marca": "Cooler Master", "pontos": 65},
        {"nome": "AF120 Elite", "preco": 130.00, "marca": "Corsair", "pontos": 75},
        {"nome": "F120 RGB", "preco": 180.00, "marca": "NZXT", "pontos": 88},
        {"nome": "NF-A12x25", "preco": 250.00, "marca": "Noctua", "pontos": 100}
    ],

    "mouse": [
        {"nome": "G203", "preco": 150.00, "marca": "Logitech", "pontos": 60},
        {"nome": "DeathAdder Essential", "preco": 180.00, "marca": "Razer", "pontos": 65},
        {"nome": "G502 Hero", "preco": 350.00, "marca": "Logitech", "pontos": 78},
        {"nome": "DeathAdder V3", "preco": 500.00, "marca": "Razer", "pontos": 90},
        {"nome": "G Pro X Superlight", "preco": 700.00, "marca": "Logitech", "pontos": 100}
    ],

    "monitor": [
        {"nome": "T350 24", "preco": 700.00, "marca": "Samsung", "pontos": 60},
        {"nome": "UltraGear 24GN60R", "preco": 1100.00, "marca": "LG", "pontos": 75},
        {"nome": "Odyssey G3", "preco": 1200.00, "marca": "Samsung", "pontos": 80},
        {"nome": "UltraGear 27 240Hz", "preco": 2500.00, "marca": "LG", "pontos": 92},
        {"nome": "Odyssey OLED G8", "preco": 6000.00, "marca": "Samsung", "pontos": 100}
    ],

    "teclado": [
        {"nome": "K120", "preco": 100.00, "marca": "Logitech", "pontos": 50},
        {"nome": "Alloy Core", "preco": 250.00, "marca": "HyperX", "pontos": 65},
        {"nome": "G Pro", "preco": 650.00, "marca": "Logitech", "pontos": 82},
        {"nome": "Huntsman Mini", "preco": 700.00, "marca": "Razer", "pontos": 90},
        {"nome": "BlackWidow V4 Pro", "preco": 1500.00, "marca": "Razer", "pontos": 100}
    ],

    "mousepad": [
        {"nome": "Speed Pequeno", "preco": 50.00, "marca": "Redragon", "pontos": 50},
        {"nome": "Gigantus V2", "preco": 150.00, "marca": "Razer", "pontos": 70},
        {"nome": "G640", "preco": 200.00, "marca": "Logitech", "pontos": 78},
        {"nome": "MM700 RGB", "preco": 400.00, "marca": "Corsair", "pontos": 90},
        {"nome": "Firefly V2", "preco": 550.00, "marca": "Razer", "pontos": 100}
    ],

    "fone": [
        {"nome": "H2002D", "preco": 180.00, "marca": "Havit", "pontos": 60},
        {"nome": "Cloud Stinger", "preco": 300.00, "marca": "HyperX", "pontos": 70},
        {"nome": "Cloud II", "preco": 500.00, "marca": "HyperX", "pontos": 82},
        {"nome": "G Pro X", "preco": 650.00, "marca": "Logitech", "pontos": 90},
        {"nome": "Cloud Alpha Wireless", "preco": 1200.00, "marca": "HyperX", "pontos": 100}
    ],

    "microfone": [
        {"nome": "Fifine K669", "preco": 250.00, "marca": "Fifine", "pontos": 60},
        {"nome": "SoloCast", "preco": 400.00, "marca": "HyperX", "pontos": 72},
        {"nome": "QuadCast", "preco": 700.00, "marca": "HyperX", "pontos": 85},
        {"nome": "QuadCast S", "preco": 900.00, "marca": "HyperX", "pontos": 92},
        {"nome": "Blue Yeti X", "preco": 1200.00, "marca": "Logitech", "pontos": 100}
    ],

    "webcam": [
        {"nome": "C270", "preco": 180.00, "marca": "Logitech", "pontos": 55},
        {"nome": "C920", "preco": 450.00, "marca": "Logitech", "pontos": 72},
        {"nome": "Kiyo", "preco": 550.00, "marca": "Razer", "pontos": 80},
        {"nome": "Kiyo Pro", "preco": 750.00, "marca": "Razer", "pontos": 90},
        {"nome": "Brio 4K", "preco": 1100.00, "marca": "Logitech", "pontos": 100}
    ],

    "cadeira": [
        {"nome": "EC1", "preco": 700.00, "marca": "ThunderX3", "pontos": 60},
        {"nome": "TGC12", "preco": 1000.00, "marca": "ThunderX3", "pontos": 70},
        {"nome": "T3 Rush", "preco": 1500.00, "marca": "Corsair", "pontos": 82},
        {"nome": "Enki", "preco": 1900.00, "marca": "Razer", "pontos": 90},
        {"nome": "Titan Evo", "preco": 3000.00, "marca": "Secretlab", "pontos": 100}
    ]
}

componentes = [
    "processador",
    "placa de video",
    "placa mae",
    "memoria ram",
    "ssd",
    "gabinete",
    "fonte",
    "cooler",
    "water cooler",
    "hd",
    "ventoinha",
    "mouse",
    "monitor",
    "teclado",
    "mousepad",
    "fone",
    "microfone",
    "webcam",
    "cadeira"
]

pc=dict()

def existe_no_pc(componente,dicionario):
    if componente in dicionario:
        return True
    else:
        return False

def existe_nome(componente,nome,dicionario):
    for i in dicionario[componente]:
        if nome==i['nome']:
            return True
    else:
        return False

for i in range(len(componentes)):
    pc[componentes[i]]={
        'nome':'',
        'preco':0,
        'pontos':0
    }

print('==========Monte seu pc==========')

usadas=[]

while True:
    falta=[]
    if len(falta)==0:
        break
    print('componentes disponiveis:')
    for i in dicionario:
        print(i)
    print('='*10)
    componente=input('qual componente voce quer colocar? ').lower()
    if existe_no_pc(componente,dicionario):
        if pc[componente]['nome']!='':
            print('esse componente ja esta adicionado ao pc')
            trocar=input('Quer trocar o componente? ').lower()
            if trocar=='s':
                print('peças disponiveis:')
                for i in dicionario[componente]:
                    if [componente, i['nome']] not in usadas:
                        print(f'{i['nome']} - R$ {i['preco']}')
                peca=input('qual peça voce quer? ')
                if existe_nome(componente,peca,dicionario):
                        for i in dicionario[componente]:
                            if i['nome']==peca:
                                usadas.remove([componente, pc[componente]['nome']])
                                pc[componente]['nome']=i['nome']
                                pc[componente]['preco']=i['preco']
                                pc[componente]['pontos']=i['pontos']
                                usadas.append([componente, i['nome']])
                else:
                    print('nao existe essa peça')
                    continue
            else:
                continue
        else:
            print('peças disponiveis:')
    else:
        print('nao exite esse componente')
        continue
        
                        