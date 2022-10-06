from django.urls import path

from blog import views


# URL 네임스페이스 설정
app_name = 'blog'

urlpatterns = [
    # Post 상세페이지 URL 매핑
    # /blog/post/99/
    # <int: > : 정수형 숫자 매핑
    # post/[정수형 숫자]로 시작하는 페이지를 요청하면, 해당 정수형 숫자를 pk에 저장하고, PostDV 클래스 뷰를 호출
    # <int: > : 정수형 숫자 매핑
    # 예를 들어, 만일 http://localhost:8000/post/2/ 페이지가 요청되면
    # 여기에 등록한 매핑 룰에 의해 http://localhost:8000/post/<int:pk>/ 가 적용되어,
    # pk 에 2가 저장되고, PostDV 클래스 뷰도 실행.
    # name='post_detail' : 해당 URL에 대해 URL 별칭 설정
    path('post/<int:pk>/', views.PostDV.as_view(), name='post_detail'),
]