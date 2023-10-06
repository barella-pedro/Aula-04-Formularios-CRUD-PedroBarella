# from django.shortcuts import render,redirect
# from .models import Jogador, Estatistica, Conquista, ListaLebron, Medias_Jogadores, Lista_Usuarios

# # Create your views here.
# def home(request):
#     lebron = Jogador.objects.get(nome="Lebron")  
#     jordan = Jogador.objects.get(nome="Jordan")
#     kobe = Jogador.objects.get(nome="Kobe")  
#     lista_lebron = ListaLebron.objects.all()  
#     medias_jogadores = Medias_Jogadores.objects.all()  
#     lista_usuarios = Lista_Usuarios.objects.all()
#     return render(request, "home.html", context=      {"lista_lebron": lista_lebron, "lebron_conquistas": [lebron.conquista.frase_feito, lebron.conquista.frase_titulos, lebron.conquista.pontos_totais], "kobe_conquistas":   [kobe.conquista.frase_feito, kobe.conquista.frase_titulos,   kobe.conquista.pontos_totais],"jordan_conquistas":   [jordan.conquista.frase_feito,   jordan.conquista.frase_titulos,jordan.conquista.pontos_totais],"medias_jogadores":medias_jogadores,"lista_usuarios":lista_usuarios})

# def crie_lista(request):
#   if request.method == "POST":
#     Lista_Usuarios.objects.create(
#       top1 = request.POST["top1"],
#       top2 = request.POST["top2"],
#       top3 = request.POST["top3"]
#     )
#     return redirect ("home")
#   return render(request,"forms.html")
from django.shortcuts import render,redirect

from .models import Jogadores, Usuario, User

def home(request):
  jogador = Jogadores.objects.all()
  jogador_kobe = Jogadores.objects.get(nome_jogador="Kobe Bryant")
  jogador_lebron = Jogadores.objects.get(nome_jogador="LeBron James")
  jogador_jordan = Jogadores.objects.get(nome_jogador="Michael Jordan")
  lista_lebron = Usuario.objects.get(nome_usuario="LeBron")
  usuarios = User.objects.all()
  return render(request, "home.html",context = {"jogador":jogador,"jogador_kobe":jogador_kobe,"jogador_lebron":jogador_lebron,"jogador_jordan":jogador_jordan,"lista_lebron":lista_lebron,"usuarios": usuarios, })

def crie_lista(request):
  if request.method == "POST":
    User.objects.create(
      top1 = request.POST["top1"],
      top2 = request.POST["top2"],
      top3 = request.POST["top3"],
      usuario_nome = request.POST["nome"],
      time = request.POST["time"])
    return redirect ("home")
  return render(request,"forms.html",context={"action":"Adicione"})

def atualize_lista(request,id):
  rank = User.objects.get(id=id)
  if request.method == "POST":
    rank.top1 = request.POST["top1"]
    rank.top2 = request.POST["top2"]
    rank.top3 = request.POST["top3"]
    rank.usuario_nome = request.POST["nome"]
    rank.time = request.POST["time"]
    rank.save()
    return redirect ("home")
  return render(request,"forms.html", context={"action":"Atualize","rank":rank})

def delete_lista(request,id):
  rank = User.objects.get(id=id)
  if request.method == "POST":
    if "confirm"in request.POST:
      rank.delete()
    return redirect ("home")
  return render(request,"are_you_sure.html", context={"rank":rank})