from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Nota
from django.urls import reverse

def lista_notas(request):
    notas = Nota.objects.all()
    contexto = {'notas': notas}
    return render(request, 'lista.html', contexto)


def detalle_nota(request, nota_id):
    nota = get_object_or_404(Nota, pk=nota_id)
    return render(request, 'detalle.html', {'nota': nota})


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

        nota = Nota.objects.create(titulo=titulo, contenido=contenido)
        return HttpResponseRedirect(reverse("notas:detalle_nota", args=(nota.id,)))

    return render(request, "formulario.html", {"accion": "crear"})


def editar_nota(request, nota_id):
    nota = get_object_or_404(Nota, pk=nota_id)

    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()
        contenido = request.POST.get("contenido", "").strip()

        if not titulo:
            return render(request, "formulario.html", {
                "error": "El título es obligatorio",
                "nota": nota,
                "accion": "editar",
            })

        Nota.objects.filter(pk=nota_id).update(titulo=titulo, contenido=contenido)
        return HttpResponseRedirect(reverse("notas:detalle_nota", args=(nota.id,)))

    return render(request, "formulario.html", {"nota": nota, "accion": "editar"})


def eliminar_nota(request, nota_id):
    """
    Elimina la nota directamente (sin plantilla de confirmación)
    """
    nota = get_object_or_404(Nota, pk=nota_id)
    nota.delete()
    return HttpResponseRedirect(reverse("notas:lista_notas"))
