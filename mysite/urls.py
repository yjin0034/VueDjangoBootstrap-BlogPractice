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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from mysite.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    # 홈 페이지 URL 매핑
    # HomeView.as_view() : 클래스형 뷰 형식
    # / 로 시작하는 페이지를 요청하면, (views의) HomeView 클래스 뷰를 호출
    # name='home' : 해당 URL에 대해 URL 별칭 설정
    path('', HomeView.as_view(), name='home'),
    # blog/ 로 시작하는 페이지를 요청하면, blog/urls.py 파일의 매핑 정보를 읽어서 처리하도록 함
    path('blog/', include('blog.urls')),
]

# 사이트에 업로드한 미디어 파일을 불러오기 위한 코드
# (장고가 제공하는) static 함수에 의해서, (settings 파일에서 정의한) MEDIA_URL이 들어오면 MEDIA_ROOT로 정의한 폴더에서 해당 미디어 파일을 찾아 처리하게 됨
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)