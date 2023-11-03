from django.shortcuts import render
from mysite.models import Post,Function,Function1,Function2
from datetime import datetime
from django.shortcuts import redirect
# Create your views here.
def homepage(request):
    selected_menu = request.GET.get('menu','home') #預設
    posts=Post.objects.all()
    if selected_menu == "home":
        abc=Post.objects.all()
    elif selected_menu == "qa":
        abc=Function1.objects.all()
    elif selected_menu == "activity":
        abc=Function2.objects.all()
    elif selected_menu == "rule":
        abc=Function.objects.all()
    now=datetime.now()
    return render(request,'index.html',{'selected_menu': selected_menu, 'abc': abc})

def showpost(request,slug):
    try:
        post = Post.objects.get(slug=slug)
        return render(request, 'post.html', {'post': post})
    except Function1.DoesNotExist:
        return redirect("/") 
   
def function1(request, slug):
    try:
        book = Function1.objects.get(slug2=slug)
        return render(request, 'qa.html', {'book': book})
    except Function1.DoesNotExist:
        return redirect("/") 
    
def function2(request, slug):
    try:
        act = Function2.objects.get(slug3=slug)
        return render(request, 'activity.html', {'act': act})
    except Function1.DoesNotExist:
        return redirect("/") 
    
def function(request, slug):
    try:
        ru = Function.objects.get(slug1=slug)
        return render(request, 'rule.html', {'ru': ru})
    except Function.DoesNotExist:
        return redirect("/") 
    

'''
function1=Function1.objects.all()
    return render(request,'qa.html',locals())

    try:
        book = Book1.objects.get(name=book_name)
        return render(request, 'book.html', {'book': book})
    except Book1.DoesNotExist:
        return redirect("/") 
'''