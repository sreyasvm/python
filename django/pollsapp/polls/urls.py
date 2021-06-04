from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('onboard/',views.onboard,name='onboard'),
    path('<str:tenant_id>/insert',views.insert_for_tenant,name='tenant_insert'),
    path('<str:tenant_id>/',views.tenant_index,name='tenant_index'),
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/results/',views.results,name='results'),
    path('<int:question_id>/vote/',views.vote,name='vote'),
]