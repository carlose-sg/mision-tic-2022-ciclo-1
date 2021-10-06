# ******************************
# Analisis Reto 4
# Jun 20, 2021
# ******************************
# reto_sem_04_carlose_sanchezg.py

# Importamos la funcion reduce
from functools import reduce

# Funcion informe de servicios de acueducto.
def inforServicio(lectura : dict, tarifa : dict) -> tuple:

    # Inicializamos variables generales
    filtrar_lecturas = list()
    servicio = list()
    info_ind_predio = list()
    total = 0.0
    total_sub_consumo = 0.0
    total_sub_cargofijo = 0.0
    
    filtrar_lecturas = list(filter(validarLecturas, lectura.items()))
    servicio = liquidarServicio(filtrar_lecturas, tarifa)

    info_ind_predio = list(zip(dict(filtrar_lecturas).keys(), servicio[1]))
    try:
        total = round(reduce(lambda x, y : x + y, servicio[1]), 2)
        total_sub_consumo = round(reduce(lambda x, y : x + y, servicio[2]), 2)
        total_sub_cargofijo = round(reduce(lambda x, y : x + y, servicio[3]), 2)
    except:
        return 'Sin lecturas'

    # Retornamos el valor de la funcion
    return info_ind_predio, total, [total_sub_consumo, total_sub_cargofijo]

# Funcion para validar las lecturas
def validarLecturas(lectura : dict):

    lec_act = lectura[1]['toma_lectura'][0]['lec_actual']
    lec_ant = lectura[1]['toma_lectura'][0]['lec_anterior']
    lectura[1]['toma_lectura'][0]['consumo'] = lec_act - lec_ant
    estado = lectura[1]['estado']
    return estado == 'activo'

# Funcion para liquidar los valores del Servicio
def liquidarServicio(lectura: list, tarifa : dict) -> list:

    infoLectura = dict(lectura)
    listaConsumo = list()
    listaTotalservicio = list()
    listaTotalsubcargofijo = list()
    listaTotalsubconsumo = list()

    for registro in infoLectura.values():
        
        # Inicializamos variables para el calculo de valores del predio
        consumo = 0
        dato = registro['toma_lectura']
        estrato = registro['estrato']

        for toma_l in dato:
            consumo = toma_l['consumo']
        listaConsumo.append(consumo)

        if estrato == 1:

            sub_cargo_fijo = (tarifa['cargo_basico'] - (tarifa['cargo_basico'] * 0.45))
            listaTotalsubcargofijo.append(tarifa['cargo_basico'] * 0.45)
            sub_consumo = (tarifa['consumo'] - (tarifa['consumo'] * 0.45))

            if consumo <= tarifa['escala_sub']:
                listaTotalservicio.append(round(sub_cargo_fijo + (consumo * sub_consumo), 2))
                listaTotalsubconsumo.append(round(consumo * (tarifa['consumo'] * 0.45), 2)) 
            else:
                listaTotalservicio.append(round(sub_cargo_fijo + (tarifa['escala_sub'] * sub_consumo) + ((consumo - tarifa['escala_sub']) * tarifa['consumo']), 2))
                listaTotalsubconsumo.append(round(tarifa['escala_sub'] * (tarifa['consumo'] * 0.45), 2)) 

        elif estrato == 2:

            sub_cargo_fijo = (tarifa['cargo_basico'] - (tarifa['cargo_basico'] * 0.35))
            listaTotalsubcargofijo.append(tarifa['cargo_basico'] * 0.35)
            sub_consumo = (tarifa['consumo'] - (tarifa['consumo'] * 0.35))

            if consumo <= tarifa['escala_sub']:         
                listaTotalservicio.append(round(sub_cargo_fijo + (consumo * sub_consumo), 2))
                listaTotalsubconsumo.append(round(consumo * (tarifa['consumo'] * 0.35), 2)) 
            else:
                listaTotalservicio.append(round(sub_cargo_fijo + (tarifa['escala_sub'] * sub_consumo) + ((consumo - tarifa['escala_sub']) * tarifa['consumo']), 2))
                listaTotalsubconsumo.append(round(tarifa['escala_sub'] * (tarifa['consumo'] * 0.35), 2)) 

        elif estrato == 3:

            sub_cargo_fijo = (tarifa['cargo_basico'] - (tarifa['cargo_basico'] * 0.10))
            listaTotalsubcargofijo.append(tarifa['cargo_basico'] * 0.10)
            sub_consumo = (tarifa['consumo'] - (tarifa['consumo'] * 0.10))

            if consumo <= tarifa['escala_sub']:
                listaTotalservicio.append(round(sub_cargo_fijo + (consumo * sub_consumo), 2))
                listaTotalsubconsumo.append(round(consumo * (tarifa['consumo'] * 0.10), 2)) 
            else:
                listaTotalservicio.append(round(sub_cargo_fijo + (tarifa['escala_sub'] * sub_consumo) + ((consumo - tarifa['escala_sub']) * tarifa['consumo']), 2))
                listaTotalsubconsumo.append(round(tarifa['escala_sub'] * (tarifa['consumo'] * 0.10), 2)) 

        else: 
            # Calculamos valores para el estrato 4 y superior

            con_cargo_fijo = (tarifa['cargo_basico'] + (tarifa['cargo_basico'] * 0.40))
            con_consumo = (tarifa['consumo'] + (tarifa['consumo'] * 0.40))
            listaTotalservicio.append(round(con_cargo_fijo + (consumo * con_consumo), 2))
    
    return [listaConsumo, listaTotalservicio, listaTotalsubconsumo, listaTotalsubcargofijo]

# ------------------------------
# Llamado a la funcion desde el reto 4
# ------------------------------

print(inforServicio({
    '501001190001' :{
            'toma_lectura':  [
                {
                'lec_anterior': 1232, 
                'lec_actual': 1304, 
                }
            ], 
        'estrato': 1, 
        'estado': 'activo'
    }, 
    '501002190324' :{
            'toma_lectura':  [
                {
                'lec_anterior': 1203, 
                'lec_actual': 1230, 
                }
            ], 
        'estrato': 4, 
        'estado': 'activo'
    }
}, 
{
    'cargo_basico': 13405.45, 
    'consumo': 1100.80, 
    'escala_sub': 15
}))


# ------------------------------
# Ejemplo 1
# ------------------------------

print(inforServicio({
    '501001190001' :{
        'toma_lectura': [
            {
                'lec_anterior': 1232, 
                'lec_actual': 1304, 
            }
        ], 
        'estrato': 1, 
        'estado': 'activo'
    }, 
    '501002190324' :{
        'toma_lectura': [
            {
                'lec_anterior': 1203, 
                'lec_actual': 1230, 
            }
        ], 
        'estrato': 4, 
        'estado': 'activo'
    }
}, 
{
	'cargo_basico': 13405.45, 
	'consumo': 1100.80, 
	'escala_sub': 15
}
))


'''
# ------------------------------
# Ejemplo 2
# ------------------------------

print(inforServicio({
    '201501001' :{
            'toma_lectura':  [
                {
                'lec_anterior': 12, 
                'lec_actual': 60, 
                }
            ], 
        'estrato': 1, 
        'estado': 'activo'
    }, 
    '201501002' :{
            'toma_lectura':  [
                {
                'lec_anterior': 2, 
                'lec_actual': 6, 
                }
            ], 
        'estrato': 2, 
        'estado': 'activo'
    }, 
    '201501003' :{
            'toma_lectura':  [
                {
                'lec_anterior': 23, 
                'lec_actual': 43, 
                }
            ], 
        'estrato': 3, 
        'estado': 'activo'
    }, 
    '201501004' :{
            'toma_lectura':  [
                {
                'lec_anterior': 90, 
                'lec_actual': 120, 
                }
            ], 
        'estrato': 1, 
        'estado': 'activo'
    }, 
    '201501005' :{
            'toma_lectura':  [
                {
                'lec_anterior': 1, 
                'lec_actual': 9, 
                }
            ], 
        'estrato': 1, 
        'estado': 'inactivo'
    }, 
    '201564006' :{
            'toma_lectura':  [
                {
                'lec_anterior': 10, 
                'lec_actual': 20, 
                }
            ], 
        'estrato': 6, 
        'estado': 'activo'
    }
}, 
{
    'cargo_basico': 13405.45, 
    'consumo': 1100.80, 
    'escala_sub': 15
}
))
# ------------------------------
'''


