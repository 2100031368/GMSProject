import random

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import render, redirect
from adminapp.models import User, Area, Notification, About, Contact, Usage
from adminapp.forms import AboutForm, ContactForm, UsageForm
from .sms import send_sms


def home(request):
    return render(request, "home.html");
def about(request):
    return render(request, "about.html");

def contact(request):
    return render(request, "contact.html");

def login(request):
    if (request.method=="POST"):
        id=request.POST["id"]
        try:
                user=User.objects.get(uid=id)
                if(user.flag==1):
                    request.session["pid"]=user.uid
                    return redirect("sendOtp")
                else:
                    msg="Access Denied"
                    return render(request, "login.html", {"msg":msg})

        except ObjectDoesNotExist:
                msg="User Not Exist"
                return render(request, "login.html", {"msg":msg})
    else:
        request.session.flush()
        return render(request, "login.html")


def sendOtp(request):
    pid=request.session["pid"]
    try:
        user=User.objects.get(uid=pid)
        otp=random.randint(100000, 999999)
        request.session["otp"]=otp
        msg=f'Your OTP is: {otp}'
        print("user mobile", user.mobile)
        print(type(user.mobile))
        sms_sid = send_sms(user.mobile, msg)
        return render(request, "enterOtp.html")
    except:
        msg="USER NOT FOUND"
        return render(request, "login.html", {"msg": msg})

def verifyOtp(request):
    pid =request.session["pid"]
    if (request.method == "POST"):
        otp1 = request.POST["otp"]
        otp0 = request.session["otp"]
        print(type(otp1))
        print(type(otp0))
        user=User.objects.get(uid=pid)
        if (str(otp1) == str(otp0)):
            if (user.access == 0):
                return render(request, "userhome.html")
            else:
                count = Notification.objects.filter(Q(touser=user) & Q(status=0)).count()
                print(count)
                return render(request, "adminhome.html", {"count": count})

        else:
            msg="X OTP MISMATCH X"
            return render(request, "login.html", {"msg":msg})
    else:
        return redirect("login")


def about(request):
    pid=request.session.get("pid")
    try:
        about = About.objects.get(id=1)
        if(pid is None):
            return render(request, "about.html", {"about":about})
        else:
            user=User.objects.get(uid=pid)
            if(user.access == -1):
                flag=1
            else:flag=0
            return render(request, "about.html", {"about": about, "flag":flag})
    except:
        if (pid is None):
            return render(request, "about.html")
        else:
            user = User.objects.get(uid=pid)
            if (user.access == -1):
                flag = 1
            else:
                flag = 0
            return render(request, "about.html", {"flag": flag})

def contact(request):
    pid = request.session.get("pid")
    try:
        contact = Contact.objects.get(id=1)
        if (pid is None):
            return render(request, "contact.html", {"contact": contact})
        else:
            user = User.objects.get(uid=pid)
            if (user.access == -1):
                flag = 1
            else:
                flag = 0
            return render(request, "contact.html", {"contact": contact, "flag": flag})
    except:
        if (pid is None):
            return render(request, "contact.html")
        else:
            user = User.objects.get(uid=pid)
            if (user.access == -1):
                flag = 1
            else:
                flag = 0
            return render(request, "contact.html", {"flag": flag})


def usage(request):
    pid = request.session.get("pid")
    try:
        usage = Usage.objects.get(id=1)
        if (pid is None):
            return render(request, "usage.html", {"usage": usage})
        else:
            user = User.objects.get(uid=pid)
            if (user.access == -1):
                flag = 1
            else:
                flag = 0
            return render(request, "usage.html", {"usage": usage, "flag": flag})
    except:
        if (pid is None):
            return render(request, "usage.html")
        else:
            user = User.objects.get(uid=pid)
            if (user.access == -1):
                flag = 1
            else:
                flag = 0
            return render(request, "usage.html", {"flag": flag})


def myprofile(request):
    pid=request.session["pid"]
    profile=User.objects.get(uid=pid)
    area=Area.objects.get(id=profile.aid)
    aname=area.area
    return render(request, "myprofile.html", {"profile":profile, "aname":aname})

def addaacu(request, id):
    if(request.method=="POST"):
        if(id == 1):
            form=AboutForm(request.POST)
            form.save()
            msg="ABOUT CONTENT UPDATED"
            return render(request, "adminhome.html")
        elif(id==2):
            form = ContactForm(request.POST)
            form.save()

            return render(request, "adminhome.html")
        else:
            form = UsageForm(request.POST)
            form.save()
            return render(request, "adminhome.html")

    else:
        if(id==1):
            title="ABOUT UPDATING FORM"
            form=AboutForm()
            return render(request, "aacu.html", {"form":form, "id":id, "title":title})
        elif(id==2):
            title = "CONTACT UPDATING FORM"
            form = ContactForm()
            return render(request, "aacu.html", {"form": form, "id":id, "title":title})
        else:
            title = "WEBSITE USAGE UPDATING FORM"
            form = UsageForm()
            return render(request, "aacu.html", {"form": form, "id":id, "title":title})
