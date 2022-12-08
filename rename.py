import os
i=1
j=1
k=1
flag=0
numero_stagione=input("-- Welcome --\n\nInsert the number of the tv season following this format (01; 02; etc..): ")
estensione=input("Insert the extension of the files following this format (mkv; mp4; etc..): ")
print("\n\n-- DEFAULT ORDER --\nIndex   Name of the file")
lista_nomi = []
lista_ordine = []
lista_rinomine = []
for x in sorted(os.listdir('./')):
    if(str(x)!=str(os.path.basename(__file__))):
        lista_nomi.append(x)
        print(f'{j})    {x}')
        j+=1
scelta=input("\n\n-- MENU --\n1) Correct sort, start to rename file \n2) Not correct sort, start manual sorting\n3) Exit\nNumber of choice: ")
if(int(scelta)==1):
    for x in lista_nomi:
        if(i<=9):
            nuovo_nome=f'S{numero_stagione}:E0{i}.{estensione}'
            if(str(nuovo_nome) in lista_nomi):
                flag+=1
        else:
            nuovo_nome=f'S{numero_stagione}:E{i}.{estensione}'
            if(str(nuovo_nome) in lista_nomi):
                flag+=1 
        i+=1
    if(flag!=0):
        print("\n\nFile with the new name are already existing, process exited")
    else:
        i=1
        for x in lista_nomi:
            if(i<=9):
                os.popen(f'mv "{x}" S{numero_stagione}:E0{i}.{estensione}')
            else:
                os.popen(f'mv "{x}" S{numero_stagione}:E{i}.{estensione}')     
            i+=1     
        print("\n\nProcess completed succesfully")
elif(int(scelta)==2):
    print('\n')
    cicli=len(lista_nomi)
    while(k<=cicli):
        ordine=input(f'Insert the index of the {k} file to rename: ')
        lista_ordine.append(ordine)
        k+=1
    for x in lista_ordine:
        rename=lista_nomi[int(x)-int(1)]
        if(i<=9):
            nuovo_nome=f'S{numero_stagione}:E0{i}.{estensione}'
            if(str(nuovo_nome) in lista_nomi):
                flag+=1
        else:
            nuovo_nome=f'S{numero_stagione}:E{i}.{estensione}'
            if(str(nuovo_nome) in lista_nomi):
                flag+=1    
        i+=1
    if(flag!=0):
        print("\n\nFile with the new name are already existing, process exited")
    else:
        i=1
        for x in lista_ordine:
            rename=lista_nomi[int(x)-int(1)]
            if(i<=9):
                os.popen(f'mv "{rename}" S{numero_stagione}:E0{i}.{estensione}')
            else:
                os.popen(f'mv "{rename}" S{numero_stagione}:E{i}.{estensione}')     
            i+=1
        print("\n\nProcess completed succesfully")
else:
    print("\n\nExited")