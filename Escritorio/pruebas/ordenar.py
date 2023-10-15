
def fetch():
    import requests
    response = requests.get("https://fakestoreapi.com/products")
    if response.status_code == 200:
        data = response.json()
    else:
        data = {}
    electronics = []
    data.sort(key=lambda x: x["price"])
    for item in data:
        if item["category"] == "electronics":
            electronics.append(item)
    for i in electronics:
        if i["price"] < 70:
            print(i)

def validarPalindromo(text):
    inverso = ""
    for i in range(len(text)-1, -1, -1):
        inverso += text[i]
    if inverso == text:
        print("true")
    else:
        print("False")

def numberMax(array):
    array.sort()
    posicion=len(array)
    print(f"El número más grande es: {array[posicion-1]}")

def anagrama(parrafoExtraido):
    parrafo = parrafoExtraido.lower()
    alfabeto = set("abcdefghijklmnopqrstuvwxyz")
    parrafoF = []
    for i in range(len(parrafo)):
        if parrafo[i] in alfabeto:
            if parrafo[i] not in parrafoF:
                parrafoF += parrafo[i]
    print(parrafoF)
    print(alfabeto)
    if len(alfabeto) == len(parrafoF):
        print("true")
    else:
        print("false") 

anagrama("El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja")