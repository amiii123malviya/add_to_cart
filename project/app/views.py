from django.shortcuts import render
from .forms import CartForm
from .models import Form
from project.settings import MEDIA_ROOT,MEDIA_URL
# Create your views here.
def home(request):
    my_dict ={}
    my_dict['form'] = CartForm
    return render(request,'home.html',my_dict)

def register(request):
    print(request.POST)
    print(request.FILES)
    if request.method == 'POST':
        form = CartForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            my_dict ={}
            my_dict['form']=CartForm
            my_dict['msg']="register successfull"
            return render(request, 'home.html', my_dict)
        else:
            msg = 'found some error'
            return render(request,'home.html',{'key':msg})
    return render(request,'home.html')


def showdata(request):
    data = Form.objects.all()   
    return render(request, 'show.html', {'data': data,'media_url':MEDIA_URL})

def addTocart(request,pk):
    print(pk)
    print(request)
    cart=request.session.get('cart',[])
    if pk not in cart:
        cart.append(pk)
        print(cart)        
        request.session['cart']=cart
    print(len(cart))
    data=Form.objects.all()
    print(data)
    return render(request,'cart.html',{'data':data,'media_url':MEDIA_URL})
    
        # quantity = request.session.get('quantity', [])
        # quantity1 =request.POST.get('quantity')
        # quantity.append(quantity1)
        # # print("quantity :",quantity)
        # request.session['quantity'] = quantity
        # cart = request.session.get('cart', [])
        # cart.append(pk)
        # request.session['cart'] = cart
        # form = CartForm()
        # data = Form.objects.all()
        # return render(request,'cart.html',{'form':form,'data':data})
        # return redirect('home')

def cart(request):
    cart=request.session.get('cart')
    details=[]
    total_price=0
    for i in cart:
        data1=Form.objects.get(id=i)
        con={
            'id':data1.id,
            'nm':data1.Name,
            'des':data1.Desc,
            'img':data1.Img,
            'amt':data1.Ammt
        }
        details.append(con)
        total_price+=data1.Ammt
    return render(request,'cart.html',{'data1':details,'media_url':MEDIA_URL,'total_price':total_price})




def delete(request,id):
    cart=request.session.get('cart')
    cart.remove(id)
    request.session['cart']=cart
    cart=request.session.get('cart')
    cart_detail=[]
    for i in cart:
        data1=Form.objects.get(id=i)
        con={
            'id':data1.id,
            'nm':data1.Name,
            'des':data1.Desc,
            'img':data1.Img,
            'amt':data1.Ammt

        }
        cart_detail.append(con)
    return render(request,'cart.html',{'data1':con,'media_url':MEDIA_URL})
