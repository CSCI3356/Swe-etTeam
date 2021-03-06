# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Instructor
from .models import Student
from .models import Course
from .models import Team
from .models import PeerAssessment
from .models import CompletedAssessments
from .forms import PeerAssessmentForm
from .forms import StudentResponseForm
from .forms import createTeamsForm

from django.contrib.auth.decorators import login_required
# Create your views here.



def allAssessments(request): 
    return render(request,"templates/allAssessments.html", {})

def createPeerAssessment(request): 
    current_user = request.user.email
    if request.method == 'POST':
        form = PeerAssessmentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            teacher = Instructor.objects.get(email=current_user)
            instance.iid = teacher
            instance.save()
            #Assign this peer assessment to all teams in the course
            teamsToAssignAssessmentTo = Team.objects.filter(theCourse=instance.cid)
            for team in teamsToAssignAssessmentTo:
                team.livePAs.add(instance.pid)
        else:
            print(form.errors)
#        return HttpResponseRedirect('/home/')
    else:
        form = PeerAssessmentForm()

    return render(request,"createPeerAssessment.html", {'form': form})

@login_required
def studentTeacherLinking(request):
    isTeacher = request.user.is_teacher
    current_user = request.user.email
    print(current_user)

    if (isTeacher == True):
        obj = Instructor.objects.get(email=current_user)
        pas = PeerAssessment.objects.filter(iid=obj.iid)
        context = {
            'object': obj,
            'pas': pas
        }
        return render(request,"home.html", context)
    else:
        obj = Student.objects.get(email=current_user)
        teams = Team.objects.filter(students=obj)
        context = {
            'object': obj,
            'teams': teams
        }
        return render(request,"home.html", context)



def takePeerAssessment(request):
    current_user = request.user.email
    current = Student.objects.get(email=current_user)
    pidToUse = request.POST.get("p_id")
    print(pidToUse)
    obj2 = PeerAssessment.objects.get(pid=10)
    if request.method == 'POST':
        form = StudentResponseForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.sid = current
            instance.pid = obj2
            instance.save()
        else:
            print(form.errors)
        context = {
            'form': form
        }
        return HttpResponseRedirect('/home/')
    else: 
        if request.GET.get("paTakeChoice"):
            obj = PeerAssessment.objects.get(name=request.GET.get("paTakeChoice"))
        else:
            obj = PeerAssessment.objects.get(pid=1)
        form = StudentResponseForm()
        context = {
            'object': obj,
            'form': form
        }

    return render(request,"takePeerAssessment.html", context)

def makeTeams(request):
    current_user = request.user.email
    current_user = Instructor.objects.get(email=current_user)
    if request.method == 'POST':
        form = createTeamsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.tid=5
            instance.livePAs = [1, 2]
            instance.save()
        else:
            print(form.errors)

        context = {
            'form': form
        }
        return HttpResponseRedirect('/home/')
    else:     
        obj = Course.objects.filter(iid=current_user.iid)
        form = createTeamsForm()
        context = {
            'object': obj,
            'form': form
        }
    return render(request,"makeTeams.html", context)

def studentResults(request): 
    if request.method == 'GET':
        current_user = request.user.email
        current = Student.objects.get(email=current_user)
        cas = CompletedAssessments.objects.filter(evalStudent=current, pid=10)
        pidOfAssess = PeerAssessment.objects.get(pid=10)
        ans1 = []
        ans2 = []
        ans3 = []
        ans4 = []
        ans5 = []
        ans6 = []
        ans7 = []
        ans8 = []
        ans9 = []
        ans10 = []
        a = []
        for ca in cas:
                ans1.append(ca.answer1)
                ans2.append(ca.answer2)
                ans3.append(int(ca.answer3))
                ans4.append(int(ca.answer4))
                ans5.append(int(ca.answer5))
                ans6.append(int(ca.answer6))
                ans7.append(int(ca.answer7))
                ans8.append(int(ca.answer8))
                ans9.append(int(ca.answer9))
                ans10.append(int(ca.answer10))
        sum3 = round(sum(ans3)/float(len(ans3)), 2)
        sum4 = round(sum(ans4)/float(len(ans4)), 2)
        sum5 = round(sum(ans5)/float(len(ans5)), 2)
        sum6 = round(sum(ans6)/float(len(ans6)), 2)
        sum7 = round(sum(ans7)/float(len(ans7)), 2)
        sum8 = round(sum(ans8)/float(len(ans8)), 2)
        sum9 = round(sum(ans9)/float(len(ans9)), 2)
        sum10 = round(sum(ans10)/float(len(ans10)), 2)
        context = {
            'current': current,
            'cas': cas,
            'ans1': ans1,
            'ans2': ans2,
            'sum3': sum3,
            'sum4': sum4,
            'sum5': sum5,
            'sum6': sum6,
            'sum7': sum7,
            'sum8': sum8,
            'sum9': sum9,
            'sum10': sum10,
            'pidOfAssess': pidOfAssess
        }
    return render(request, "studentResults.html", context)

def instructorResults(request): 
    if request.method == 'GET' and request.GET.get("yourChoice"):
        if request.GET.get("yourChoice") == '2':
            obj = Team.objects.get(tid=2)
            if obj == Team.objects.get(tid=2):
                pidOfAssess = PeerAssessment.objects.get(pid=9)
                pidOfCompleteAssess = CompletedAssessments.objects.filter(pid=9)
                ans1 = []
                ans2 = []
                ans3 = []
                ans4 = []
                ans5 = []
                ans6 = []
                ans7 = []
                ans8 = []
                ans9 = []
                ans10 = []
                for ca in pidOfCompleteAssess:
                    ans1.append(ca.answer1)
                    ans2.append(ca.answer2)
                    ans3.append(int(ca.answer3))
                    ans4.append(int(ca.answer4))
                    ans5.append(int(ca.answer5))
                    ans6.append(int(ca.answer6))
                    ans7.append(int(ca.answer7))
                    ans8.append(int(ca.answer8))
                    ans9.append(int(ca.answer9))
                    ans10.append(int(ca.answer10))
                sum3 = round(sum(ans3)/float(len(ans3)),2)
                sum4 = round(sum(ans4)/float(len(ans4)),2)
                sum5 = round(sum(ans5)/float(len(ans5)), 2)
                sum6 = round(sum(ans6)/float(len(ans6)), 2)
                sum7 = round(sum(ans7)/float(len(ans7)), 2)
                sum8 = round(sum(ans8)/float(len(ans8)), 2)
                sum9 = round(sum(ans9)/float(len(ans9)), 2)
                sum10 = round(sum(ans10)/float(len(ans10)),2)
                context = {
                    'current': Team.objects.get(tid=2),
                    'ans1': ans1,
                    'ans2': ans2,
                    'sum3': sum3,
                    'sum4': sum4,
                    'sum5': sum5,
                    'sum6': sum6,
                    'sum7': sum7,
                    'sum8': sum8,
                    'sum9': sum9,
                    'sum10': sum10,
                    'pidOfAssess': pidOfAssess
                }
        else:
            obj = Student.objects.get(fname=request.GET.get("yourChoice"))
            pidOfAssess = PeerAssessment.objects.get(pid=9)
            cas = CompletedAssessments.objects.filter(evalStudent=obj)
            ans1 = []
            ans2 = []
            ans3 = []
            ans4 = []
            ans5 = []
            ans6 = []
            ans7 = []
            ans8 = []
            ans9 = []
            ans10 = []
            for ca in cas:
                if ca.pid == pidOfAssess:
                    ans1.append(ca.answer1)
                    ans2.append(ca.answer2)
                    ans3.append(int(ca.answer3))
                    ans4.append(int(ca.answer4))
                    ans5.append(int(ca.answer5))
                    ans6.append(int(ca.answer6))
                    ans7.append(int(ca.answer7))
                    ans8.append(int(ca.answer8))
                    ans9.append(int(ca.answer9))
                    ans10.append(int(ca.answer10))
            sum3 = round(sum(ans3)/float(len(ans3)),2)
            sum4 = round(sum(ans4)/float(len(ans4)),2)
            sum5 = round(sum(ans5)/float(len(ans5)),2)
            sum6 = round(sum(ans6)/float(len(ans6)),2)
            sum7 = round(sum(ans7)/float(len(ans7)),2)
            sum8 = round(sum(ans8)/float(len(ans8)),2)
            sum9 = round(sum(ans9)/float(len(ans9)),2)
            sum10 = round(sum(ans10)/float(len(ans10)),2)
            context = {
                'obj': obj,
                'ans1': ans1,
                'ans2': ans2,
                'sum3': sum3,
                'sum4': sum4,
                'sum5': sum5,
                'sum6': sum6,
                'sum7': sum7,
                'sum8': sum8,
                'sum9': sum9,
                'sum10': sum10,
                'pidOfAssess': pidOfAssess
            }
    else:
        context = {

        }

    return render(request, "instructorResults.html", context)



# this needs to be updated
# def studentResults(request):
#     obj = studentResults.objects.get(pid=1)
#     context = {
#         'object': obj
#     }
#     return render(request,"",context)

# def enterQuestions(request):
#     #if request.method == 'POST':
#         #form = EnterQuestionsForm(request.POST)
#         #if form.is_valid():
#          #   for i
#     #data= request.POST.get('name')
#     #
#     #    numString += '3'
#     # obj = PeerAssessment.objects.get(pid=1)
#     # context = {
#     #     'object': obj,
#     #     'loopc': '123456789'
#     # }
#     if request.method == 'POST':
#         form = EnterQuestionsForm(request.POST or None)
#         if form.is_valid():
#             myQuestions = form.save()
#             myQuestions.private_field = "2"
#             myQuestions.save()
#             return HttpResponseRedirect('/home/')
#     else:
#         form = EnterQuestionsForm()
    
#     return render(request,"enterQuestions.html", {'form': form})
