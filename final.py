#Función para la obtención de datos del usuario, regresándolos en forma de array
def get_data():
    print('1.Ingrese su edad: ')
    edad=int(input())
    print('2.Ingrese su altura en cm: ')
    altura=int(input())
    print('3.Ingrese su peso en kg: ')
    peso=int(input())
    print('4.Ingrese su género [H/M]: ')
    gen=input()
    print('4.Presión sistólica: ')
    ps=int(input())
    print('5.Presión diástolica: ')
    pd=int(input())
    print('6.Nivel de colesterol: ')
    col=int(input())
    print('7.Nivel de glucosa: ')
    gluc=int(input())
    print('9.¿Fuma? [S/N]: ')
    fum=input()
    print('10.¿Consume alcohol? [S/N]: ')
    alco=input()
    print('11.¿Se ejercita cotidianamente? [S/N]: ')
    ejer=input()
    return [edad,altura,peso,gen,ps,pd,col,gluc,fum,alco,ejer]

#Función para categorizar el tipo colesterol, de acuerdo con el valor ingresado 
#por el usuario, de acuerdo a los niveles sugeridos por American Heart Association
def prueba_col(colest):
    if colest<200:
        return 1
    elif colest>=200 and colest<240:
        return 2
    else:
        return 3


def prueba_glucosa(gluc):
    if gluc<110:
        return 1
    elif gluc>=110 and gluc<130:
        return 2
    else:
        return 3

def tabaco(f):
    if f=='s' or f=='S':
        return 1
    else:
        return 0

def ejerc(f):
    if f=='s' or f=='S':
        return 1
    else:
        return 0

def alcoh(f):
    if f=='s' or f=='S':
        return 1
    else:
        return 0

def genero(f):
    if f=='M' or f=='m':
        return 2
    else:
        return 1

def IMC(alt,pes):
    return round((pes*10000)/(alt**2),2)

#Función para conversión de datos para realizar el predict con el modelo
def prueba_datos(data):
    edad=data[0]
    altura=data[1]
    peso=data[2]
    ps=data[4]
    pd=data[5]
    col_fin=prueba_col(data[6])
    glu_fin=prueba_glucosa(data[7])
    tab_fin=tabaco(data[8])
    ejer_fin=ejerc(data[10])
    alco_fin=alcoh(data[9])
    gen_final=genero(data[3])
    imc_fin=IMC(altura,peso)
    return [[edad,gen_final,altura,peso,ps,pd,col_fin,glu_fin,
                tab_fin,alco_fin,ejer_fin,imc_fin]]

def analisis_resultado(prueba):
    a=prueba[0]
    if a[-1]<18.5:
        print('Su IMC={} indica que tiene bajo peso.'.format(a[-1]))
    elif a[-1]>=18.5 and a[-1]<25:
        print('Su IMC={} indica que su peso es normal.'.format(a[-1]))
    elif a[-1]>=25 and a[-1]<30:
        print('Su IMC={} indica que tiene sobrepeso.'.format(a[-1]))
    else:
        print('Su IMC={} indica que tiene obesidad.'.format(a[-1]))
    
    if a[6]==1:
        print('Su nivel de colesterol está en un rango normal.')
    elif a[6]==2:
        print('Su nivel de colesterol está en un rango medio, lo ideal es menor a 200 mg/dl.')
    else:
        print('Su nivel de colesterol es elevado, lo ideal es menor a 200 mg/dl.')
    
    if a[7]==1:
        print('Su nivel de glucosa está en un rango normal.')
    elif a[7]==2:
        print('Su nivel de glucosa está en un rango medio, lo ideal es menor a 110 mg/dl.')
    else:
        print('Su nivel de glucosa es elevado, lo ideal es menor a 110 mg/dl.')

#MAIN
import pickle
modelo = pickle.load(open('Datos/modelo_fin.sav', 'rb'))
datos=get_data()
prueba_final=prueba_datos(datos)
resul_prob=modelo.predict_proba(prueba_final)

prob1=resul_prob[0][1]
print('Tiene una probabilidad de {}% de desarrollar una enfermedad cardiovascular'
         .format(round(prob1*100,2)))
print('Más información: ')
analisis_resultado(prueba_final)
