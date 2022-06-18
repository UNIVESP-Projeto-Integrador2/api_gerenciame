from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .models import Tarefa
from .serializers import TarefaSerializer


# from .serializers import SubtarefaSerializer


class TarefaView(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()  # serializar todos os objetos da tabela
    serializer_class = TarefaSerializer


# class SubtarefaView(viewsets.ModelViewSet):
#     queryset = Subtarefa.objects.all()  # serializar todos os objetos da tabela
#     serializer_class = SubtarefaSerializer

@api_view(['GET', 'POST'])
def tarefas_lista(request):
    if request.method == 'GET':
        tarefas = Tarefa.objects.all()
        tarefas_serializer = TarefaSerializer(tarefas, many=True)
        return JsonResponse(tarefas_serializer.data, safe=False)

    elif request.method == 'POST':
        tarefa_data = JSONParser().parse(request)
        tarefa_serializer = TarefaSerializer(data=tarefa_data)
        if tarefa_serializer.is_valid():
            tarefa_serializer.save()
            return JsonResponse(tarefa_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tarefa_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH', 'DELETE'])
def tarefas_detalhes(request, pk):
    try:
        tarefa = Tarefa.objects.get(pk=pk)
        if request.method == 'PATCH':
            tarefa_data = JSONParser().parse(request)
            tarefa_serializer = TarefaSerializer(tarefa, data=tarefa_data)
            if tarefa_serializer.is_valid():
                tarefa_serializer.save()
                return JsonResponse(tarefa_serializer.data)
            return JsonResponse(tarefa_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            tarefa.delete()
            return JsonResponse({'message': 'Tarefa apagada com sucesso.'}, status=status.HTTP_200_OK)

    except Tarefa.DoesNotExist:
        return JsonResponse({'message': 'Essa tarefa nao existe'}, status=status.HTTP_404_NOT_FOUND)


# @api_view(['DELETE'])
# def subtarefas_detalhes(request, pk, fk):
#     try:
#         subtarefa = Subtarefa.objects.get(pk=pk, fk=fk)
#         if request.method == 'DELETE':
#             subtarefa.delete()
#             return JsonResponse({'message': 'Subtarefa apagada com sucesso.'}, status=status.HTTP_200_OK)
#
#     except Subtarefa.DoesNotExist:
#         return JsonResponse({'message': 'Essa subtarefa nao existe'}, status=status.HTTP_404_NOT_FOUND)
