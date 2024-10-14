from django.shortcuts import render

# Create your views here.
from . models import Area, User
from .forms import AddUserForm

def viewareas(request):
    area=Area.objects.all()
    return render(request, "aareas.html", {"area":area})

def action0(request, aid):
    return render(request, "aactions.html", {"aid":aid})


def aaddarea0(request):
    return render(request, "aaddarea.html")

def aaddarea1(request):
    aname=request.POST["aname"]
    a=Area.objects.all()
    try:
        x=Area.objects.get(area__iexact=aname)
        msg="AREA WITH THIS NAME ALREADY EXIST"
        return render(request, "aareas.html", {"area":a, "msg":msg})
    except:
        newarea=Area(area=aname)
        newarea.save()
        msg="AREA ADDED SUCCESSFULLY"
        return render(request, "aareas.html", {"area":a, "msg":msg})


def editarea0(request, aid):
    area=Area.objects.get(id=aid)
    return render(request, "aeditarea.html", {"area":area})

def updatearea(request, aid):
    newar=request.POST["aname"]
    Area.objects.filter(id=aid).update(area=newar)
    msg="UPDATED AREA NAME SUCCESSFULLY"
    a=Area.objects.all()
    return render(request, "aareas.html", {"msg":msg, "area":a})

def delarea0(request, aid):
    a=Area.objects.all();
    area=Area.objects.get(id=aid)

    users=User.objects.filter(aid=aid)
    for i in users:
        if(i.access ==0):
            i.delete()
    msg="DELETED AREA SUCCESSFULLY"
    area.delete()
    return render(request, "aareas.html", {"msg": msg, "area": a})

### ADMIN -- USER
def viewusers0(request, aid):
    users=User.objects.filter(aid=aid)
    ar=Area.objects.get(id=aid)
    aname=ar.area
    return render(request, "ausers.html", {"users":users, "aname":aname})

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
            return render(request, "ausers.html", {"msg":msg, "users":users})
        else:
            return render(request, "aadduser.html", {"aid": aid, "form":form})
    else:
        return render(request, "aadduser.html", {"aid":aid, "form":form})



