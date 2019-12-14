#Para filtros:
#Opcion 1 en view.py:
#Datos=DatosPersonales.objects.filter(Nombre="Mike")
#
#Opcion 2 en template:
#{% for object in Alumnos%}
#   {% ifequal object.Nombre "Willy" %}
#       <p>{{object.Nombre}}</p>
#  	{% endifequal  %}
#{% endfor %}
#
#Opcion 3:
#En view.py:
#def res(request):
     #Datos=DatosPersonales.objects.all()
     #Datos1=DatosPersonales.objects.filter(Nombre="Mike")
     #return render(request, "Alumnos/resultado.html",{"Alumnos":Datos,"Alumnos1":Datos1})
#En template:
#{% for object in Alumnos1 %}
  #<p>{{object.Nombre}}</p>
#{% endfor %}
