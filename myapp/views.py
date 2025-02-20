from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.core.mail import send_mail
import random
from django.conf import settings    
# import razorpay
from django.core.paginator import Paginator

# Create your views here.


# def fun(request):
#     return HttpResponse("hello python")

def about(request):
    return render(request,"about.html")   
 
# def blog_details(request):
#     return render(request,"blog_details.html")

#def blog(request):
    #return render(request,"blog.html")

def checkout(request):
    uid=user.objects.get(email=request.session['email'])
    aid=add_to_cart.objects.filter(user_id=uid)
    
    l1=[]
    sub_total=0
    total=0
    for i in aid:
        l1.append(i.total)
    sub_total=sum(l1)  
    total=sub_total 
    discount=0 

    amount = total*100 #100 here means 1 dollar,1 rupree if currency INR
    # client = razorpay.Client(auth=('rzp_test_bilBagOBVTi4lE','77yKq3N9Wul97JVQcjtIVB5z'))
    # response = client.order.create({'amount':amount,'currency':'INR','payment_capture':1})
    # print(response,"")

    contaxt={
        "aid":aid,
        "sub_total":sub_total,
        "total":total,
        "discount":discount,
    }
    return render(request,"checkout.html",contaxt)

def contact(request):
    return render(request,"contact.html")

def index(request):
    if "email" in request.session:
        return render(request,"index.html")
    else:
        return render(request,"login.html")


def main(request):
    return render(request,"main.html")

#def shop_details(request,id):
    #sp_id=product.objects.get(id=id)
    #sid=size.objects.all()
    #contaxt={
     #   "sp_id":sp_id,
      #  "sid":sid,
    #}
    #return render(request,"shop_details.html",contaxt)

def shop_details(request, product_id):
    product_obj = product.objects.filter(id=product_id).first()  # Get the first matching product or None
    
    if not product_obj:
        return render(request, "shop_details.html", {"error": "Product not found"})  # Pass an error message

    return render(request, "shop_details.html", {"sp_id": product_obj})
def add_to_wishlist(request,id):
    uid=user.objects.get(email=request.session['email'])
    pid=product.objects.get(id=id)
    show1=wishlist.objects.filter(user_id=uid,product_id=pid).exists()
    
    if show1:
        return redirect("shop")
    else:
    
        wishlist.objects.create(user_id=uid,
                                product_id=pid,
                                image=pid.img,
                                name=pid.name,
                                price=pid.price)    
        
        return redirect("shop")


def blog(request):
    # Fetch blog posts from your database
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog.html', context)

def blog_details(request):
    # Here you might fetch a single blog post. Adjust according to your URL parameters.
    # For example, if you change the URL to include an id:
    # def blog_details(request, id):
    #     blog_post = get_object_or_404(Blog, id=id)
    #     return render(request, 'blog_details.html', {'blog': blog_post})
    return render(request, 'blog_details.html')




def shop(request):
    pid=product.objects.all()
    mid=main_category.objects.all()
    bid=branding.objects.all()
    fid=prize.objects.all()
    cid=color.objects.all()
    sid=size.objects.all()
    uid=user.objects.get(email=request.session['email'])
    show1=wishlist.objects.filter(user_id=uid)
    wl1=[]
    for i in show1:
        wl1.append(i.product_id.id)
    print(wl1)
    f_id=request.GET.get("f_id")
    print(f_id)

    s_id=request.GET.get("s_id")
    print(s_id)

    b_id=request.GET.get("b_id")
    print(b_id)
    
    m_id=request.GET.get("m_id")
    print(m_id)

    c_id=request.GET.get("color_id")
    print(c_id)

    sb_id=request.GET.get("sb_id")
    print(sb_id)

    

    if m_id:
        pid=product.objects.filter(main_category=m_id)
    elif b_id:
        pid=product.objects.filter(branding_id=b_id)    
    elif f_id:
        pid=product.objects.filter(prize_id=f_id)    
    elif c_id:
        pid=product.objects.filter(color_id=c_id)    
    elif s_id:
        pid=product.objects.filter(size_id=s_id)
    elif sb_id == "ATOZ":
        pid=product.objects.order_by("name")  
    elif sb_id == "ZTOA":
        pid=product.objects.order_by("-name")
    elif sb_id == "LTOH":
        pid=product.objects.order_by("price") 
    elif sb_id == "HTOL":
        pid=product.objects.order_by("-price")                       
    else:
        pid=product.objects.all()

    

    paginator=Paginator(pid,3)
    page_number=request.GET.get("page")
    pid=paginator.get_page(page_number)
    contaxt={

        "pid":pid,
        "mid":mid,
        "bid":bid,
        "fid":fid,
        "cid":cid,
        "sid":sid,
        "wl1":wl1,

    }
    return render(request,"shop.html",contaxt)











def shopping_cart(request):
    uid=user.objects.get(email=request.session['email'])
    aid=add_to_cart.objects.filter(user_id=uid)
    l1=[]
    sub_total=0
    total=0
    for i in aid:
        l1.append(i.total)
    sub_total=sum(l1)  
    total=sub_total  
    # amount = total*100 #100 here means 1 dollar,1 rupree if currency INR
    # client = razorpay.Client(auth=('rzp_test_bilBagOBVTi4lE','77yKq3N9Wul97JVQcjtIVB5z'))
    # response = client.order.create({'amount':amount,'currency':'INR','payment_capture':1})
    # print(response,"")
    contaxt={
        "aid":aid,
        "sub_total":sub_total,
        "total":total,
        # "response":response,
        "uid":uid,
    }

    return render(request,"shopping_cart.html",contaxt)



def add_cart(request,id):
    pid=product.objects.get(id=id)
    print(pid)
    uid=user.objects.get(email=request.session['email'])
    aid=add_to_cart.objects.filter(product_id=pid,user_id=uid).exists()
    if aid:
        aid=add_to_cart.objects.get(product_id=pid,user_id=uid)
        aid.qty+=1
        aid.total=aid.qty*aid.price
        aid.save()
    else:
        add_to_cart.objects.create(user_id=uid,product_id=pid,img=pid.img,name=pid.name,price=pid.price,qty=1,total=pid.price)
    return redirect("shopping_cart")


def cart_delete(request,id):
    aid=add_to_cart.objects.get(id=id)
    aid.delete()
    return redirect("shopping_cart")

def cart_plus(request,id):
    aid=add_to_cart.objects.get(id=id)
    aid.qty+=1
    aid.total=aid.qty*aid.price
    aid.save()
    return redirect("shopping_cart")

def cart_minus(request,id):
    try:
        aid=add_to_cart.objects.get(id=id)
        aid.qty-=1
        aid.total=aid.qty*aid.price
        aid.save()
        if aid.qty==0:
            aid.delete()
        return redirect("shopping_cart")
    except:
        return redirect("not found")

















def login(request):
    if "email" in request.session:
        return redirect("index")
    else:
        if request.POST:
            email=request.POST['email']
            password=request.POST['password']
            try:
                uid=user.objects.get(email=email)
                if email==email:
                    if uid.password==password:
                        request.session['email']=uid.email
                        return redirect("index")
                    else:
                        contaxt={
                            "msg":"invalid password"
                        }
                        return render(request,"login.html",contaxt)
                else:
                    return render(request,"login.html")
            except:
                contaxt={
                    "msg":"invalid email"
                }
                return render(request,"login.html",contaxt)
        else:
            return render(request,"login.html")


               
               
        
def register(request):
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        c_password=request.POST['c_password']
        print(name,email,password,c_password)
        uid=user.objects.filter(email=email).exists()
        uid1=user.objects.filter(name=name).exists()
        if uid:
            contaxt={
                "msg":"invalid email"
            }
            return render(request,"register.html",contaxt)
        elif uid1:
            contaxt={
                "msg":"invalid name"
            }
            return render(request,"register.html",contaxt)
        else:
            if password==c_password:
               user.objects.create(name=name,email=email,password=password)
               return redirect("login")
            else:
                contaxt={
                    "msg":"invalid password"
                }
                return render(request,"register.html",contaxt)
            
    return render(request,"register.html")

def logout(request):
    if "email" in request.session:
        del request.session['email']
    return redirect("login")


def forgot(request):
    if request.POST:
        email=request.POST['email']
        otp=random.randint(1000,9999)
        try:
            uid=user.objects.get(email=email)
            if uid:
                uid.otp=otp
                uid.save()
                send_mail("simple mail",f"your oti is:{otp}","devangpanchal1206@gmail.com",[email])
                contaxt={
                    "email":email
                }
                return render(request,"conform.html",contaxt)
        except:
            contaxt={
                "msg":"invalid email"
            }
            return render(request,"forgot.html",contaxt)
    else:
        return render(request,"forgot.html")

def conform(request):
    if request.POST:
        email=request.POST['email']
        otp=request.POST['otp']
        n_password=request.POST['n_password']
        c_password=request.POST['c_password']
        print(email,otp,n_password,c_password)

        uid=user.objects.get(email=email)
        print(type(uid.otp),type(otp))
        if uid.otp == int(otp):
            if n_password == c_password:
                uid.password=n_password
                uid.save()
                return redirect("login")
            else:
                contaxt={
                    "email":email,
                    "msg":"Invalid Password"
                }
                return render(request,"conform.html",contaxt)
        else: 
            print("otp") 
            contaxt={
                "email":email,
                "msg":"Invalid Otp"
            }
            return render(request,"conform.html",contaxt)
    else:  
        return render(request,"cornform.html")    
    
    



def search_fun(request):
    search=request.GET.get("search")
    print(search)
    mid=main_category.objects.all()
    bid=branding.objects.all()
    fid=prize.objects.all()
    cid=color.objects.all()
    sid=size.objects.all()
    if search:
        pid=product.objects.filter(name__contains=search)
    contaxt={
        "pid":pid,
        "mid":mid,
        "bid":bid,
        "fid":fid,
        "cid":cid,
        "sid":sid,
    }    
    return render(request,"shop.html",contaxt)


def apply_coupon(request):
    name=request.POST['coupon']
    print(name)
    uid=user.objects.get(email=request.session['email'])
    aid=add_to_cart.objects.filter(user_id=uid)
    l1=[]
    sub_total=0
    total=0
    for i in aid:
        l1.append(i.total)
    sub_total=sum(l1)  
    total=sub_total
    discount=0 
    c_id=coupon.objects.filter(name=name).exists()
    if c_id:
        print("yes")

        discount=total*30/100
        contaxt={
        "aid":aid,
        "sub_total":sub_total,
        "discount":discount,
        "total":total-discount,
        "uid":uid,
        }

        return render(request,"checkout.html",contaxt)
    else:
        print("no")    
    return render(request,"shopping_cart.html")
        

def billing_details(request):
    if 'email' in request.session:
        uid1 = user.objects.get(email=request.session['email'])
        aid = add_to_cart.objects.filter(user_id=uid1)
        
        if request.POST:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            country = request.POST['country']
            address = request.POST['address']
            address1 = request.POST['address1']
            city = request.POST['city']
            state = request.POST['state']
            pincode = request.POST['pincode']
            phone = request.POST['phone']
            email = request.POST['email']
            note = request.POST['note']

            # Create a new billing object and save it to the database
            billing_obj = billing.objects.create(
                first_name=first_name,
                last_name=last_name,
                country=country,
                address=address,
                address1=address1,
                city=city,
                state=state,
                pincode=pincode,
                phone=phone,
                email=email,
                notes=note
            )
            billing_obj.save()

            # Redirect to a success page or do whatever is necessary after saving the data
            return redirect("cheackout")

        context = {
            'aid': aid  # Pass the 'aid' variable to the template context
        }
        return render(request, "checkout.html", context)
    else:
        # Handle the case when 'email' is not in session
        return redirect("shopping_cart")  

