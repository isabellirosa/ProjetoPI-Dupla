from rest_framework.serializers import ModelSerializer
from .models import Livro, Aluno, Emprestimos

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class EmprestimosSerializer(ModelSerializer):
    class Meta:
        model = Emprestimos
        fields = '__all__'