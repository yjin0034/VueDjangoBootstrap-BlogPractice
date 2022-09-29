# 클래스형 뷰 형식

from django.views.generic import TemplateView


# 홈 페이지 관련 뷰 클래스
class HomeView(TemplateView):
    # 해당 뷰 클래스에 관련 템플릿 파일(home.html) 지정
    template_name = 'home.html'
