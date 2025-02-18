from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from livraria.views import LivroViewSet, AlunoViewSet, EmprestimosViewSet

router = DefaultRouter()
router.register(r'livros', LivroViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'emprestimos', EmprestimosViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]