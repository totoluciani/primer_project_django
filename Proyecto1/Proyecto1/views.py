from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from AppCoder.models import Curso

def saludo(request):
	dia = datetime.datetime.now() #Completar bien el comando
	return HttpResponse(f'Hola Django - Coder, hoy es {dia}')

def dia(request):
	dia = datetime.date(2000,1,1)
	return HttpResponse(f'{dia}')

def template(request):
    #EXPLICAR BIEN ESTO, BUSCAR CHATGPT Y EN DEMAS LUGARES
	#REVISAR GIT CLASE 17 CODIGO VIEJO
	# Use raw string (r'') to avoid issues with backslashes in the file path.
    template_path = open('#/index.html')

    plantilla = Template(template_path.read())

    template_path.close()

    


def template(self):

    nom = "Juan"
    ap = "Geroni"

    lista_de_notas = [1,2,2,4,5,7,7]

    dicc = {'nombre':nom,'apellido':ap,'notas':lista_de_notas}

    template = open("C:/Users/Toto/Desktop/CODERHOUSE PYTHON/PythonClase17/Primer_Project_Django/plantillas/index.html")

    plantilla = Template(template.read()) #Se carga en memoria nuestro documento, template1  

    #OJO importar template y contex, con: from django.template import Template, Context

    template.close() #Cerramos el archivo

    miContexto = Context(dicc) #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo
    

    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento


    return HttpResponse(documento)


    #MANERA MAS FACIL DE HACERLO#

    #nom = "Juan"
    #ap = "Geroni"

    #lista_de_notas = [1,2,2,4,5,7,7]

    #dicc = {'nombre':nom,'apellido':ap,'notas':lista_de_notas}

    #plantilla = loader.get_template('index.html') !!!'Se utiliza loader.get_template('<nombreTemplate>') para buscar la template en nuestra ruta ya definida en settings"!!!

    #documento = plantilla.render(dicc) !!!'Ya no se necesita contexto, poner el diccionario ya funcionaria'!!!


    #return HttpResponse(documento)

def buenavista(self):

    plantilla = loader.get_template('hola.html')

    documento = plantilla.render() #Siempre tiene que existir contexto
    return HttpResponse(documento)

def curso(self):
    curso = Curso(nombre='Desarrollo web',camada="19881")
    curso.save()
    documentoDeTexto= f"Curso: {curso.nombre}  Camada: {curso.camada}"
    
    return HttpResponse(documentoDeTexto)
