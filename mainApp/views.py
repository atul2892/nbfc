from django.shortcuts import render,redirect,HttpResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponseForbidden
from django.db.models import Q
from random import randrange
from django.conf import settings
from django.core.mail import send_mail

def homePage(Request):
    return render(Request,"index.html")

def aboutPage(Request):
    return render(Request,"about/index.html")

def registerPage(Request):
    return render(Request,"register/index.html")

def bankregisterPage(request):
    if request.method == "POST":
        p = request.POST.get("password")
        cp = request.POST.get("cpassword")
        
        if p != cp:
            messages.error(request, "Password and Confirm Password don't match!")
            return render(request, "register/bank-register.html")
        
        user_id = request.POST.get("userid")
        if User.objects.filter(username=user_id).exists():
            messages.error(request, "User Id already exists!")
            return render(request, "register/bank-register.html")
        
        b = Bank()
        b.user_id = user_id
        b.bank_name = request.POST.get("bankname")
        b.location = request.POST.get("location")
        b.logo = request.FILES.get("logo")  # Ensure to use request.FILES for file uploads
        b.password = p

        user = User(username=user_id)
        user.set_password(p)
        user.save()

        b.save()

        # Uncomment and configure email functionality if needed
        # subject = 'Your Account is Created: Team Vshop'
        # message = "Hello "+b.name+"\nThanks for creating a Buyer Account with Us\nNow you can buy our latest products\nTeam Vshop"
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [b.email]
        # send_mail(subject, message, email_from, recipient_list)

        return redirect("/registration-thanks")
    
    return render(request, "register/bank-register.html")

# def bankregisterPage(Request):
#     if(Request.method=="POST"):
#         p = Request.POST.get("password")
#         cp = Request.POST.get("cpassword")
#         if(p==cp):
#             b = Bank()
#             b.user_id = Request.POST.get("userid")
#             # b.email = Request.POST.get("email")
#             b.bank_name = Request.POST.get("bankname")
#             b.location = Request.POST.get("location")
#             b.logo = Request.POST.get("logo")
#             b.password = p
#             user = User(username=b.user_id)
#             if(user):
#                 user.set_password(p)
#                 user.save()
#                 b.save()
#                 # subject = 'Your Account is Created: Team Vshop'
#                 # message =  "Hello "+b.name+"\nThanks to Create a Buyer Account with Us\nNow You can buy Our Latest Products\nTeam Vshop"           
#                 # email_from = settings.EMAIL_HOST_USER
#                 # recipient_list = [b.email, ]
#                 # send_mail( subject, message, email_from, recipient_list )
#                 return redirect("/registration-thanks")
#             else:
#                 messages.error(Request,"User Id Already Exist!!!")
#         else:
#             messages.error(Request,"Password and Confirm Password doesn't matched!!!")    
#     return render(Request,"register/bank-register.html")

def condidateregisterPage(request):
    if request.method == "POST":
        p = request.POST.get("password")
        cp = request.POST.get("cpassword")
        
        if p != cp:
            messages.error(request, "Password and Confirm Password don't match!")
            return render(request, "register/bank-register.html")
        
        user_name = request.POST.get("username")
        if User.objects.filter(username=user_name).exists():
            messages.error(request, "User Name already exists!")
            return render(request, "register/bank-register.html")
        
        b = Candidate()
        b.user_name = user_name
        b.name = request.POST.get("fullname")
        b.email = request.POST.get("email")
        b.phone = request.POST.get("phone")
        b.location = request.POST.get("location")
        b.password = p

        user = User(username=user_name)
        user.set_password(p)
        user.save()

        b.save()

        # Uncomment and configure email functionality if needed
        # subject = 'Your Account is Created: Team Vshop'
        # message = "Hello "+b.name+"\nThanks for creating a Buyer Account with Us\nNow you can buy our latest products\nTeam Vshop"
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [b.email]
        # send_mail(subject, message, email_from, recipient_list)

        return redirect("/registration-thanks")
    return render(request,"register/condidate-register.html")


def registrationThanksPage(Request):
    return render(Request,"registration-thanks.html")

def loginPage(Request):
    if(Request.method=="POST"):
        username = Request.POST.get("user_id")
        password = Request.POST.get("password")
        user = authenticate(username=username,password=password)
        if(user is not None):
            login(Request,user)
            if(user.is_superuser):
                return redirect("/admin")
            else:
                if(Bank.objects.filter(user_id=username)):
                   return redirect("/bank-dashboard")
                elif(Candidate.objects.filter(user_name=username)):
                   return redirect("/candidate-dashboard")
        else:
            messages.error(Request,"Invalid Username or Password!!!")
    return render(Request, "login/index.html")

def logoutLogic(Request):
    logout(Request)
    return redirect("/login")


def loanPage(Request):
    loandata = Loan.objects.all()
    return render(Request,"loan/index.html",{"loandata":loandata})


def bankPage(Request,id):
    sldata = Loan.objects.get(id=id)
    bankdata = Bank.objects.all()
    return render(Request,"bank.html",{"sldata":sldata,"bankdata":bankdata})

@login_required(login_url='/login/')
def loanEnquiryPage(Request):
    loandata = Loan.objects.all()
    bankdata = Bank.objects.all()
    
    if (Request.method=="POST"):
        le = LoanEnquiry()
        le.loan = Request.POST.get("loan")
        le.bank = Request.POST.get("bank")
        le.candidate = Request.user.username
        le.name = Request.POST.get("fullname")
        le.email = Request.POST.get("email")
        le.phone = Request.POST.get("phone")
        le.amount = Request.POST.get("amount")
        le.tenure = Request.POST.get("tenure")
        le.adhar = Request.FILES.get("adhar")
        le.pan = Request.FILES.get("pan")
        le.save()
        messages.success(Request, "Your Details Submitted Successfully!!!")
    return render(Request,"loan-enquiry.html",{"loandata":loandata,"bankdata":bankdata})



# ========= Bank Panel Start ==========

@login_required(login_url='/login/')
def bank_dashboard(Request):
   
    data=LoanEnquiry.objects.filter(bank=Request.user.username).order_by('id').reverse()
    print(data)
    print("**********************")
    pending=len(LoanEnquiry.objects.filter(bank=Request.user.username,status="Pending"))
    under=len(LoanEnquiry.objects.filter(bank=Request.user.username,status="UnderProcess"))
    approved=len(LoanEnquiry.objects.filter(bank=Request.user.username,status="Approved"))
    cancel=len(LoanEnquiry.objects.filter(bank=Request.user.username,status="Cancel"))
    paginator = Paginator(data, 100)  # Show 10 posts per page
    page_number = Request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    current_page = page_posts.number
    total_pages = paginator.num_pages
    page_range = range(max(current_page - 2, 1), min(current_page + 3, total_pages + 1))
    
    
    return render(Request,'bank/index.html',{'page_posts':page_posts,'page_range': page_range,"pending":pending,"under":under,"approved":approved,"cancel":cancel})


@login_required(login_url='/login/')
def loan_enquiry_status(Request,id,ops):

    data=LoanEnquiry.objects.get(id=id)
    data.status=ops
    data.save()
    return redirect("/bank-dashboard")



# ========= Candidate Panel Start ==========

@login_required(login_url='/login/')
def candidate_dashboard(Request):
   
    data=LoanEnquiry.objects.filter(candidate=Request.user.username).order_by('id').reverse()
    print(data)
    print("**********************")
    # pending=len(Product.objects.all())
    # lstock=len(Product.objects.filter(stock_qty__lte=models.F('low_stock_qty')))
    # ord=len(Checkout.objects.all())
    # use=len(Buyer.objects.all())
    paginator = Paginator(data, 100)  # Show 10 posts per page
    page_number = Request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    current_page = page_posts.number
    total_pages = paginator.num_pages
    page_range = range(max(current_page - 2, 1), min(current_page + 3, total_pages + 1))
    
    
    return render(Request,'candidate/index.html',{'page_posts':page_posts,'page_range': page_range})


# @login_required(login_url='/login/')
# def loan_enquiry_status(Request,id,ops):

#     data=LoanEnquiry.objects.get(id=id)
#     data.status=ops
#     data.save()
#     return redirect("/bank-dashboard")