from django.urls import path, include
from data_test import views
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('empresas/clientes', views.CompanyClientsViewSet, basename='empresasclientes')
router.register('empresas/rentaunasemana', views.getCompaniesWithRentsOver1WeekViewSet, basename='empresasrentaunasemana')
router.register('empresas/clientesmenorgastos', views.getClientsWithLessExpenseViewSet, basename='empresasclientesmenorgastos')
router.register('clientes/ranking', views.newClientRankingiewSet, basename='clientesranking')

router.register('clientes/cantidad/<int:company>/', views.getClientsSortByAmountViewSet, basename='clientescantidad')

router.register('clientes', views.ClientesViewSet)
router.register('empresas', views.EmpresasViewSet)
router.register('arriendos', views.ArriendosViewSet)

urlpatterns = [
    path('clientes2/cantidad/<int:company>/', views.getClientsSortByAmountView.as_view()),
    path('', include(router.urls))
]