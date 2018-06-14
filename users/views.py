from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def logout_view(request):
    '''注销'''
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    '''注册'''
    if request.method !='POST':
        #显示空的注册表单
        form = UserCreationForm()
    else:
        #处理优势局的表单
        form =UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            print('new_user.name:'+new_user.username)
            print('new_user.password:' + request.POST['password1'])
            #让用户自动登陆，并重定向到主页
            authenticated_user = authenticate(username= new_user.username,
                                              password= request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context ={'form':form}
    return render(request,'users/register.html',context)
