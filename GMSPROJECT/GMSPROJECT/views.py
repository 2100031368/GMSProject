import random

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from adminapp.models import User, Area
from adminapp.sms import send_sms


def home(request):
    return render(request, "home.html");
def about(request):
    return render(request, "about.html");

def contact(request):
    return render(request, "contact.html");

def login(request):
    if request.method == "POST":
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
        return render(request, "login.html");

def sendOtp(request):
    pid=request.session["pid"]
    user=User.objects.get(uid=pid)
    otp=random.randint(100000, 999999)
    request.session["otp"]=otp
    msg=f'Your OTP is: {otp}'
    sms_sid = send_sms(user.mobile, msg)
    print("SMS SID:", sms_sid)  # Debug output to verify SMS sending
    print("OTP Sent:", otp)  # Debug output to verify OTP value
    return render(request, "enterOtp.html")

def verifyOtp(request):
    pid =request.session["pid"]
    if (request.method == "POST"):
        otp1 = request.POST["otp"]
        otp0 = request.session["otp"]
        print(type(otp1))
        print(type(otp0))
        if (str(otp1) == str(otp0)):
            user = User.objects.get(uid=pid)
            if (user.access == 0):
                return render(request, "userhome.html")
            else:
                return render(request, "adminhome.html")
        else:
            msg="X OTP MISMATCH X"
            return render(request, "login.html", {"msg":msg})
    else:
        return redirect("login")
