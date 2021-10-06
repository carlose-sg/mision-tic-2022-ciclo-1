# ******************************
# Analisis Reto 3
# Jun 09, 2021
# ******************************
# reto_sem_03_carlose_sanchezg.py

def calcularInforme(creditos : dict)-> list:

    # Guardamos todos los items del diccionario
    datosUsuarios = creditos.items()

    # Se definen variables para los totales del informe
    totGenPagada = 0
    totGenMora = 0
    totGenElaborada = 0

    # Se define variable para el retorno de la funcion
    valRetornar = ''

    # Iniciamos el recorrido de todo el diccionario
    for usuario, datos in datosUsuarios:

        # Cargamos en variables los datos del usuario
        codUsuario = usuario
        nomUsuario = datos['nombres']
        apeUsuario = datos['apellidos']
        # Estado del credito
        estCredito = datos['est_credito']

        # Cargamos la informacion detallada del credito del usuario
        idCredito = datos['credito'][0]['id_credito']
        cuotasCred = datos['credito'][0]['cuotas']
        valorCred = datos['credito'][0]['valor']
        intCred = datos['credito'][0]['interes']
        # Numero de cuotas vencidas
        cuotasVenc = datos['credito'][0]['cuo_vencidas']
        # Contador de cuotas vencidas
        contCuotasVenc = cuotasVenc
        # Numero de cuotas pagadas
        cuotasPaga = datos['credito'][0]['cuo_pagadas']
        # Contador de cuotas pagadas
        contCuotasPaga = cuotasPaga

        # Creamos variables para los totales del credito
        totPagada = 0
        totMora = 0
        totElaborada = 0

        # Contador de numero de cuotas
        numCuota = 1
        # Calculamos el valor de la cuota mensual del credito
        valorCuota = valorCred / cuotasCred
        # Cargamos el saldo inicial del credito
        saldoCred = valorCred
        # Se define variable para almacenar el estado de la cuota
        estCuota = ''

        # Se genera la amortizacion mensual del credito
        while numCuota <= cuotasCred:
            
            # Calculamos el valor del interes para la cuota
            valorInt = saldoCred * intCred
            # Calculamos el valor de la cuota mensual a pagar con interes
            valorPagoMes = valorCuota + valorInt
            # Calculamos el nuevo saldo del credito
            saldoCred = saldoCred - valorCuota

            # Definimos el estado de la cuota en el siguiente orden:
            # 1. Cuotas Pagadas, 2. Cuotas En Mora, 3. Cuotas Elaboradas

            if contCuotasPaga > 0:
                # Cuota Pagada
                estCuota = 'Pagada'
                # Se actualiza el contador de cuotas pagadas
                contCuotasPaga -= 1
                # Se actualiza el total de cuotas pagadas
                totPagada = totPagada + valorPagoMes
            else:
                if contCuotasVenc > 0:
                    # Cuota En Mora
                    estCuota = 'En Mora'
                    # Se actualiza el contador de cuotas en mora
                    contCuotasVenc -= 1
                    # Se actualiza el total de cuotas en mora
                    totMora = totMora + valorPagoMes
                else:
                    # Cuota Elaborada
                    estCuota = 'Elaborada'
                    # Se actualiza el total de cuotas elaboradas
                    totElaborada = totElaborada + valorPagoMes

            # Impresion de control con la informacion de la cuota del credito
            # print('Cuota No.: ', numCuota)
            # print('Valor Cuota: ', valorCuota)
            # print('Valor Interes: ', valorInt)
            # print('Valor a Pagar: ', valorPagoMes)
            # print('Saldo del Credito: ', saldoCred)
            # print('Estado Cuota: ', estCuota)

            # Actualizamos el contador de la cuota
            numCuota += 1

        # Impresion de control de los totales del credito
        # print(totPagada, totMora, totElaborada)

        # Validamos si el credito ya ha sido pagado completamente para no incluirlo en el informe
        if estCredito != 'Pagado':

            # Se actualizan los totales generales del reporte de creditos
            totGenPagada += totPagada
            totGenMora += totMora
            totGenElaborada += totElaborada

            # Se actualiza la variable a retornar con los datos del usuario
            valRetornar = valRetornar + codUsuario + ';' + nomUsuario[0:3] + ';' + apeUsuario[0:3] + ';'

    # Se ajusta la variable a retornar de la funcion
    valRetornar = valRetornar[0:len(valRetornar)-1]
    # print(valRetornar)

    # Se genera una tupla con los totales de los creditos para el reporte
    tuplaValores = (round(totGenPagada, 2), round(totGenMora, 2), round(totGenElaborada, 2))
    # print(tuplaValores)

    # Se retorna el valor de la funcion
    return list((valRetornar, tuplaValores))


# Se hace el llamado a la funcion con los diccionarios de pruebas

# Prueba No. 1
'''
print(
calcularInforme(
{
'2015020192098' :{
'nombres': 'Juan',
'apellidos': 'Arias Ruiz',
'est_credito': 'Activo',
'credito': [
{
'id_credito': 'C0198238',
'cuotas': 24,
'valor': 3066936.00,
'interes': 0.020,
'cuo_vencidas': 8,
'cuo_pagadas':10
}
]
}
}
)
)
'''

# Prueba No. 2
'''
print(
calcularInforme(
{
'2015020192098' :{
'nombres': 'Juan',
'apellidos': 'Arias Ruiz',
'est_credito': 'Activo',
'credito': [
{
'id_credito': 'C0198238',
'cuotas': 24,
'valor': 3066936.00,
'interes': 0.020,
'cuo_vencidas': 8,
'cuo_pagadas':10
}
]
}
}
)
)
'''

# Prueba No. 3
print(
calcularInforme(
{
'2018015647382' :{
'nombres': 'Luis Antonio',
'apellidos': 'Lopez Rueda',
'est_credito': 'Activo',
'credito': [
{
'id_credito': 'C0013453',
'cuotas': 60,
'valor': 87558500,
'interes': 0.020,
'cuo_vencidas': 30,
'cuo_pagadas':7
}
]
},
'2019041209845' :{
'nombres': 'Elias',
'apellidos': 'Diaz Lopez',
'est_credito': 'Activo',
'credito': [
{
'id_credito': 'C0335501',
'cuotas': 3,
'valor': 87558,
'interes': 0.020,
'cuo_vencidas': 1,
'cuo_pagadas':2
}
]
}
}
)
)
