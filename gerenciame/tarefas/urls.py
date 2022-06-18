from django.conf.urls import url
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tarefas', views.TarefaView)  # quando acessarmos site/tarefas, vai aparecer a lista
# router.register('tarefas/subtarefas', views.SubtarefaView)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^api/tarefas$', views.tarefas_lista),  # tarefas get
    #    url(r'^api/tarefas$', ), # tarefas post
    #    url(r'^api/tarefas/(?P<pk>[0-9]+)$', ), # tarefas patch
    url(r'^api/tarefas/(?P<pk>[0-9]+)$', views.tarefas_detalhes),  # tarefa delete
    # url(r'^api/tarefas/(?P<pk>[0-9]+)/subtarefas/(?P<pk>[0-9]+)$', views.subtarefas_detalhes)  # subtarefa delete
]
