from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()

    def __str__(self):
        return self.titulo
    
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.IntegerField()
    curso = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Emprestimos(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()

    def __str__(self):
        return self.livro.titulo
