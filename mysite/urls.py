"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from mysite.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    # shkim
    # 홈 페이지 URL 매핑
    # HomeView.as_view() : 클래스형 뷰 형식
    # / 로 시작하는 페이지를 요청하면, (views의) HomeView 함수를 호출
    # name='home' : 해당 URL에 대해 URL 별칭 설정
    path('', HomeView.as_view(), name='home'),
]
