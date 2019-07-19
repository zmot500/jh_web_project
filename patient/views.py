from django.shortcuts import render_to_response, redirect
from patient.models import Patient, Check
from anaconda_navigator.utils.py3compat import request
from django.views.decorators.csrf import csrf_exempt
from dask.dataframe.tests.test_rolling import idx

def home(request):
    patientList = Patient.objects.order_by("Pt_name")
    patientCount = Patient.objects.all().count()
    return render_to_response("list.html",\
{"patientList": patientList, "patientCount": patientCount})
    
    
@csrf_exempt
def insert_patient(request):
    patient=Patient(Pt_name=request.POST["Pt_name"],\
                 Pt_bdate=request.POST["Pt_bdate"],\
                 Pt_man=request.POST["Pt_man"])
    patient.save()
    return redirect("/")    

def detail_patient(request):
    id = request.GET["idx"]
    dto=Patient.objects.get(idx=id)
#    dtoList=Check.objects.raw("""
#        select Pt_name, Pt_bdate, idx_id, in_db, in_wt, in_bp_l, in_bp_h, in_date
#        from patient_patient, patient_check
#        where idx=%s
#        order by in_date
#    """,id)
    dtoList=Check.objects.filter(idx_id=id).order_by("-in_date")
    return render_to_response("detail_patient.html", {"dto":dto, "dtoList":dtoList})

@csrf_exempt
def insert_check(request):
    check=Check(idx_id=request.POST["idx_id"],\
                in_date=request.POST["in_date"],\
                in_db=request.POST["in_db"],\
                in_wt=request.POST["in_wt"],\
                in_bp_l=request.POST["in_bp_l"],\
                in_bp_h=request.POST["in_bp_h"])
    check.save()
    return redirect(".")

def detail_check(request):
    id = request.GET["idx"]
    dtoP=Patient.objects.get(idx=id)
    
    snumber = request.GET["sno"]
    dtoC=Check.objects.get(sno=snumber)
    return render_to_response("detail_check.html", {"dtoP":dtoP, "dtoC":dtoC})

@csrf_exempt
def update_check(request):
    id=request.POST["idx"]
    snumber=request.POST["sno"]
    check=Check(sno=snumber, idx_id=id,\
                in_date=request.POST["in_date"],\
                in_wt=request.POST["in_wt"],\
                in_db=request.POST["in_db"],\
                in_bp_l=request.POST["in_bp_l"],\
                in_bp_h=request.POST["in_bp_h"]
               )
    check.save()
    return redirect("/")
    
@csrf_exempt
def delete_check(request):
#    id=request.POST["idx"]
    snumber=request.POST["sno"]
    Check.objects.get(sno=snumber).delete()
    return redirect("/")
    