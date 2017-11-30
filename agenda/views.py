# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from models import ItemAgenda
from forms import FormItemAgenda

def index(request):
    lista_itens = ItemAgenda.objects.all()
    return render(request, "lista.html",
                    {'lista_itens':lista_itens})

def adiciona(request):
    if request.method == 'POST': # Formulário enviado
        form = FormItemAgenda(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        # Exibe formulário em branco
        form = FormItemAgenda()
    return render(request, "adiciona.html",
                    {'form': form})

def item(request, nr_item):
    item = get_object_or_404(ItemAgenda, pk = nr_item)
    form = FormItemAgenda(request.POST or None,
                            request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("/")

    return render(request, "item.html", {'form': form})

def remover(request, nr_item):
    item = get_object_or_404(ItemAgenda, pk = nr_item)
    if request.method == "POST":
        # parent_obj_url = obj.content_object.get_absolute_url()
        item.delete()
        # messagens.success(request,"Removido com sucesso!")
        return redirect("/")

    return render(request, "remover.html", {'item': item})
