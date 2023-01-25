from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import *

# def index(request):
#     return render(request,'home.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('uname')
        password1 = request.POST.get('password1')
        password = request.POST.get('password')
        phone = request.POST.get('ph')
        if password == password1 :
            insert=Register(name=name,email=email,password=password1,username=username,phone=phone)
            insert.save()
            return render(request,'login.html')
        else:
            return HttpResponse('password does not match!!!!')
    return render(request,'registration.html')

def log(request):
    if request.method == 'POST':
        name = request.POST.get('nm')
        pas = request.POST.get('pass')
        user=Register.objects.filter(username=name,password=pas)
        if user:
            for user in user:
                request.session['id']=user.id
                return redirect('userhome',request.session['id'])
        else:
            error=[]
            error.append("!!!!please enter valid details!!!")
            return render(request,'login.html',{'error':error})
    return render(request,'login.html')


def userhome(request,pk):
    if 'id' in request.session:
        current_user=request.session['id']
        user=get_object_or_404(Register,id=current_user)
        return render(request,'userhome.html',{'user':user,'question':Questions.objects.all().order_by('-question')})
    else:
        return redirect('log')
    return render(request,'userhome.html')

def viewprofile(request,pk):
    if 'id' in request.session:
        profile=Register.objects.filter(id=request.session['id'])
    else:
        return redirect('log')
    return render(request,"viewprofile.html",{'user.id':request.session['id'],'profile':profile})

def logout(request):
    try:
        del request.session['id']
    except:
        return redirect('log')
    return redirect('log')


def questions(request,pk):
    n=get_object_or_404(Register,id=request.session['id'])
    if 'id' in request.session:
            if request.method == 'POST':
                insert=Questions(name=n,question=request.POST.get('nm'))
                insert.save()
    else:
        return redirect('log')
    return render(request,'questions.html',{'user.id':request.session['id'],'question':Questions.objects.filter(name=n).order_by('-question')})

def option(request,pk):
    fet=get_object_or_404(Questions,id=pk)
    if request.method=='POST':
        insert=Vote(question=fet,op1=request.POST.get('o1'))
        insert.save()
    return render(request,'option.html',{'option':Vote.objects.filter(question_id=pk),'question':fet})

def options(request,pk):
    fetch = get_object_or_404(Questions,id=pk)
    option = fetch.choices.all()
    return render(request,'like.html',{'option':option,'question':fetch})


def result(request,pk):
    user = Register.objects.get(id=request.session['id'])
    question = Questions.objects.get(id=pk)
    options = question.choices.all()
    if request.method == 'POST':
        if user == request.session['id']:
            inputvalue = request.POST['choice']
            selection_option = options.get(id=inputvalue)
            selection_option.like+=1
            selection_option.save()
    return render(request, 'result.html', {'question': question, 'options': options})

def delquestion(request,pk):
    ques=get_object_or_404(Questions,id=pk)
    if ques:
        ques.delete()
        return redirect('questions',ques.id)
    return redirect('questions',ques.id)

def deloption(request,pk):
    opt=get_object_or_404(Vote,id=pk)
    rev=opt.question.id
    if opt:
        opt.delete()
        return redirect('option',rev)
    return redirect('option',rev)
