from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from django.shortcuts import render, reverse, redirect
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


# 로그인
@require_POST
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_url = request.POST.get('next') or reverse('home')
            return redirect(next_url)
        else:
            context = {
                'message': "계정정보를 찾을 수 없습니다.",
                "return_url": request.POST.get('next') or reverse('home')
            }
            return render(request, 'message.html', context)


# 로그아웃
def logout(request):
    auth_logout(request)
    return redirect('home')


# 회원가입
@require_POST
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            next_url = request.POST.get('next') or reverse('home')
            return redirect(next_url)
        else:
            meseege = ""
            for error in form.errors:
                meseege += str(error)+"\n"
                meseege += str(form.errors[error])+"\n"
            context = {
                'message': "회원가입에 실패하엿습니다.\n"+meseege,
                'return_url': request.POST.get('next') or reverse('home')
            }
            return render(request, 'message.html', context)


# 프로필
@require_GET
@login_required
def profile(request):
    return render(request, "detail.html")


# 프로필 수정
@require_http_methods(['GET', 'POST'])
@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            context = {
                "message": "정상적으로 수정하였습니다.",
                "return_url": reverse("accounts:profile")
            }
            return render(request, "message.html", context)
        else:
            return render(request, 'update.html', {"form": form})
    else:
        return render(request, "update.html")


@require_http_methods(['GET', 'POST'])
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            context = {
                "message": "비밀번호가 정상적으로 변경하였습니다.",
                "return_url": reverse("home")
            }
            return render(request, "message.html", context)
        else:
            return render(request, 'change_password.html', {"form": form})
    else:
        return render(request, 'change_password.html')


@login_required
def profile_delete(request):
    request.user.delete()
    auth_logout(request)
    context = {
        "message": "정상적으로 탈퇴하였습니다.",
        "return_url": reverse("home")
    }
    return render(request, "message.html", context)



