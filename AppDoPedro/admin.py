from django.contrib import admin
# from .models import Jogador, Estatistica, Conquista, ListaLebron, Medias_Jogadores,Lista_Usuarios

# admin.site.register(ListaLebron)
# admin.site.register(Jogador)
# admin.site.register(Estatistica)
# admin.site.register(Conquista)
# admin.site.register(Medias_Jogadores)
# admin.site.register(Lista_Usuarios)

from .models import Jogadores, Usuario, Userlist

admin.site.register(Jogadores)
admin.site.register(Usuario)
admin.site.register(Userlist)