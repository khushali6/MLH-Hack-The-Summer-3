from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from app.models import Profile,Post,LikePost,Comment
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='signin')
def index(request):
    user_profile=Profile.objects.get(user=request.user)
    allPost= Post.objects.all().order_by('-created_at')
    return render(request,'index.html',{'user_profile':user_profile,'allPost': allPost})

def upload(request):
    non_inclusive_word=["guys","mankind","ladies","gentleman","man","men","businessman"]
    if request.method=='POST':
        user = request.user.username
        post_text=request.POST['postData']
        if post_text=="":
            messages.info(request,'Cannot Be Empty')
            return redirect('/')
            
        else:
            if 'man' in post_text:
                messages.info(request,'Please use inclusive words')
                return redirect('/') 
            else:
                post_model=Post.objects.create(user=user,text=post_text)
                post_model.save()
                return redirect('/')
    else:
        return redirect('/')


def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                #Log user in and redirect to settings page
                user_login=auth.authenticate(username=username,password=password)
                auth.login(request,user_login)

                #create a Profile object for new user
                user_model=User.objects.get(username=username)
                new_profile=Profile.objects.create(user=user_model,uid=user_model.id)
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request,'Password Do not match')
            return redirect('signup')



    else:
        return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('signin')

    else:
        return render(request,'signin.html')

@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def settings(request):
    user_profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
        if request.FILES.get('image')==None:
            image=user_profile.profile_img
            bio=request.POST['bio']
            location=request.POST['location']

            user_profile.profile_img=image
            user_profile.bio=bio
            user_profile.location=location
            user_profile.save()
        if request.FILES.get('image')!=None:
            image=request.FILES.get('image')
            bio=request.POST['bio']
            location=request.POST['location']

            user_profile.profile_img=image
            user_profile.bio=bio
            user_profile.location=location
            user_profile.save()
        return redirect('settings')
    return render(request,'setting.html',{'user_profile':user_profile})

def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes+1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes-1
        post.save()
        return redirect('/')


def comment(request):
    if request.method=='POST':
        user_profile=request.user.username
        comment_text=request.POST['comment']
        if comment_text!="":
            comment_model=Comment.objects.create(user=user_profile,text=comment_text)
            comment_model.save()
            return redirect('/')
    else:
        return render(request,'comment.html')
        




    

