from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Nota
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def lista_notas(request):
    notas = Nota.objects.filter(usuario=request.user)
    contexto = {'notas': notas}
    return render(request, 'lista.html', contexto)

@login_required
def detalle_nota(request, nota_id):
    nota = get_object_or_404(Nota, pk=nota_id, usuario=request.user)
    return render(request, 'detalle.html', {'nota': nota})

@login_required
def crear_nota(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()
        contenido = request.POST.get("contenido", "").strip() 

        if not titulo:
            return render(request, "formulario.html", {
                "error": "El título es obligatorio",
                "titulo": titulo,
                "contenido": contenido,
                "accion": "crear",
            })

        nota = Nota.objects.create(
            titulo=titulo,
            contenido=contenido,
            usuario=request.user
        )
        return HttpResponseRedirect(reverse("notas:detalle_nota", args=(nota.id,)))

    return render(request, "formulario.html", {"accion": "crear"})

@login_required
def editar_nota(request, nota_id):
    nota = get_object_or_404(Nota, pk=nota_id, usuario=request.user)

    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()
        contenido = request.POST.get("contenido", "").strip()

        if not titulo:
            return render(request, "formulario.html", {
                "error": "El título es obligatorio",
                "nota": nota,
                "accion": "editar",
            })

        nota.titulo = titulo
        nota.contenido = contenido
        nota.save()
        return HttpResponseRedirect(reverse("notas:detalle_nota", args=(nota.id,)))

    return render(request, "formulario.html", {"nota": nota, "accion": "editar"})

@login_required
def eliminar_nota(request, nota_id):
    nota = get_object_or_404(Nota, pk=nota_id, usuario=request.user)
    nota.delete()
    return HttpResponseRedirect(reverse("notas:lista_notas"))
