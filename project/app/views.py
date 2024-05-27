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
    data = Form.objects.all()  # Retrieve the instance you want to display
    return render(request, 'show.html', {'data': data,'media_url':MEDIA_URL})

def addTocart(request,pk):
    if request.method=='POST':  
        addToCart=request.session.get('addTocart',[])
        addToCart=[]
        addToCart.append(pk)
        print(addToCart)
        request.session['addToCart']=addToCart
        form=CartForm()
        data=Form.objects.all()

        return render(request,'show.html',{'form':form,'data':data})





