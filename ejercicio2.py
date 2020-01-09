
def manejoEquipaje():
    numeroBultos = int(input("Por favor ingrese el número de bultos :"))
    tablaBultos = []
    precioKilo = 0
    tablaPrecioKilo = []
    totalBultos = 0
    bultoPesado = 0
    bultoLiviano = 500
    pesoPromedio = 0
    while numeroBultos > 0:
        pesoBulto = int(input("Ingrese el peso de cada Bulto :"))
        if pesoBulto < 500:
            tablaBultos.append(pesoBulto)
            # tablaPrecioKilo.append(precioKilo)
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

    for j in tablaBultos:
        if j > bultoPesado:
            bultoPesado = j
        elif j < bultoLiviano:
            bultoLiviano = j
        pesoPromedio += j / len(tablaBultos)

    return ["Valores Peso Tabla : ",
            tablaBultos,
            "Valores precio : ",
            tablaPrecioKilo,
            ["Numero de bultos totales ",
             len(tablaBultos),
             "Bulto menor peso ",
             bultoLiviano,
             "Bulto mayor peso ",
             bultoPesado,
             "Peso promedio "
             pesoPromedio]
            ]


print(manejoEquipaje())
