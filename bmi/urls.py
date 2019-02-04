from django.urls import path
from .views import *

urlpatterns = [
    # 1.url pattern
    # 2. view
    # 3. 1번 유알엘 pattern 의 이름
    # path
    path('', BMIList.as_view(), name='bmi_list'),
    path('update/<int:pk>/', BMIUpdate.as_view(), name='bmi_update'),
    path('create/', BMICreate.as_view(), name='bmi_create'),
    path('delete/<int:pk>/', BMIDelete.as_view(), name='bmi_delete'),
    path('detail/<int:pk>/', BMIDetail.as_view(), name='bmi_detail'),
    # BMIList.as_view()

]