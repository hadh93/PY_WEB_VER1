from django.views.generic.base import TemplateView

from django.views.generic.edit import CreateView
# CreateView 는 테이블에 데이터를 생성하기 위해 필요한 폼을 보여주고,
# 폼의 입력을 받아서 테이블에 데이터를 생성해주는 뷰입니다.
# (CreateView 처럼 데이터를 추가, 수정, 삭제할 수 있는 뷰는
# UpdateView, DeleteView 등이 있습니다.)

from django.contrib.auth.forms import UserCreationForm

# UserCreationForm은 User 모델의 객체를 생성하기 위해 보여주는
# 폼입니다. 장고에서 기본 제공하는 뷰.

from django.core.urlresolvers import reverse_lazy

# reverse_lazy() 함수는 뷰가 성공적으로 테이블에 데이터를 추가했을때 사용자를 특정 URL로 이동시킬 수 있다.
# ex) 회원가입이 성공적으로 완료되면 reverse_lazy() 함수로
# 사용자를 인덱스 페이지로 보낼지 어디로 보낼지 코딩할 수 있음.

class IndexView(TemplateView):
    template_name = 'index.html'

class UserCreateView(CreateView): # import한 CreateView를 상속받습니다.
    template_name = 'registration/register.html'
    # UserCreateView는 작동되면,
    # 사용자에게 register.html 템플릿을 보여줄 것입니다.
    # (해당 템플릿에는 회원가입 폼을 나타낼 겁니다)

    form_class = UserCreationForm
    # register.html 에 회원가입 시킬 수 있는 장고의 기본제공 폼인
    # UserCreationForm을 사용하기 위해서
    # form_class 속성에 UserCreationForm을 지정합니다.

    success_url = reverse_lazy('register_done')
    # register_done 이라는 url 패턴 name을 만들어서
    # 사용자를 회원가입 완료 메시지를 보여줄 페이지로 이동시킬 예정입니다.

class UserCreateDoneTV(TemplateView):
    # 회원가입이 완료되면 사용자를 특정페이지로 이동시키게 만들어줄 뷰 인
    # UserCreateDoneTV 뷰를 정의합니다.

    template_name = 'registration/register_done.html'
    # 회원가입이 완료되면 사용자에게 register_done.html 페이지가
    # 보여지게 할 것입니다.
