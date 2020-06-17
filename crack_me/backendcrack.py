def cod_caesar(texto_cod, key):
#Aca armo el array a encriptar
    caesar_array = []
    crypto_array = []
    abc_array = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    for x in texto_cod:
        if x!=" " and isinstance(x, str):
            x1 = x.lower()
            caesar_array.append(x1)

#Aca armo el array encriptado
    for i in caesar_array:
        for j in abc_array:
            if i==j:
                crypto_array.append(abc_array[(abc_array.index(j)+key)%26])

#Aca transformo el array a un string final
    crypto_text = ""
    for x in crypto_array:
        crypto_text+=x

    return crypto_text

def cod_vigenere(texto_cod):
    print(texto_cod)