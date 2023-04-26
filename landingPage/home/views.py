from django.shortcuts import render,HttpResponseRedirect
from django.shortcuts import HttpResponse
from service.models import Service,Servicecard
from home.models import Home,HomeForm
from django.core.paginator import Paginator
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
# Create your views here.   
def homepage(request):
    # servicesData = Service.objects.all()
    # data2 = {
    #     'servicesData' : servicesData,
    subject = 'New Mail'
    message = '<p><b>Hello,</b> paste the given link to verify your account.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list =['chaudharyvasu234@gmail.com']
    message = EmailMultiAlternatives(subject,message,email_from,recipient_list)
    message.content_subtype = 'html'
    message.send()
    # send_mail(subject, message, email_from, recipient_list )
    print("Done")
    
    if request.method=="POST":
        print("inside post")
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        enquiry = HomeForm(user_name=name,user_email=email)
        enquiry.save()
        print("save done!")
        
    # data={
    #     "Name":name,
    #     "Email" : email,
    # }
    # try:
    #     if request.method == "POST":
    #         emailid = request.POST.get('Email')
    #         pswrd = request.POST.get('Password')
    #         print("Email entered is :" + emailid)
    #         print("Password entered is :" + pswrd)
    #         data = {
    #             "emailid":emailid,
    #             "password":pswrd
    #         }
    #     url = f"about-us/?name={emailid}"
    #     return HttpResponseRedirect(url)
    # except:
    #     pass
    return render(request,"index.html")    

def aboutUs(request):
    if request.method=="GET":
        emailid = request.GET.get('name')
        print("Email = ", emailid)
    return render(request,"aboutus.html",{'names':emailid})

def services(request):
    servicesData = Service.objects.all()
    servicescardFinal = Servicecard.objects.all()
    paginator = Paginator(servicescardFinal,1)
    page_number = request.GET.get('page')
    servicescardFinal = paginator.get_page(page_number)
    totalpage = servicescardFinal.paginator.num_pages
    if request.method == "GET":
        st = request.GET.get('servicename')
        if st!=None:
            servicesData = Service.objects.filter(service_icon=st)
    data = {
            'servicesData' : servicesData,
            'lastpage':totalpage,
            'totalpagelist':[n+1 for n in range(totalpage)],     
            'servicescardfinal':servicescardFinal,
            }
    return render(request,"services.html",data)

def contact(request):
    return render(request,"contacts.html")

def user_login(request):
    pass
    
    # return render(request,"index.html",data)
    # try:    
    #     emailid = request.GET['Email']
    #     pswrd = request.GET.get('Password')
    #     print("Email entered is :" + emailid)
    #     print("Password entered is :" + pswrd)
    # except:
    #     print("No Details.")
    # return render(request,"index.html")
    
def calculation(request):
    n1 = ''
    n2 = ''
    output =''
    try:
        if request.method=="POST":
            if request.POST.get('input1')=="":
                return render(request,"calculator.html",{"error":True})
            elif request.POST.get('input2')=="":
                return render(request,"calculator.html",{"error":True})
            n1 = eval(request.POST.get('input1'))
            n2 = eval(request.POST.get('input2'))
            opr = request.POST.get('operations')
            if opr=="+":
                output = n1+n2
            elif opr =="-":
                output = n1-n2 
            elif opr == "*":
                output = n1*n2
            elif opr == "/":
                output = n1/n2 
    except:
        print("Invalid inputs.")
    print(output)
    return render(request,"calculator.html",{'output':output,'n1':n1,'n2':n2}) 