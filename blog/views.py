from django.views.generic import DetailView

from blog.models import Post


# Post 상세페이지 관련 클래스 뷰
# DetailView를 상속받음
class PostDV(DetailView):
    # 대상 모델(테이블) 지정  # blog/models.py의 Post 모델
    model = Post
    # 해당 클래스 뷰에 관련 템플릿 파일(blog/post_detail.html) 지정
    template_name = 'blog/post_detail.html'