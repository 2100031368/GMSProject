from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from . models import Area, User, Grievance, EditData, Notification
from .forms import AddUserForm, AboutForm, ContactForm, UsageForm, NotifyForm
from GMSPROJECT.sms import send_sms
import matplotlib.pyplot as plt


############# about pg, contact pg, how to use pg

############# admin add area, delete are, update area
def adminhome(request):
    return render(request, "adminhome.html")

def viewareas(request):
    pid=request.session["pid"]
    user=User.objects.get(uid=pid)
    if(user.access == -1):
        area=Area.objects.all()
    else:
        area=Area.objects.filter(id=user.access)
    return render(request, "aareas.html", {"area":area})

def action0(request, aid):
    return render(request, "aactions.html", {"aid":aid})


def aaddarea0(request):
    pid=request.session["pid"]
    user=User.objects.get(uid=pid)
    if(user.access==-1):
        return render(request, "aaddarea.html")
    else:
        area=Area.objects.all()
        return render(request, "aareas.html", {"area": area})

def aaddarea1(request):
    a = Area.objects.all()
    if(request.method=="POST"):
        aname=request.POST["aname"]
        try:
            x=Area.objects.get(area__iexact=aname)
            msg="AREA WITH THIS NAME ALREADY EXIST"
            return render(request, "aareas.html", {"area":a, "msg":msg})
        except:
            newarea=Area(area=aname)
            newarea.save()
            msg="AREA ADDED SUCCESSFULLY"
            return render(request, "aareas.html", {"area":a, "msg":msg})
    else:
        return render(request, "aareas.html", {"area":a})


def editarea0(request, aid):
    pid=request.session["pid"]
    user=User.objects.get(uid=pid)
    if(user.access==-1):
        area=Area.objects.get(id=aid)
        return render(request, "aeditarea.html", {"area":area})
    else:
        area = Area.objects.all()
        return render(request, "aareas.html", {"area": area})


def updatearea(request, aid):
    newar=request.POST["aname"]
    Area.objects.filter(id=aid).update(area=newar)
    msg="UPDATED AREA NAME SUCCESSFULLY"
    a=Area.objects.all()
    return render(request, "aareas.html", {"msg":msg, "area":a})

def delarea0(request, aid):
    pid = request.session["pid"]
    user = User.objects.get(uid=pid)
    if (user.access == -1):
        a=Area.objects.all()
        try:
            area=Area.objects.get(id=aid)
            users=User.objects.filter(aid=aid).delete()
            gre = Grievance.objects.filter(aid=aid).delete()
            users=User.objects.filter(aid=aid).delete()
            area.delete()
            return render(request,"aareas.html", {"area":a})
        except:
            return render(request, "aareas.html", {"area":a})
    else:
        area = Area.objects.all()
        return render(request, "aareas.html", {"area": area})


##########    ADMIN -- USER  ADDING, DELETING, EDITING  #############
def viewusers0(request, aid):
    users=User.objects.filter(aid=aid)
    ar=Area.objects.get(id=aid)
    aname=ar.area
    return render(request, "ausers.html", {"users":users, "aid":aid, "aname":aname})

def adduser0(request, aid):
    form=AddUserForm()
    if(request.method == "POST"):
        form=AddUserForm(request.POST)
        if(form.is_valid()):
            user = form.save(commit=False)  # Create the model instance but don't save to the database yet
            user.aid = aid  # Manually set the 'aid' field
            user.save()
            msg="ADDED USER SUCCESSFULLY"
            users=User.objects.filter(aid = aid)
            msg2=f'Dear {user.name}\n, WELCOME TO VIJAYAWADA GRIEVANCE MANAGEMENT PORTAL.\nANY OF YOUR QURIES WILL BE TAKEN ACTIONS BY POSTING IN THE WEBSITE.\nFOR MORE DETAILS VISIT: \n. Thank You.'
            #sms=send_sms(user.mobile, msg2)
            return render(request, "ausers.html", {"msg":msg, "users":users})
        else:
            return render(request, "aadduser.html", {"aid": aid, "form":form})
    else:
        return render(request, "aadduser.html", {"aid":aid, "form":form})


def edituser0(request, uid):
    pid=request.session["pid"]
    admin=User.objects.get(uid=pid)
    user = User.objects.get(uid=uid)
    if(request.method=="POST"):
        form=AddUserForm(request.POST, instance=user)
        if(form.is_valid()):
            if(admin.access != -1):
                form.access=user.access
            form.save()
            msg=f'Dear User\n,YOUR DETAILS HAS BEEN UPDATED BY OUR MANAGEMENT.\nFOR MORE DETAILS VISIT: \n. Thank You.'
            #sms_sid=send_sms(user.mobile, msg)
            return redirect("viewusers0", aid=user.aid)
        else:
            return render(request, "aedituser.html",{"form":form})
    else:
        form = AddUserForm(instance=user)
        return render(request, "aedituser.html", {"form": form})

def deleteuser0(request, uid):
    user=User.objects.get(uid=uid)
    msg=f'Dear {user.name}\n,YOU HAVE BEEN REMOVED FROM VIJAYAWAD RIEVANCE MANAGEMENT PORTAL.\n Thank You.'
    #sms=send_sms(user.mobile, msg)
    aid=user.aid
    user.delete()
    return redirect("viewusers0", aid)

########### ADMIN SUB-ADMINS

#### 1. VIEW SUBADMINS
def viewsubadmin(request):
    pid=request.session["pid"]
    user=User.objects.get(uid=pid)
    areas=Area.objects.all()
    subadmins=[]
    if(user.access== -1):
        users=User.objects.all()
        for i in users:
            if i.access !=0 and i.access != -1:
                subadmins.append(i)
        return render(request, "asubadmins.html", {"subadmins":subadmins, "areas":areas})
    elif(user.access != 0 ):
        subadmins=User.objects.filter(access=user.access)
        return render(request, "asubadmins.html", {"subadmins": subadmins, "areas": areas})
    else:
        msg="ACCESS DENIED"
        return render(request, "adminhomt.html", {"msg":msg})

### 2. ADD SUBADMIN
def aaddsubadmin0(request, id):
    pid=request.session["pid"]
    user=User.objects.get(uid=pid)
    if(user.access == -1):
      user=User.objects.filter(aid=id)
      aname=Area.objects.get(id=id).area
      return render(request, "aaddsubadmin0.html", {"user":user, "aname":aname})
    else:
        msg="PRIVILEGE TO ADD SUBADMINS IS ONLY GIVEN TO ADMIN"
        return render(request, "aareas.html", {"msg":msg})

def aaddsubadmin1(request, id, uid):
    user=User.objects.get(uid=uid)
    user.access=id
    user.save()
    msg = f'Dear {user.name} you have been given SUB-ADMIN PRIVILEGE FOR YOUR AREA.\nYou are requested to complete your tasks and notify ADMIN if any needed.\nThankYou.'
    sms_sid = send_sms(user.mobile, msg)
    return redirect("aaddsubadmin0", id=id)

#### 3. take off from sub-admin position
def adenysubadmin(request, uid):
    pid=request.session["pid"]
    user =User.objects.get(uid=pid)
    if(user.access == -1):
        user=User.objects.get(uid=uid)
        user.access=0
        user.save()
        msg = f'Dear {user.name} you have been taken off from SUB-ADMIN PRIVILEGE FOR YOUR AREA.\nThankYou.'
        sms_sid = send_sms(user.mobile, msg)
        return redirect("viewsubadmin")
    else:
        return redirect("viewsubadmin")

############ VIEW GRIEV OF USERS

### 1.LIST OF GRE
def viewgrelist(request):
    pid=request.session["pid"]
    try:
        user=User.objects.get(uid=pid)
        if(user.access == -1):
            gres=Grievance.objects.all()
        else:
            gres=Grievance.objects.filter(aid=user.access)
        if(gres.count()==0):
            msg="NO GRIEVANCES POSTED"
            return render(request, "aviewgre.html", {"msg":msg})
        else:
            return render(request, "aviewgre.html", {"gres":gres})
    except:
        return HttpResponse("INVALID")

### 2. READ ISSUE AND MARK VIEWFLAG=1
def readgre(request, gid):
    x=Grievance.objects.get(gid=gid)
    if (x.viewflag != 1):
        x.viewflag=1
        x.viewdt=datetime.now()
    x.save()
    return render(request, "areadgre.html", {"x":x})

### 3.SOLVING ISSUE
def update_issue_status(request, gid):
    pid=request.session["pid"]
    gre=Grievance.objects.get(gid=gid)
    gre.solvedflag=1
    gre.solvedt=datetime.now()
    gre.solvedby=pid
    gre.save()
    user=gre.user
    msg=f'Dear User\n,GRIEVANCE POSTED FROM AADHAR NUMBER- {user.uid}\n GRIVANCE - {gre.issue} HAS BEEN SOLVED.\nFOR MORE DETAILS VISIT: \n. Thank You.'
    sms_sid=send_sms(user.mobile, msg)
    return redirect("viewgrelist")

##### edit data requests from user - area, name, mobile, address

def editreq0(request):
    pid=request.session["pid"]
    user = User.objects.get(uid=pid)
    if(user.access == -1):
        reqs=EditData.objects.all()
    else:
        users=User.objects.filter(aid=user.access)
        reqs=[]
        for i in users:
            try:
                edits=EditData.objects.get(user=i)
                reqs.append(edits)
            except:
                pass
    return render(request, "aeditreq0.html", {"reqs":reqs})


def editreq1(request, eid, flag): # flag for accepting and rejecting
    try:
        req = EditData.objects.get(eid=eid)
        if(flag == 1):
            userid=req.user.uid
            user=User.objects.get(uid=userid)
            type=req.type
            if(type=="MOBILE"):
                user.mobile=req.new
            elif(type=="NAME"):
                user.name=req.new
            elif(type=="ADDRESS"):
                user.address=req.new
            elif(type=="AREA"):
                user.aid=req.new
            user.save()
            req.status=1
            req.save()
        else:
            req.status=2
            req.save()
        return redirect("editreq0")
    except:
        return render(request, "404.html")

######### ADMIN VIEWING NOTIFICATIONS

def viewsendnotify(request):
    pid=request.session["pid"]
    try:
        user=User.objects.get(uid=pid)
        sent=Notification.objects.filter(sendby=user)
        users=User.objects.all()
        return render(request, "asentnotifys.html", {"sent":sent, "users":users})
    except:
        return render(request, "404.html")

def viewrecnotify(request):
    pid=request.session["pid"]
    try:
        user = User.objects.get(uid=pid)
        notify=Notification.objects.filter(touser=user)
        users=User.objects.all()
        return render(request, "aviewrecnotifys.html", {"notify":notify, "users":users})
    except:
        return render(request, "404.html")

def readnotify(request,id):
    try:
        notify=Notification.objects.get(id=id)
        notify.status=1
        notify.save()
        return render(request, "areadnotification.html", {"notify":notify})
    except:
        return render(request, "404.html")


def sendnotify(request, uid):
    pid=request.session["pid"]
    try:
        sender=User.objects.get(uid=pid)
        user=User.objects.get(uid=uid)
        if(request.method=="POST"):
            form=NotifyForm(request.POST)
            if (form.is_valid()):
                notify=form.save(commit=False)
                notify.sendby=sender
                notify.touser=user
                notify.senddt=datetime.now()
                notify.save()
                return redirect("viewrecnotify")
            else:
                return render(request, "asendnotify.html", {"form": form, "uid":uid})
        else:
            form=NotifyForm()
            uname= user.name
            return render(request, "asendnotify.html", {"form":form, "uid":uid, "uname":uname})
    except:
        return render(request, "404.html")
def deletenotify(request, id):
    notify=Notification.objects.get(id=id)
    notify.delete()
    return redirect("viewsendnotify")

############ ADMIN VIEW WORK ANALYSIS OF SUBADMIN
def workanalysis(request,uid):
    pid=request.session["pid"]
    user=User.objects.get(uid=uid)
    total=Grievance.objects.filter(aid=user.aid).count()
    totalsolved=Grievance.objects.filter(Q(aid=user.aid)&Q(solvedflag=1)).count()
    solved=Grievance.objects.filter(Q(aid=user.aid)&Q(solvedflag=1)&Q(solvedby=uid)).count()
    labels=['Total Issues', 'SolvedIssues', 'SolvedBySubAdmin']
    sizes=[total, totalsolved, solved]
    colors = ['#ff9999', '#66b3ff', '#99ff99']
    plt.figure(figsize=(6,6))
    plt.pie(sizes, labels=labels, colors=colors)
    plt.text(0, 1.2, f"Total: {total}, Solved: {totalsolved}, Solved by User: {solved}",
             ha='center', va='center', fontsize=12, weight='bold')

    plt.title('WORK ANALSIS')
    plt.show()
    return redirect("viewsubadmin")



