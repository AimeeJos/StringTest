from django.http import HttpResponse
from django.shortcuts import render
from .forms import myform
from collections import Counter


def index(request):
    masterstr = ''
    string1str = ''
    string2str = ''
    string3str = ''
    string4str = ''
    if request.method =='POST':
        masterstr = request.POST.get('master').lower()
        string1str = request.POST.get('string1').lower()
        string2str = request.POST.get('string2').lower()
        string3str = request.POST.get('string3').lower()
        string4str = request.POST.get('string4').lower()
    master = Counter(masterstr)

    string1 = Counter(string1str)
    result1 = checkStr(master, string1)

    string2 = Counter(string2str)
    result2 = checkStr(master, string2)

    string3 = Counter(string3str)
    result3 = checkStr(master, string3)

    string4 = Counter(string4str)
    result4 = checkStr(master, string4)
    form=myform()
    context={'form':form,
             'Master':masterstr,
             'strings':{string1str:result1,
                        string2str:result2,
                        string3str:result3,
                        string4str:result4,
                        },
             }

    return render(request,"home.html",context)

def checkStr(master,child):
    flag = ""
    for ch in child:
        if ch in master.keys():
            if child[ch] <= master[ch]:
                master[ch] = master[ch] - child[ch]
                # print(ch,master)
                flag = 'Yes'
            else:
                flag = 'No'
                break
        else:
            flag = "No"
            break

    return flag