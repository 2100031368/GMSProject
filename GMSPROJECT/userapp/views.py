from datetime import datetime

from django.core.files.storage import default_storage
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from adminapp.models import Grievance, User, Area, EditData, Usage, About, Contact

from adminapp.forms import PostGreForm

### 0. USER HOME
def userhome(request):
    return render(request, "userhome.html")

### 1. USER VIEWING HER GRIEVANCES
def viewmygre0(request):
    pid=request.session["pid"]
    user=User.objects.get(uid=pid)
    mygre = Grievance.objects.filter(user=user)
    return render(request, "uviewmygre.html", {"mygre":mygre})

### 2. MODIFYING POSTED GRIEVANCE
def editmygre0(request, gid):
   gre=Grievance.objects.get(gid=gid)
   pid = request.session["pid"]
   if(request.method=="POST"):
       form=PostGreForm(request.POST, instance=gre)
       if(form.is_valid()):
           form.save()
           user=User.objects.get(uid=pid)
           mygre = Grievance.objects.filter(user=user)
           msg="EDITED GRIEVANCE SUCCESSFULLY"
           return render(request, "uviewmygre.html", {"mygre":mygre, "msg":msg})
       else:
           return render(request, "upostgre.html", {"form": form})
   else:
       form = PostGreForm()
       return render(request, "upostgre.html", {"form": form})

def delmygre0(request, gid):
    pid=request.session["pid"]
    gre=Grievance.objects.get(gid=gid)
    gre.delete()
    user=User.objects.get(uid=pid)
    mygre = Grievance.objects.filter(user=user)
    msg="DELETED GRIEVANCE SUCCESSFULLY"
    return render(request, "uviewmygre.html", {"msg":msg, "mygre":mygre})

### 3. POSTING GRIEVANCE
def postgre0(request):
    pid=request.session["pid"]
    user=User.objects.get(uid=pid)
    aname=Area.objects.get(id=user.aid)
    if(request.method == "POST"):
        form = PostGreForm(request.POST)
        if(form.is_valid()):
            gre=form.save(commit=False)
            gre.user=user
            gre.aid=user.aid
            gre.area=aname
            gre.phno=user.mobile
            gre.postdt=datetime.now()
            gre.save()
            return redirect("viewmygre0")
        else:
            return render(request, "upostgre.html", {"form":form})
    else:
        form=PostGreForm()
        return render(request, "upostgre.html", {"form": form})

### 4. REQUEST TO EDIT HER DETAILS
def editmydetails0(request):
    return render(request, "ueditmydetails0.html")
def editmobile(request):
    pid=request.session["pid"]
    user=User.objects.get(uid=pid)
    if(request.method== "POST"):
        newph=request.POST["newph"]
        if(newph == user.mobile):
            msg="MOBILE NUMBER ENTERED IS SAME AS EXISTED ONE"
            return render(request, "ueditmydetails0.html", {"msg":msg})
        else:
            reason=request.POST["reason"]
            proof=request.files["file"]
            data = EditData(user=user, type="MOBILE", old=user.mobile, new=newph, reason=reason, proof=proof, reqdt=datetime.now())
            data.save()
            return redirect("myedits")
    else:
        return render(request, "ueditmobile.html", {"pid":pid})

def editname(request):
    pid = request.session["pid"]
    user = User.objects.get(uid=pid)
    if (request.method == "POST"):
        newname = request.POST["newname"]
        if (newname == user.name):
            msg = "USER NAME ENTERED IS SAME AS EXISTED ONE"
            return render(request, "ueditmydetails0.html", {"msg": msg})
        else:
            reason = request.POST["reason"]
            proof = request.FILES["file"]
            data = EditData(user=user, type="NAME", old=user.name, new=newname, reason=reason, proof=proof, reqdt=datetime.now())
            data.save()

            return redirect("myedits")
    else:
        return render(request, "ueditname.html", {"pid": pid})

def editaddr(request):
    pid = request.session["pid"]
    user = User.objects.get(uid=pid)
    if (request.method == "POST"):
        newaddr = request.POST["newaddr"]
        if (newaddr == user.address):
            msg = "ADDRESS ENTERED IS SAME AS EXISTED ONE"
            return render(request, "ueditmydetails0.html", {"msg": msg})
        else:
            reason = request.POST["reason"]
            proof = request.files["file"]
            data = EditData(user=user, type="ADDRESS", old=user.address, new=newaddr, reason=reason, proof=proof, reqdt=datetime.now())
            data.save()
            return redirect("myedits")
    else:
        return render(request, "ueditaddress.html", {"pid": pid})

def editarea0(request):
    pid=request.session["pid"]
    user=User.objects.get(uid=pid)
    try:
        exist=EditData.objects.get(Q(type="ADDRESS")&Q(user=user))
        areas=Area.objects.all()
        return render(request,"ueditarea.html", {"areas":areas})
    except:
        msg="YOU NEED TO FIRST EDIT ADDRESS THEN EDIT AREA"
        return render(request, "ueditaddress.html", {"msg":msg})

def editarea1(request):
    pid = request.session["pid"]
    user = User.objects.get(uid=pid)
    if (request.method == "POST"):
        newaid = request.POST["newaid"]
        if (newaid == user.aid):
            msg = "AREA ENTERED IS SAME AS EXISTED ONE"
            return render(request, "ueditmydetails0.html", {"msg": msg})
        else:
            reason = request.POST["reason"]
            proof = request.files["file"]
            data = EditData(user=user, type="AREA", old=user.aid, new=newaid, reason=reason, proof=proof, reqdt=datetime.now())
            data.save()
            return redirect("myedits")

    else:
        return redirect("editarea0")

###### 5. user view his edit requests and status
def myedits(request):
    pid=request.session["pid"]
    user=User.objects.get(uid=pid)
    myreq=EditData.objects.filter(user=user)
    return render(request, "umyeditreq.html", {"myreq":myreq})

#### user delete his req if admin not updated it
def delmyreq(request,eid):
    req=EditData.objects.get(eid=eid)
    file_path = req.proof.path

    if default_storage.exists(file_path):
        default_storage.delete(file_path)
    req.delete()
    return redirect("myedits")

####### 6. how to use
def usage(request):
    usage=Usage.objects.first()
    return render(request, "usage.html")

def contact(request):
    contact=Contact.objects.first()
    return render(request, "contact.html")

def about(request):
    about=About.objects.first()
    return render(request, "about.html")
