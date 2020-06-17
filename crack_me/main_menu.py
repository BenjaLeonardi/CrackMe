import backendcrack

def menu(): 
        option = 1
        while option!=6:
                print("""

                 _____                _     ___  ___     _          __   _____  _____   
                /  __ \              | |    |  \/  |    | |        /  | |  _  ||  _  |  
                | /  \/_ __ __ _  ___| | __ | .  . | ___| |        `| | | |/' || |/' |  
                | |   | '__/ _` |/ __| |/ / | |\/| |/ _ \ |         | | |  /| ||  /| |  
                | \__/\ | | (_| | (__|   <  | |  | |  __/_|        _| |_\ |_/ /\ |_/ /  
                 \____/_|  \__,_|\___|_|\_\ \_|  |_/\___(_)        \___(_)___(_)\___/   
                                                         ______                                          
                                                        |______|                                         
                 _                 _   _              _ _____      _      _             
                | |               | \ | |            | /  ___|    (_)    (_)            
                | |__  _   _      |  \| | ___ _ __ __| \ `--.  ___ _  ___ _  ___  _ __  
                | '_ \| | | |     | . ` |/ _ \ '__/ _` |`--. \/ __| |/ __| |/ _ \| '_ \ 
                | |_) | |_| |     | |\  |  __/ | | (_| /\__/ / (__| | (__| | (_) | | | |
                |_.__/ \__, |     \_| \_/\___|_|  \__,_\____/ \___|_|\___|_|\___/|_| |_|
                        __/ |                                                           
                       |___/                                                            

                """)

                print("Opciones:")
                print("1. Ingresar texto a codificar.")
                print("2. Codificar en CAESAR.")
                print("3. Codificar en Vigenere.")
                print("4. Ingresar texto a decodificar.")
                print("5. Decodificar en CAESAR.")
                print("6. Salir!")
                print()
                option = int(input("Ingrese su opcion: "))

                if option==1:
                        texto_cod = input("Texto: ")
                elif option==2:
                        print("Eligio opcion Nº2")
                        caesar_text = ""
                        if texto_cod != "":
                                key = int(input("Ingrese la llave numerica para Caesar: "))
                                caesar_text = backendcrack.cod_caesar(texto_cod, key)
                                print("Su texto cifrado es: " + caesar_text)
                                input("")
                        else:
                                print("No selecciono un texto para cifrar.")
                                input("")
                elif option==3:
                        print("Eligio opcion Nº3")
                elif option==4:
                        print("Eligio opcion Nº4")
                elif option==5:
                        print("Eligio opcion Nº5")
                elif option==6:
                        print("Adios, vuelva pronto!")

menu()