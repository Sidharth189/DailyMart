from django.shortcuts import render,redirect
from .models import categorydb
from .models import productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from UserModule.models import userdb,contactdb,cartdb
from django.db.models import Sum
# Create your views here.
def loginpage(request):
    return render(request,'loginpage.html')

def adminindex(request):
    if 'username' in request.session:
        productcount=productdb.objects.count()
        categorycount=categorydb.objects.count()
        sales=cartdb.objects.filter(status=1).aggregate(Sum('total'))['total__sum']
        usercount=userdb.objects.count()
        return render(request,'index.html',{'pcount':productcount,'catcount':categorycount,'usercount':usercount,'sales':sales})
    else:
        return redirect('loginpage')

def addcategorypage(request):
    if 'username' in request.session:
        return render(request,'addcategory.html')
    else:
        return redirect('loginpage')

def addcategory(request):
    if request.method=='POST':
        cname=request.POST['catname']
        cdescr=request.POST['catdescr']
        data=categorydb(name=cname,descr=cdescr)
        data.save()
        return redirect('addcategorypage')
        
def viewcategory(request):
    if 'username' in request.session:
        data=categorydb.objects.all()
        return render(request,'viewcategorypage.html',{'data':data})
    else:
        return redirect('loginpage')

def deletecategory(request,id):
    data=categorydb.objects.filter(id=id).delete()
    return redirect('viewcategory')

def editcategorypage(request,id):
    if 'username' in request.session:
        data=categorydb.objects.filter(id=id)
        return render(request,'editcategory.html',{'data':data})
    else:
        return redirect('loginpage')

def editcategory(request,id):
    if request.method=='POST':
        cname=request.POST['catname']
        cdescr=request.POST['catdescr']
        categorydb.objects.filter(id=id).update(name=cname,descr=cdescr)
        return redirect('viewcategory')

def addproductpage(request):
    if 'username' in request.session:
        data=categorydb.objects.all()
        return render(request,'addproduct.html',{'data':data})
    else:
        return redirect('loginpage')

def addproduct(request):
    if request.method=='POST':
        pname=request.POST['proname']
        pdescr=request.POST['prodescr']
        price=request.POST['proprice']
        img=request.FILES['proimg']
        pcategory=request.POST['procategory']
        data=productdb(pname=pname,pdescr=pdescr,price=price,pimg=img,pcategory=pcategory)
        data.save()
        return redirect('addproductpage')

def viewproduct(request):
    if 'username' in request.session:
        data=productdb.objects.all()
        return render(request,'viewproduct.html',{'data':data})
    else:
        return redirect('loginpage')

def editproductpage(request,id):
    if 'username' in request.session:
        select=categorydb.objects.all()
        data=productdb.objects.filter(id=id)
        return render(request,'editproduct.html',{'data':data,'select':select})
    else:
        return redirect('loginpage')

def editproduct(request,id):
    if request.method=='POST':
        pname=request.POST['proname']
        pdescr=request.POST['prodescr']
        price=request.POST['proprice']
        pcategory=request.POST['procategory']
        try:
            img=request.FILES['proimg']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=productdb.objects.get(id=id).img
            
        productdb.objects.filter(id=id).update(pname=pname,pdescr=pdescr,price=price,pimg=file,pcategory=pcategory)
        return redirect('viewproduct')

def deleteproduct(request,id):
    productdb.objects.filter(id=id).delete()
    return redirect('viewproduct')



def adlogin(request):
    username_a = request.POST.get('username')
    password_a = request.POST.get('password')
    if User.objects.filter(username__contains=username_a).exists():
        user = authenticate(username=username_a,password=password_a)
        if user is not None:
            login(request,user)
            request.session['username'] = username_a
            request.session['password'] = password_a
            print(user)
            return redirect('adminindex')
        else:
            return render(request,'loginpage.html',{'msg':'invalid user!!'})
    else:
        return redirect('adlogin')

def adlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect('loginpage')

def feedback(request):
    data=contactdb.objects.all()
    return render(request,'feedback.html',{'data':data})

def deletefeedback(request,id):
    contactdb.objects.filter(id=id).delete()
    return redirect('feedback')







