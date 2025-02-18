from rest_framework.viewsets import ModelViewSet
from .models import Livro, Aluno, Emprestimos
from .serializers import LivroSerializer, AlunoSerializer, EmprestimosSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class EmprestimosViewSet(ModelViewSet):
    queryset = Emprestimos.objects.all()
    serializer_class = EmprestimosSerializer