
def manejoEquipaje():
    numeroBultos = int(input("Por favor ingrese el número de bultos :"))
    tablaBultos = []
    tablaPrecioKilo = []
    precioKilo = 0    
    totalBultos = 0
    bultoPesado = 0
    bultoLiviano = 0
    pesoPromedio = 0
    while numeroBultos > 0:
        pesoBulto = int(input("Ingrese el peso de cada Bulto :"))
        if pesoBulto < 500:
            tablaBultos.append(pesoBulto)
        else:
            print('El peso del bulto excede el peso requerido')
        numeroBultos -= 1

    for i in tablaBultos:
        if i <= 25:
            precioKilo = 0
        elif i > 25 and i < 300:
            precioKilo = 1500
        else:
            precioKilo = 2500
        tablaPrecioKilo.append(precioKilo)
        pesoPromedio += i / len(tablaBultos)
        
    bultoLiviano = min(tablaBultos)
    bultoPesado = max(tablaBultos) 
    totalBultos = len(tablaBultos)

    print("Valores Peso Tabla : \n" , tablaBultos)  
    print("Valores Precio : \n" , tablaPrecioKilo)
    print("Numero de bultos totales : \n" , totalBultos)
    print("Bulto mayor peso : \n" , bultoPesado)
    print("Bulto menor peso : \n" , bultoLiviano)
    print("Peso promedio : \n", pesoPromedio )

manejoEquipaje()
