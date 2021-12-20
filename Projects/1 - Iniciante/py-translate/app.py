from translate import Translator
from interface import logo, menu, mostrar_formatado
from time import sleep


def traduzir(f,t,texto):    

    translator = Translator(from_lang=f, to_lang=t)
    result = translator.translate(texto)
    return result


logo()
menu()

op = int(input())

if op == 0:        
    logo()
    print("OBRIGADO POR USAR NOSSOS SERVIÇOS")
    
elif(op == 1):
    logo()
    traduz = traduzir("portuguese","english",input("Informe o texto a ser traduzido: "))
    
elif(op == 2):        
    logo()
    traduz = traduzir("english","portuguese",input("Informe o texto a ser traduzido: "))
    

mostrar_formatado(traduz)
    
