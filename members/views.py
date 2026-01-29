from django.shortcuts import render, get_object_or_404
from .models import Member

# your views here
def members(request):
    mymembers = Member.objects.all()
    
    context = {
        'mymembers': mymembers,
    }
    
    return render(request, "all_members.html",context)


def details(request, id):
    mymember = get_object_or_404(Member, id=id)
    context = {
        'mymember': mymember,
    }
    
    return render(request, 'details.html', context)


def main(request):
    return render(request, "main.html")


def testing(request):
    mydata = Member.objects.all()
    context = {
        'fruits': ['Apple','Banana','Cherry'],
    }
    
    return render(request, 'template.html',context)
