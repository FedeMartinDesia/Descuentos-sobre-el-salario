import pandas as pd

#descuentos sobre el salario original en porcentajes
descuento_jubilacion=0.10
descuento_obrasocial=0.20
descuento_cuotasindical=0.03
descuento_ganancias=0.35

#creo una funcion que recibe como parametro el sueldo original
#y devuelve el sueldo "neto" luego de haberle aplicado cada descuento
#si la persona gana mas de 10000 tiene un descuento adicional
def calculo_sueldoneto(sueldo_bruto):
    sueldo_neto=sueldo_bruto-(sueldo_bruto*descuento_jubilacion)
    sueldo_neto=sueldo_neto-(sueldo_bruto*descuento_obrasocial)
    sueldo_neto=sueldo_neto-(sueldo_bruto*descuento_cuotasindical)
    
    if (sueldo_bruto>=100000):
        sueldo_neto=sueldo_neto-(sueldo_bruto*descuento_ganancias)
        
    return sueldo_neto


    
mis_empleados=pd.read_excel("C:\\Users\\PC\\Documents\\DataScience\\Basico\\Datasets\\MuestraTarjetaX2019.xlsx",engine='openpyxl')

mis_empleados=mis_empleados[['IDFIJO','PROVINCIA','INGRESOS','Sexo']]



#uso apply para aplicar la funcion que cree mas arriba a cada celda de la columna sueldo del dataframe
#el resultado se guardara en una nueva columna sueldo neto
mis_empleados['sueldo_neto']=mis_empleados['INGRESOS'].apply(
    calculo_sueldoneto
    )

mis_empleados.to_excel('C:\\Users\\PC\\Documents\\DataScience\\Basico\\Datasets\\mis_empleados.xlsx')