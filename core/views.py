from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import *
from django.db.models import Model
from django.db.models import Field
from django.forms.models import model_to_dict
from django.core import serializers
import json



def getName(fieldString):
    return fieldString.split(".")[-1]

# Create your views here.
def index(request):
    return render(request,"core/index.html",{"entities":companyCompare.objects.all()})

def getfield(request,eid,name,index):
    companies_json = serializers.serialize("json", [get_object_or_404(companyCompare,pk=eid)])
    cjl = json.loads(companies_json)
    
    return JsonResponse({"index":index,"pk":eid,"val":cjl[0]["fields"][name]})

def getfieldmcps(request,eid,name,index):
    companies_json = serializers.serialize("json", [get_object_or_404(mcpsSchool,pk=eid)])
    cjl = json.loads(companies_json)
    
    return JsonResponse({"index":index,"pk":eid,"val":cjl[0]["fields"][name]})


def explore(request):
    s=False
    g=False
    p=False
    try:
        objectfilter = request.GET["filter"]
        if objectfilter=="s":
            s=True
        if objectfilter=="g":
            g=True
        if objectfilter=="p":
            p=True
    except:
        pass
    return render(request,"core/explore.html",{"entities":companyCompare.objects.all(),"s":s,"g":g,"p":p})

def plasticmap(request):
    s=False
    g=False
    p=False
    try:
        objectfilter = request.GET["filter"]
        if objectfilter=="s":
            s=True
        if objectfilter=="g":
            g=True
        if objectfilter=="p":
            p=True
    except:
        pass

    companies_json = serializers.serialize("json", companyCompare.objects.all())
    cjl = json.loads(companies_json)

    return render(request,"core/plasticmap.html",{"rawjson":companies_json,"entities":cjl,"fields":cjl[0]["fields"].items()})


def plasticmapmcps(request):

    companies_json = serializers.serialize("json", mcpsSchool.objects.all())
    cjl = json.loads(companies_json)
    zipcodes = zipcode.objects.all()

    return render(request,"core/plasticmapmcps.html",{"zipcodes":zipcodes,"rawjson":companies_json,"entities":cjl,"fields":cjl[0]["fields"].items()})


def explorespecific(request,eid):
    e = get_object_or_404(companyCompare,pk=eid)
    posts = e.blogpost_set.all()
    return render(request,"core/explorespecific.html",{"e":e,"bps":posts})

def blog(request):
    return render(request,"core/exploreblog.html",{"bs":blogpost.objects.all()})

def blogspecific(request,eid):
    e = get_object_or_404(blogpost,pk=eid)
    return render(request,"core/blogpost.html",{"b":e})


def database(request):
    fields = companyCompare._meta.fields
    fields = list(fields)
    fields = list(map(str,fields))
    fields = list(map(getName,fields))
    companies = list(companyCompare.objects.all())
    companies = list(map(model_to_dict,companies))
    companies_json = serializers.serialize("json", companyCompare.objects.all())
    cjl = json.loads(companies_json)
    return render(request,"core/db.html",{"rawjson":companies_json,"entities":cjl,"fields":cjl[0]["fields"].items()})
