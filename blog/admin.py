from django.contrib import admin

from blog.models import Post, Category, Tag, Comment


# Post 모델을 Admin 페이지에 등록
@admin.register(Post)
# Post 모델에 세부 기능을 추가할, PostAdmin 클래스 생성
class PostAdmin(admin.ModelAdmin):
    # 목록 뷰에 표시되는 컬럼을 설정
    # id, category, tags ... 등의 컬럼 표시
    list_display = ('id', 'category', 'tag_list', 'title', 'description', 'image', 'create_dt', 'update_dt', 'like')

    # list_display는l ManyToManyField는 사용할 수 없다는 에러에 대한 대처. 즉, list_display에 tags 필드(컬럼)를 못 쓴다는 말.
    # ERRORS: <class 'blog.admin.PostAdmin'>: (admin.E109) The value of 'list_display[2]' must not be a ManyToManyField.
    # tags 컬럼명을 직접쓰는 대신, tag_list라는 메서드를 만들어 list_display에서 사용한다.
    # tat_list 메서드는 Post 객체의 모든 태그(obj.tags.all())에 대해 태그의 이름(t.name)들을 ','로 이어 붙인(','.join()) 값을 반환하도록 만들었다.
    # obj : Post 모델의 객체
    def tag_list(self, obj):
        return ','.join([t.name for t in obj.tags.all()])

    # 데이터베이스에 대한 쿼리 횟수를 줄여 성능에 도움을 주기 위한 코드
    # get_queryset 메서드를 오버라이딩
    def get_queryset(self, request):
        # .prefetch_related 메서드를 사용해, 테이블로부터 Post 레코드들을 가져올 때 관련된 태그 테이블의 레코드도 같이 가져오게 함
        return super().get_queryset(request).prefetch_related('tags')


# Category 모델을 Admin 페이지에 등록
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


# Tag 모델을 Admin 페이지에 등록
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


# Comment 모델을 Admin 페이지에 등록
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'short_content', 'create_dt', 'update_dt')
