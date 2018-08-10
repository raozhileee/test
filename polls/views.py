# -*-coding:utf-8-*-
from django.shortcuts import render
from	django.shortcuts	import	render,	get_object_or_404,redirect

from	django.http	import	HttpResponse
from .models import Question,Choice

def	index(request):
	#return	HttpResponse("Hi!	这是polls应用的首页。")
	qlist=Question.objects.order_by('-pub_date')[:5]
	#clist=Choice.objects.all()
	context={'q':qlist}
	return render(request,'polls/index.html',context)

def	hello(request):
	return	render(request,'polls/index.html')

def detail(request,question_id):
	#return HttpResponse('wen ti %s' % question_id)
	question = get_object_or_404(Question, pk=question_id)
	return render(request,'polls/detail.html',{'q':question})

def result(request,question_id):
	#return HttpResponse('result %s' % question_id)
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/result.html', {'q': question})
def resultall(request):
	qlist = Question.objects.order_by('-pub_date')[:5]
	context = {'q': qlist}
	return render(request, 'polls/resultall.html', context)

def vote(request):
	#return HttpResponse('votes %s' % question_id)
	question = get_object_or_404(Question, pk=request.POST['question_id'])
	choices=question.choice_set.get(pk=request.POST['choice'])
	choices.votes+=1
	choices.save()
	#return render(request, 'polls/vote.html', {'q': question})
	return redirect(result,question_id=request.POST['question_id'])

def vote1(request):
	for i in range(1,4):
		question = get_object_or_404(Question, pk=i)
		choices=question.choice_set.get(pk=request.POST['choice'+str(i)])
		choices.votes+=1
		choices.save()
	return redirect('resultall')

def home(request):
	return render(request,'polls/home.html')

def login(request):
	username=request.POST.get('username')
	password = request.POST.get('pwd')
	if username == 'bob' and password == '123456':
		request.session['IS_LOGIN']=True
		return redirect('index')
	return redirect('home')

def protected(request):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        return HttpResponse('OK')
    return redirect('home')

def test(request):
	x=1
	y=[1,2]
	z={'one':1,'two':2}
	return render(request, 'polls/test.html',{'x':x,'y':y,'z':z})