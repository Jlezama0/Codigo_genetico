# Codigo Dogma central 

codigo_genetico = {
    "Phe": ["UUC","UUU"],
    "Leu": ["UUA","UUG","CUU","CUC","CUA","CUG"],
    "Ser": ["UCU","UCC","UCA","UCG"],
    "Tyr": ["UAU","UAC"],
    "Cys": ["UGU","UGC"],
    "Trp": ["UGG"],
    "Stop": ["UAA","UAG","UGA"],
    "Pro": ["CCU","CCC","CCA","CCG"],
    "His": ["CAU","CAC"],
    "Gln": ["CAA","CAG"],
    "Arg": ["CGU","CGC","CGA","CGG","AGA","AGG"],
    "":[],
}

def arnMensajero(cadena : str):

    arn_lista = []

    # Ciclo para combertir el ADN en arn mensajero
    for a in cadena:
        if a == 'A':
            arn_lista.append('U')
        elif a == 'T':
            arn_lista.append('A')
        elif a == 'G':
            arn_lista.append('C')
        else :
            arn_lista.append('G')
    
    arnM = ''.join(arn_lista)
    
    return arnM

adn = input("Cadena: ")

print(arnMensajero(adn))