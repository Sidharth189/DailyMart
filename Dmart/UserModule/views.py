from django.shortcuts import render,redirect
from adminpanel.models import productdb,categorydb
from .models import contactdb
from .models import userdb,cartdb,shippingaddressdb
from django.core.paginator import Paginator
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
def userindex(request):
    catdata=categorydb.objects.all()
    if('username' in request.session):
        uid=request.session['uid']
        cartcount=cartdb.objects.filter(user=uid,status=0).count()
        gtotal=cartdb.objects.filter(user=uid,status=0).aggregate(Sum('total'))['total__sum']
        return render(request,'userindex.html',{'catdata':catdata,'cartcount':cartcount,'carttotal':gtotal})
    else:
        return render(request,'userindex.html',{'catdata':catdata})

def shopgrid(request):
    catdata=categorydb.objects.all()
    prodata=productdb.objects.all()
    procount=productdb.objects.count()
    latestproduct=productdb.objects.all().order_by('-id')[:9]
    return render(request,'shop-grid.html',{'catdata':catdata,'prodata':prodata,'procount':procount,'latpro':latestproduct})

def contactpage(request):
    return render(request,'contact.html')

def contact(request):
    if request.method=='POST':
        cname=request.POST['name']
        cemail=request.POST['email']
        cmsg=request.POST['msg']
        data=contactdb(cname=cname,cemail=cemail,cmsg=cmsg)
        data.save()
        return redirect('contactpage')

def userreg(request):
    return render(request,'user_reg.html')

def userlogin(request):
    return render(request,'user_login.html')

def registration(request):
    if request.method=='POST':
        uname=request.POST['username']
        email=request.POST['email']
        phone=request.POST['phno']
        password=request.POST['password']
        cpass=request.POST['cpass']
        if(password==cpass):
            data=userdb(uname=uname,email=email,phno=phone,password=password)
            data.save()
            return redirect('userlogin')


def login(request):
    if request.method=='POST':
        uname=request.POST['username']
        password=request.POST['password']
        if userdb.objects.filter(uname=uname,password=password).exists():
            data = userdb.objects.filter(uname=uname,password=password).values('uname','id').first()
            request.session['username']=uname
            request.session['uid']=data['id']
            return redirect('userindex')
        else:
            return render(request,'user_login.html',{'msg':'Invalid user'})

def logout(request):
    del request.session['username']
    return redirect('userindex')

def productdetails(request,id):
    data=productdb.objects.filter(id=id)
    return render(request,'productdetails.html',{'data':data})
            
def shopcart(request):
    if 'username' in request.session:
        uid=request.session['uid']
        catdata=categorydb.objects.all()
        cartdata=cartdb.objects.filter(user=uid,status=0)
        gtotal=cartdb.objects.filter(user=uid,status=0).aggregate(Sum('total'))['total__sum']
        return render(request,'shop-cart.html',{'catdata':catdata,'cartdata':cartdata,'gtotal':gtotal})
    else:
        return redirect('userlogin')

def addtocart(request,id):
    if 'username' in request.session:
        if request.method=='POST':
            quantity=request.POST['quantity']
            price=request.POST['price']
        total1=(int(quantity)*float(price))
        username=request.session['username']
        data=cartdb(user=userdb.objects.get(uname=username),product=productdb.objects.get(id=id),total=total1,quantity=quantity)
        data.save()
        return redirect('shopcart')
    else:
        return render(request,'user_login.html',{'msg':'Login to continue'})

def removecart(request,id):
    cartdb.objects.filter(id=id).delete()
    return redirect('shopcart')

def checkoutpage(request):
    uid=request.session['uid']
    data=cartdb.objects.filter(user=uid,status=0)
    gtotal=cartdb.objects.filter(user=uid,status=0).aggregate(Sum('total'))['total__sum']
    return render(request,'checkout.html',{'data':data,'total':gtotal})

def checkout(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        country=request.POST['country']
        street=request.POST['street']
        building=request.POST['building']
        city=request.POST['city']
        state=request.POST['state']
        zipcode=request.POST['zipcode']
        phone=request.POST['zipcode']
        email=request.POST['mail']
        notes=request.POST['notes']
    uid=request.session['uid']
    checkoutdata=shippingaddressdb(user=userdb.objects.get(id=uid),fname=fname,lname=lname,country=country,street=street,building=building,city=city,state=state,zipcode=zipcode,phone=phone,email=email,notes=notes)
    checkoutdata.save()
    cartdb.objects.filter(user=uid).update(status=1)
    return render(request,'checkout.html',{'msg':'Order placed !! Thank You'})


@csrf_exempt
def cartupdate(request):
    if request.method=="POST":
        cartid=request.POST['pid']
        q=request.POST['qty']
        p=request.POST['price']
        t=float(q)*float(p)
        print(t)
        cartdb.objects.filter(id=cartid).update(total=t,quantity=q)
        return HttpResponse()

def searchpage(request):
    catdata=categorydb.objects.all()

    return render(request,'search.html',{'catdata':catdata})

def search(request):
    prod = None
    query = None
    catdata=categorydb.objects.all()
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = productdb.objects.all().filter(Q(pname__contains=query) | Q(pdescr__contains=query))

    return render(request, 'search.html', {'q': query, 'pr': prod,'catdata':catdata})

        


