from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .models import Doctor,Patient,Appointment

# Create your views here.
def home(request):
    return render(request,'hospital/home.html')

def about(request):
    return render(request,'hospital/about.html')

def contact(request):
    return render(request,'hospital/contact.html')

def index(request):
    if not request.user.is_staff:
        return redirect("login")
    return render(request,'hospital/index.html')

def Login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(request,username=data['username'],password=data['password'])
            if user is not None:
                login(request,user)
                return redirect("home")
            else:
                return HttpResponse("<h1>Invalid Crediantials</h1>")
    else:
        form=LoginForm()
    return render(request,'hospital/login.html',{'form':form})

def Logout(request):
    if not request.user.is_staff:
        return redirect("login")
    logout(request)
    return redirect("login")


def index(request):
    return render(request,'hospital/index.html')

def view_doctor(request):
    if not request.user.is_staff:
        return redirect("login")
    doc=Doctor.objects.all()
    d={'doc':doc}
    return render(request,'hospital/view_doctor.html',d)

def delete_doctor(request,pid):
   if pid:
        try:
            doctor_to_be_removed=Doctor.objects.get(id=pid)
            doctor_to_be_removed.delete()
            return HttpResponse("<h1>doctor Removed SuccessFully<h1>")
        except:
            return HttpResponse(("Please Enter A Valid EMPID"))
   doctors=Doctor.objects.all()
   context={
            'doctors':doctors
        }
   return render(request,'hospital/view_doctor.html',context)

def add_doctor(request):
    if not request.user.is_staff:
        return redirect("login")
    if request.method=='POST':
        n=request.POST['name']
        m=request.POST['mobile']
        sp=request.POST['special']
        try:
            Doctor.objects.create(name=n,mobile=m,special=sp)
            error="no"
        except:
            error="yes"
            d={'error':error}
        return HttpResponse("<h1>Record Added Successfully</h1>")
    return render(request,'hospital/add_doctor.html')

def view_patient(request):
    if not request.user.is_staff:
        return redirect("login")
    doc=Patient.objects.all()
    d={'doc':doc}
    return render(request,'hospital/view_patient.html',d)

def delete_patient(request,pid):
   if pid:
        try:
            patient_to_be_removed=Patient.objects.get(id=pid)
            patient_to_be_removed.delete()
            return HttpResponse("<h1>patient Removed SuccessFully<h1>")
        except:
            return HttpResponse(("Please Enter A Valid EMPID"))
   patient=Patient.objects.all()
   context={
            'patient':patient
        }
   return render(request,'hospital/view_patient.html',context)

def add_patient(request):
    if not request.user.is_staff:
        return redirect("login")
    if request.method=='POST':
        n=request.POST['name']
        g=request.POST['gender']
        m=request.POST['mobile']
        add=request.POST['address']
        try:
            Patient.objects.create(name=n,mobile=m,address=add)
            error="no"
        except:
            error="yes"
            d={'error':error}
        return HttpResponse("<h1>Record Added Successfully</h1>")
    return render(request,'hospital/add_patient.html')

def view_appointment(request):
    if not request.user.is_staff:
        return redirect("login")
    doc=Appointment.objects.all()
    d={'doc':doc}
    return render(request,'hospital/view_appointment.html',d)

def delete_appointment(request,pid):
   if pid:
        try:
            appointent_to_be_removed=Appointment.objects.get(id=pid)
            appointent_to_be_removed.delete()
            return HttpResponse("<h1>appointment Removed SuccessFully<h1>")
        except:
            return HttpResponse(("Please Enter A Valid EMPID"))
   appointment=Appointment.objects.all()
   context={
            'appointment':appointment
        }
   return render(request,'hospital/view_appointment.html',context)

def add_appointment(request):
    if not request.user.is_staff:
        return redirect("login")
    doctor1=Doctor.objects.all()
    patient1=Patient.objects.all()
    if request.method=='POST':
        n=request.POST['doctor']
        p=request.POST['patient']
        g=request.POST['gender']
        date=request.POST['date']
        time=request.POST['time']
        doctor=Doctor.objects.filter(name=n).first()
        patient=Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=n,patient=p,date=date,time=time,grnder=g)
            error="no"
        except:
            error="yes"
            d={'doctor':doctor1,'patient':patient1,'error':error}
        return HttpResponse("<h1>Record Added Successfully</h1>")
    return render(request,'hospital/add_appointment.html')
