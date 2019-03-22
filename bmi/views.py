from django.shortcuts import render

# Create your views here.

#CRUD+L
# list -.Create -> update ->

#뷰 : 뷰는 오똔 기능 단위, 로직을 처리하는 함수 혹은 클래스를 의미합니다.
#뷰 : ->하나의 주소에 연결된 하나의 페이지
#화면에 나타나는 뷰 ㅣ 템프릿과 세트로 작업

#화면에 나타나지 않는 뷰 ㅣ 뷰만 단독, Json ,XML


# 함수형 뷰 : def 함수로 만든 뷰
#내가 마음대로 할수있음 : 내가 알아서 해야함
# 클래스형 뷰 :  class로 만든 뷰
#원래 많이 사용 하는 형태의 뷰를 상속받아서 사용
# 크ㅜㄹ랴수횽 뷰가 상속받는 것 ? : 재내락 뷰
#detail, list, edit


#1. 파이썬 빌트인 모듈
#2. 장고 관련 모듈
#3. 그외 가타 모듈
#4. 내가 만든 모듈

from django.views.generic.list import ListView
#자세하게 쓰는 것을 권장
from .models import BMI

class BMIList(ListView):
    model =  BMI

from django.views.generic.edit import UpdateView,CreateView, DeleteView
class BMIUpdate(UpdateView):
    model = BMI
    fields = ['name', 'height', 'weight']
    template_name = 'bmi/bmi_update.html'
    success_url = '/'

class BMICreate(CreateView):
    model = BMI
    fields = ['name', 'height', 'weight']
    template_name = 'bmi/bmi_create.html'

class BMIDelete(DeleteView):
    model = BMI
    template_name = 'bmi/bmi_delete.html'
    success_url = '/'

from django.views.generic.detail import DetailView
class BMIDetail(DetailView):
    model = BMI
    template_name = 'bmi/bmi_detail.html'



