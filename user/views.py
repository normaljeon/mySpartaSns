from django.shortcuts import render, redirect
# redirect는 성공시 로그인(/sign-in) 화면으로 넘기는 역할
from .models import UserModel
from django.http import HttpResponse
# 사용자가 데이터베이스 안에 있는지 검사하는 함수
from django.contrib.auth import get_user_model
from django.contrib import auth
# 사용자가 꼭 로그인이 되었을 때만 접근할 수 있게 함
from django.contrib.auth.decorators import login_required

def sign_up_view(request):
    if request.method == "GET":
        user = request.user.is_authenticated
        if user:
            # ①tweet/urls.py 와 ②tweet/views.py 의 def home(request)에서 관리하는 경로
            return redirect('/')
        else:
            return render(request, 'user/signup.html')
    elif request.method == "POST" :
        username = request.POST.get('username', '')   # ..., None) 옵션은 빈값을 허용안함
        password = request.POST.get('password', '')   # ..., None) 옵션은 빈값을 허용안함
        password2 = request.POST.get('password2', '') # ..., None) 옵션은 빈값을 허용안함
        bio = request.POST.get('bio', '')             # ..., None) 옵션은 빈값을 허용안함
        # bio = request.POST.get('bio', None)

        # me = UserModel.objects.get(username=username)
        # exist_user = UserModel.objects.filter(username=username)

        # exist_user = get_user_model().objects.filter(username=username)
        # if exist_user: # 사용자가 있을 경우
        #     return render(request, 'user/signup.html')

        if password != password2:
            # [에러처리] 패스워드가 같지 않다고 알람
            return render(request, 'user/signup.html',{'error' : '패스워드를 확인 해주세요!'})
        else:
            # [에러처리] 필수값 2개가 입력되지 않았을 때
            if username == '' or password == '':
                return render(request, 'user/signup.html', {'error' : '사용자 이름과 비밀번호는 필수값 입니다.'})
            # [에러처리] 동일한 username이 있을 때
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html', {'error' : '사용자가 존재합니다.'})
            else:
                # new_user = UserModel()
                # new_user.username = username
                # new_user.password = password
                # new_user.bio = bio
                # new_user.save() # DB에 저장
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                return redirect('/sign-in')

def sign_in_view(request):
    if request.method == "POST":
        username = request.POST.get('username', '')  # ..., None) 옵션은 빈값을 허용안함
        password = request.POST.get('password', '')  # ..., None) 옵션은 빈값을 허용안함

        # 유저가 존재하는지 찾기
        # me = UserModel.objects.get(username=username)
        me = auth.authenticate(request, username=username, password=password)

        # if me.password == password:
        if me is not None:
            # request.session['user'] = me.username
            auth.login(request, me)
            # return HttpResponse("로그인 성공!" + '\n' + me.username)
            return redirect('/')
        else:
            # [에러처리] 로그인 실패
            # return redirect('/sign-in') 에러로그를 보여주기 위하여 render로 구현
            return render(request, 'user/signin.html', {'error':'유저이름 혹은 패스워드를 확인 해주세요.'})

    elif request.method == "GET":
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signin.html')

@ login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

# user/views.py
@login_required
def user_view(request):
    if request.method == 'GET':
        # 사용자를 불러오기, exclude와 request.user.username 를 사용해서 '로그인 한 사용자'를 제외하기
        user_list = UserModel.objects.all().exclude(username=request.user.username)
        return render(request, 'user/user_list.html', {'user_list': user_list})

@login_required
def user_follow(request, id):
    me = request.user
    click_user = UserModel.objects.get(id=id)
    if me in click_user.followee.all():
        click_user.followee.remove(request.user)
    else:
        click_user.followee.add(request.user)
    return redirect('/user')















