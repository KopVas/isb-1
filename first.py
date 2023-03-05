def main():
    alfavit =  'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ. ,!'
    key=        'ВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБ. ,!'
    message=''
    with open("Исходный_текст_1", mode="r", encoding='utf-8') as r_file:
        message=r_file.read()
    message=message.replace("\n",'')
    itog = ''   
    for i in message.upper():
        tmp=alfavit.index(i)
        itog+=key[tmp]
    with open ("Ключ_к_тексту_1",mode='w+') as file:
        file.write(dict(zip(alfavit,key)))

    with open("Зашифрованный_текст_1",mode='w+') as file:
        file.write(itog)


if __name__=="__main__":
    main()