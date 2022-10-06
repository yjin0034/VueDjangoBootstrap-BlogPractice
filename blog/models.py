# blog 앱에서 필요한 테이블들을 정의

from django.db import models


# 포스트 모델(테이블)
class Post(models.Model):
    # 카테고리 모델을 속성으로 연결
    # models.ForeignKey('Category', ) : Category 모델을 외래키로 연결
    # on_delete=models.SET_NULL : 연결된 테이블(Category)의 해당 레코드가 삭제되는 경우, 해당 테이블(Post) 레코드의 해당 컬럼(category)을 NULL로 채우라는 의미
    # blank=True, null=True : 해당 컬럼의 값으로 공백값(null, '')이 저장되는 것을 허용
    # blank=True와 null=True의 차이
    # blank=True : 필드가 폼(입력 양식)에서 empty한 상태로 저장되는 것을 허용한다. DB column에 해당 값은 빈 폼의 형태, 즉 ''로 저장됨
    # null = True : DB column에 해당 값은 null로 저장됨
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    # 태그 모델을 속성으로 연결
    # Tag 모델을 ManyToManyField 관계로 연결. 다대다(N:N) 관계
    tags = models.ManyToManyField('Tag', blank=True)
    # 제목 컬럼
    # models.CharField('TITLE', ) : 해당 컬럼들의 별칭으로 임의로 지정해 줌
    # 최대 50자
    title = models.CharField('TITLE', max_length=50)
    # 한 줄 요약 컬럼
    # models.CharField('DESCRIPTION', ) : 해당 컬럼들의 별칭으로 임의로 지정해 줌
    # CharField인 경우, null=True를 설정하지 않는 것이 좋다. 그 이유는, 값이 존재하지 않으면 null이 아닌 ''(empty string)이 저장되게 하기 위해
    # help_text='simple one-line text.' : 해당 컬럼에 대한 설명문 작성
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple one-line text.')
    # 이미지 컬럼
    # upload_to='blog/%Y/%m/' : 해당 이미지 파일이 저장될 디렉터리의 경로 지정
    image = models.ImageField('IMAGE', upload_to='blog/%Y/%m/', blank=True, null=True)
    # 내용 컬럼
    content = models.TextField('CONTENT')
    # 작성 일시 컬럼
    # auto_now_add=True : django model이 최초 저장(insert) 시에만 현재 날짜(date.today())를 적용
    create_dt = models.DateTimeField('CREATE DT', auto_now_add=True)
    # 수정 일시 컬럼
    # auto_now=True : django model이 save될 때마다 현재 날짜(date.today()) 로 갱신
    update_dt = models.DateTimeField('UPDATE DT', auto_now=True)
    # 좋아요 기능 컬럼
    # default=0 : 컬럼이 생성될 때 해당 컬럼에 값이 주어지지 않으면, 값을 0으로 채워줌
    like = models.PositiveSmallIntegerField('LIKE', default=0)

    # __str__ 메서드(string 메서드)
    def __str__(self):
        return self.title  # 제목 표시

# 카테고리 모델(테이블)
class Category(models.Model):
    # 이름 컬럼
    # unique=True : 중복된 값이 생기지 않도록 설정
    name = models.CharField(max_length=50, unique=True)
    # 한 줄 요약 컬럼
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple one-line text.')

    def __str__(self):
        return self.name  # 이름 표시

# 태그 모델(테이블)
class Tag(models.Model):
    # 이름 컬럼
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name  # 이름 표시

# 댓글 모델(테이블)
class Comment(models.Model):
    # 포스트 모델을 속성으로 연결
    # models.ForeignKey('Category', ) : Category 모델을 외래키로 연결
    # on_delete=models.CASCADE : Post 테이블의 레코드가 삭제되면, Comment 테이블의 레코드도 삭제되도록 설정
    # models.ForeignKey(Post, ) : 앞에서 Post 테이블이 정의되어 있는 경우 이와 같이 따옴표를 붙이지 않고 Post라고 작성해도 된다.
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    # 내용 컬럼
    content = models.TextField('CONTENT')
    # 작성 일시 컬럼
    create_dt = models.DateTimeField('CREATE DT', auto_now_add=True)
    # 수정 일시 컬럼
    update_dt = models.DateTimeField('UPDATE DT', auto_now=True)


    # 파이썬의 @property 문법을 사용해 메서드를 필드로 정의
    @property
    # 댓글 내용으로부터 10글자를 가져오는 short_content 메서드 정의
    def short_content(self):
        # 댓글(content) 내용으로부터 10글자만 가져온다.
        return self.content[:10]

    # Comment 모델에는 title이나 name과 같은 컬럼이 없어서, 임의의 메서드를 직접 정의해서 사용할 것이다.
    def __str__(self):
        # 직접 정의한 short_content 메서드(필드)를 string 메서드에 사용
        return self.short_content  # 댓글의 내용(댓글 내용의 10글자) 표시