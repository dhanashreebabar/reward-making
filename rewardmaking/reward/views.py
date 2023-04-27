from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from . models import Task,TaskLinks
from django.contrib import messages
from django.db.models import Count
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.models import User, auth

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Task.objects.get(user=user_object)
    task_links = TaskLinks.objects.get(user=user_object)
    if request.method == "POST":
        task1 = request.POST.get('task1')
        if task1:
            task_links.task1 =task1
        task2 = request.POST.get('task2')
        if task2:
            task_links.task2 =task2   
        task3 = request.POST.get('task3')    
        if task3:
            task_links.task3=task3 
        task4 = request.POST.get('task4')    
        if task4:
            task_links.task4 =task4           
        # task_completed = Task.objects.create(task_complete)
        task_links.save()      
        task_complete = request.POST.get('task_complete')
        if task_complete:
            user_profile.task_complete =task_complete
        # task_completed = Task.objects.create(task_complete)
            user_profile.save()   
        return redirect('/')
    
           
    account_balance=user_profile.account_balance
    if task_links.task1 :
        account_balance -=20
    if task_links.task2 ==True:
        account_balance -=20
    if task_links.task3 ==True:
        account_balance -=20
    if task_links.task4 ==True:
        account_balance -=20
    # if user_profile.task_complete==True:
    #      account_balance +=200

    status = TaskLinks.objects.filter(
        Q(user=user_object)&
        Q(task1='True')&
        Q(task2='True')&
        Q(task3='True')&
        Q(task4='True')
    
        )   
    if status:
        user_profile.status = 'Complete '
        account_balance +=200
        
    context = {
        'user_object': user_object,
        'user_profile':user_profile,
        'account_balance': account_balance,
        'task_links':task_links
        
    }
    return render(request,'home.html',context)

def SignupPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken")
            return redirect('home')

        if pass1!=pass2:
            return HttpResponse("your password and confirm password are not same!!!")
        else:
            my_user=User.objects.create_user(username,email,pass1)
            my_user.save()
            user_login = auth.authenticate(username=username, password=pass1)
            auth.login(request, user_login)
            user_model = User.objects.get(username=request.user.username)
            new_profile = Task.objects.create(user=user_model)
            new_profile2 = TaskLinks.objects.create(user=user_model)

            new_profile.save()
            new_profile2.save()

            return redirect('login')

    return render(request,'signup.html')

def LoginPage(request):
    # if request.method=='POST':
    #     username = request.POST.get('username')
    #     pass1 = request.POST.get('pass')
    #     user=authenticate(request,username=username,password=pass1)
    #     if user is not None:
    #         login(request,user)
    #         return redirect('home')
    #     else:
    #         return HttpResponse('Username And Password Are Not Matching')

    # return render(request,'login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    else:
        return render(request, 'login.html')


@login_required(login_url='signin')
def search(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Task.objects.get(user=user_object)
    task_links = TaskLinks.objects.get(user=user_object)

    if request.method == 'POST':
        username = request.POST['username']
        username_object = User.objects.filter(username__icontains=username)

        username_profile = []
        username_profile_list = []

        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_lists = Profile.objects.filter(id_user=ids)
            username_profile_list.append(profile_lists)
        
        username_profile_list = list(chain(*username_profile_list))
    return render(request, 'search.html', {'user_profile': user_profile, 'username_profile_list': username_profile_list})

def LogoutPage(request):
    logout(request)
    return redirect('login')
