from operations import Operations


def menu():
    option = 0
    operationsObject = Operations()
    while option != 6:
        print('Lenguajes Formales de programacion, Hector Ponsoy')
        print('----- Menu -----')
        print('1. Cargar menú' + '\n2. Cargar orden' + '\n3. Generar menú' +
              '\n4. Generar factura' + '\n5. Generar árbol' + '\n6. Salir')
        print('Opcion: ', end='')
        option = input()
        
        if option == '1':
            print('Cargando menu...')
            operationsObject.uploadOrder()

        elif option == '2':
            print('Cargando orden')
            
        elif option == '3':
            print('Generando menú')
            operationsObject.threeOption()
        elif option == '4':
            print('Generando factura')
        elif option == '5':
            print('Generando árbol')
        elif option == '6':
            print('Saliendo....')
            option = 6
        else:
            print('Opcion invalida')


menu()
'''
[["restaurante='Restaurante LFP'\n"], 
    ["'Bebidas'  :\n"], 
    ["[bebida_1;'Bebida #1';11.;'DescripciÃ³n Bebida 1'    ]\n"], 
    ["[ bebida_2;'Bebida #2';10.50;    'DescripciÃ³n Bebida 2']\n"], 
    ['\n'], 
    ["'Desayunos':\n"], 
    ["[d1;'Desayuno 1';45.00;'DescripciÃ³n Desayuno 1']\n"], 
    ["[d2 ;'Desayuno 2';    40.   ;'DescripciÃ³n Desayuno 2']\n"], 
    ["[d3;'Desayuno 3';35;'DescripciÃ³n Desayuno 3']\n"], 
    ['\n'], 
    ["'  Postres':\n"], 
    ["[   pos_001;'Postre 1'   ;25;'DescripciÃ³n Postre 1']\n"]]
'''