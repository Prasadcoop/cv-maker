from django.shortcuts import render,HttpResponse,redirect
from django.template import loader
from .models import Profile ,Contact
from django.core.mail.message import EmailMessage
from django.contrib.auth.decorators import login_required
import requests
from bs4 import BeautifulSoup
import pdfkit

# Create your views here.
def homepage(request):
    return render(request,'main.html')


def secondpage(request):
    return render(request,'nav.html')

def resume(request):
    #return HttpResponse('hello')
    return render(request,'resume_builder.html')


@login_required(login_url='')
def addresume(request):
    if request.method == "POST":
        userid = request.POST.get("userid")
        name =request.POST.get("name") 
        objective =request.POST.get("objective") 
        address =request.POST.get("address") 
        phoneno =request.POST.get("phoneno") 
        email =request.POST.get("email") 
        github =request.POST.get("github")
        linkedin =request.POST.get("linkedin") 
        university1 =request.POST.get("university1") 
        degree1 =request.POST.get("degree1") 
        stream1 =request.POST.get("stream1") 
        currentYear1 =request.POST.get("currentYear1") 
        univStartingYear1 =request.POST.get("univStartingYear1") 
        univPassingYear1 =request.POST.get("univPassingYear1") 
        univResult1 =request.POST.get("univResult1")
        university2 =request.POST.get("university2") 
        degree2 =request.POST.get("degree2") 
        stream2 =request.POST.get("stream2") 
        currentYear2 =request.POST.get("currentYear2") 
        univStartingYear2 =request.POST.get("univStartingYear2") 
        univPassingYear2 =request.POST.get("univPassingYear2") 
        univResult2 =request.POST.get("univResult2")
        intermediateSchool =request.POST.get("intermediateSchool") 
        intermediateSubjects =request.POST.get("intermediateSubjects") 
        intermediateStartingYear =request.POST.get("intermediateStartingYear") 
        intermediatePassingYear =request.POST.get("intermediatePassingYear") 
        intermediateMarks =request.POST.get("intermediateMarks") 
        highSchool =request.POST.get("highSchool") 
        highSchoolSubjects =request.POST.get("highSchoolSubjects") 
        highSchoolStartingYear =request.POST.get("highSchoolStartingYear") 
        highSchoolPassingYear =request.POST.get("highSchoolPassingYear") 
        highSchoolMarks =request.POST.get("highSchoolMarks") 
        jobTitle1 =request.POST.get("jobTitle1") 
        jobStartDate1 =request.POST.get("jobStartDate1") 
        jobEndDate1 =request.POST.get("jobEndDate1") 
        jobDescription1 =request.POST.get("jobDescription1") 
        jobTitle2 =request.POST.get("jobTitle2") 
        jobStartDate2 =request.POST.get("jobStartDate2") 
        jobEndDate2 =request.POST.get("jobEndDate2") 
        jobDescription2 =request.POST.get("jobDescription2") 
        jobTitle3 =request.POST.get("jobTitle3") 
        jobStartDate3 =request.POST.get("jobStartDate3") 
        jobEndDate3 =request.POST.get("jobEndDate3") 
        jobDescription3 =request.POST.get("jobDescription3") 
        jobTitle4 =request.POST.get("jobTitle4") 
        jobStartDate4 =request.POST.get("jobStartDate4") 
        jobEndDate4 =request.POST.get("jobEndDate4") 
        jobDescription4 =request.POST.get("jobDescription4") 
        jobTitle5 =request.POST.get("jobTitle5") 
        jobStartDate5 =request.POST.get("jobStartDate5") 
        jobEndDate5 =request.POST.get("jobEndDate5") 
        jobDescription5 =request.POST.get("jobDescription5") 
        projectTitle1 =request.POST.get("projectTitle1") 
        projectStartDate1 =request.POST.get("projectStartDate1") 
        projectEndDate1 =request.POST.get("projectEndDate1") 
        projectDescription1 =request.POST.get("projectDescription1") 
        projectTitle2 =request.POST.get("projectTitle2") 
        projectStartDate2 =request.POST.get("projectStartDate2") 
        projectEndDate2 =request.POST.get("projectEndDate2") 
        projectDescription2 =request.POST.get("projectDescription2") 
        projectTitle3 =request.POST.get("projectTitle3") 
        projectStartDate3 =request.POST.get("projectStartDate3") 
        projectEndDate3 =request.POST.get("projectEndDate3") 
        projectDescription3 =request.POST.get("projectDescription3") 
        projectTitle4 =request.POST.get("projectTitle4") 
        projectStartDate4 =request.POST.get("projectStartDate4") 
        projectEndDate4 =request.POST.get("projectEndDate4") 
        projectDescription4 =request.POST.get("projectDescription4") 
        projectTitle5 =request.POST.get("projectTitle5") 
        projectStartDate5 =request.POST.get("projectStartDate5") 
        projectEndDate5 =request.POST.get("projectEndDate5") 
        projectDescription5 =request.POST.get("projectDescription5") 
        skillDetail =request.POST.get("skillDetail") 
        languageDetail =request.POST.get("languageDetail") 
        areaOfInterest =request.POST.get("areaOfInterest") 
        extracurricularDetail =request.POST.get("extracurricularDetail") 


        profile=Profile.objects.create(userid=userid, name=name, objective=objective, address=address, phoneno=phoneno, email=email, github=github, linkedin=linkedin, university1=university1, degree1=degree1, stream1=stream1, currentYear1=currentYear1, univStartingYear1=univStartingYear1, univPassingYear1=univPassingYear1, univResult1=univResult1, university2=university2, degree2=degree2, stream2=stream2, currentYear2=currentYear2, univStartingYear2=univStartingYear2, univPassingYear2=univPassingYear2, univResult2=univResult2, intermediateSchool=intermediateSchool, intermediateSubjects=intermediateSubjects, intermediateStartingYear=intermediateStartingYear, intermediatePassingYear=intermediatePassingYear, highSchool=highSchool, highSchoolSubjects=highSchoolSubjects, highSchoolStartingYear=highSchoolStartingYear, highSchoolPassingYear=highSchoolPassingYear, highSchoolMarks=highSchoolMarks, jobTitle1=jobTitle1, jobStartDate1=jobStartDate1, jobEndDate1=jobEndDate1, jobDescription1=jobDescription1, jobTitle2=jobTitle2, jobStartDate2=jobStartDate2, jobEndDate2=jobEndDate2, jobDescription2=jobDescription2, jobTitle3=jobTitle3, jobStartDate3=jobStartDate3, jobEndDate3=jobEndDate3, jobDescription3=jobDescription3, jobTitle4=jobTitle4, jobStartDate4=jobStartDate4, jobEndDate4=jobEndDate4, jobDescription4=jobDescription4, jobTitle5=jobTitle5, jobStartDate5=jobStartDate5, jobEndDate5=jobEndDate5, jobDescription5=jobDescription5, projectTitle1=projectTitle1, projectStartDate1=projectStartDate1, projectEndDate1=projectEndDate1, projectDescription1=projectDescription1, projectTitle2=projectTitle2, projectStartDate2=projectStartDate2, projectEndDate2=projectEndDate2, projectDescription2=projectDescription2, projectTitle3=projectTitle3, projectStartDate3=projectStartDate3, projectEndDate3=projectEndDate3, projectDescription3=projectDescription3, projectTitle4=projectTitle4, projectStartDate4=projectStartDate4, projectEndDate4=projectEndDate4, projectDescription4=projectDescription4, projectTitle5=projectTitle5, projectStartDate5=projectStartDate5, projectEndDate5=projectEndDate5, projectDescription5=projectDescription5, skillDetail=skillDetail, languageDetail=languageDetail, areaOfInterest=areaOfInterest, extracurricularDetail=extracurricularDetail)
      
        # p=product.save()
       # profile = Profile (userid=userid, name=name, objective=objective, address=address, phoneno=phoneno, email=email, github=github, linkedin=linkedin, university1=university1, degree1=degree1, stream1=stream1, currentYear1=currentYear1, univStartingYear1=univStartingYear1, univPassingYear1=univPassingYear1, univResult1=univResult1, university2=university2, degree2=degree2, stream2=stream2, currentYear2=currentYear2, univStartingYear2=univStartingYear2, univPassingYear2=univPassingYear2, univResult2=univResult2, intermediateSchool=intermediateSchool, intermediateSubjects=intermediateSubjects, intermediateStartingYear=intermediateStartingYear, intermediatePassingYear=intermediatePassingYear, highSchool=highSchool, highSchoolSubjects=highSchoolSubjects, highSchoolStartingYear=highSchoolStartingYear, highSchoolPassingYear=highSchoolPassingYear, highSchoolMarks=highSchoolMarks, jobTitle1=jobTitle1, jobStartDate1=jobStartDate1, jobEndDate1=jobEndDate1, jobDescription1=jobDescription1, jobTitle2=jobTitle2, jobStartDate2=jobStartDate2, jobEndDate2=jobEndDate2, jobDescription2=jobDescription2, jobTitle3=jobTitle3, jobStartDate3=jobStartDate3, jobEndDate3=jobEndDate3, jobDescription3=jobDescription3, jobTitle4=jobTitle4, jobStartDate4=jobStartDate4, jobEndDate4=jobEndDate4, jobDescription4=jobDescription4, jobTitle5=jobTitle5, jobStartDate5=jobStartDate5, jobEndDate5=jobEndDate5, jobDescription5=jobDescription5, projectTitle1=projectTitle1, projectStartDate1=projectStartDate1, projectEndDate1=projectEndDate1, projectDescription1=projectDescription1, projectTitle2=projectTitle2, projectStartDate2=projectStartDate2, projectEndDate2=projectEndDate2, projectDescription2=projectDescription2, projectTitle3=projectTitle3, projectStartDate3=projectStartDate3, projectEndDate3=projectEndDate3, projectDescription3=projectDescription3, projectTitle4=projectTitle4, projectStartDate4=projectStartDate4, projectEndDate4=projectEndDate4, projectDescription4=projectDescription4, projectTitle5=projectTitle5, projectStartDate5=projectStartDate5, projectEndDate5=projectEndDate5, projectDescription5=projectDescription5, skillDetail=skillDetail, languageDetail=languageDetail, areaOfInterest=areaOfInterest, extracurricularDetail=extracurricularDetail)
        profile.save()

        # messages.success(request, "Your resume has been successfully added!")
        return redirect('addResume')

    return render(request, 'addResume.html')   



# def addresume(request):
#     #return HttpResponse('hello')
#     return render(request,'addresume.html')

@login_required(login_url='')
def viewResume(request, id):
    user_profile = Profile.objects.get(pk=id)
    return render(request, "viewResume.html", {'user_profile':user_profile})
    
@login_required(login_url='')
def listResume(request):
    current_user = request.user.username
    userid = Profile.userid

    if Profile.objects.filter(userid = current_user).exists():
        profile=Profile.objects.filter(userid = current_user)
        return render(request, "listResume.html", {'profile':profile})
        
    return render(request, "listResume.html")

def logout(request):
    del request.session['username']
    return redirect('login')


def scrape_data(request):
    url = 'https://www.freecodecamp.org/news/python-sort-how-to-sort-a-list-in-python/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.text

       
        paragraphs = soup.find_all('p')
       
        return render(request, 'scrap_data.html', {
            'title': title,
            'paragraphs': paragraphs,
        })
    else:
        return render(request, 'scraping/error.html')


# def generate_resume(request):

#     user_profile = Profile.objects.get(pk=id)

#     resume_content = """
#         <div class="pt-4 pl-5 pr-5 ml-5 mr-5 pb-4">
#     <div class="row">
#         <div class="col-md-2">
#         </div>
#         <div class="col-md-8 border border-dark px-5 ">
#         <div class="row">
#             <h2 class=" h1 text-center py-3"> {{user_profile.name}}</h2>
#             <div class="col">
#             </div>
#             <div class="col">
#             </div>

#             <div class="col align-self-end pb-2">
#             <a href={{user_profile.github}}> {{user_profile.github}}</a> <br>
#             <a href={{user_profile.linkedin}}> {{user_profile.linkedin}}</a>
#             </div>
#             <hr class="hl">

#             <div class="col-sm-4">
#             <h4 class="py-3 vl px-2">CONTACT</h4>
#             <p>{{user_profile.address}}</p>
#             <p>{{user_profile.phoneno}}</p>
#             <p>{{user_profile.email}}</p>
#             </div>

#             <div class="col-sm-8">
#             <h4 class="py-3 vl px-2">OBJECTIVE</h4>
#             <p>{{user_profile.objective}}</p>
#             <br>
#             </div>
#         </div>

#         <div class="row">
#             <div class="col-sm-4">
#             <hr class="hl invisible">
#             <h4 class="py-3 vl px-2">SKILLS</h4>
#             <p>{{user_profile.skillDetail}}</p>
#             </div>
#             <div class="col-sm-8">

#             {% if user_profile.university1 or user_profile.university2 or user_profile.intermediateSchool or user_profile.highSchool %}
#             <hr class="hl">

#             <h4 class="py-3 vl px-2">EDUCATION</h4>

#             {% if user_profile.university1 %}

#             <p class="font-weight-bold">{{user_profile.degree1}} in {{user_profile.stream1}} --- (
#                 {{user_profile.univStartingYear1}} - {{user_profile.univPassingYear1}} ) </p>
#             <p>{{user_profile.university1}} </p>
#             <p>{{user_profile.univResult1}} </p>

#             {%endif%}

#             {% if user_profile.university2 %}

#             <p class="font-weight-bold">{{user_profile.degree2}} in {{user_profile.stream2}} --- (
#                 {{user_profile.univStartingYear2}} - {{user_profile.univPassingYear2}} ) </p>
#             <p>{{user_profile.university2}} </p>
#             <p>{{user_profile.univResult2}} </p>

#             {%endif%}

#             {% if user_profile.intermediateSchool %}

#             <p class="font-weight-bold"> Intermediate --- ( {{user_profile.intermediateStartingYear}} -
#                 {{user_profile.intermediatePassingYear}} )</p>
#             <p> {{user_profile.intermediateSchool}} </p>
#             <p> {{user_profile.intermediateMarks}} in {{user_profile.intermediateSubjects}} </p>

#             {%endif%}

#             {% if user_profile.highSchool %}

#             <p class="font-weight-bold"> High School --- ( {{user_profile.highSchoolStartingYear}} -
#                 {{user_profile.highSchoolPassingYear}} )</p>
#             <p> {{user_profile.highSchool}} </p>
#             <p> {{user_profile.highSchoolMarks}} in {{user_profile.highSchoolSubjects}} </p>

#             {%endif%}

#             {%endif%}
#             </div>
#         </div>

#         <div class="row">
#             <div class="col-sm-4">
#             <hr class="hl invisible">
#             <h4 class="py-3 vl px-2">LANGUAGES</h4>
#             <p>{{user_profile.languageDetail}}</p>
#             </div>
#             <div class="col-sm-8">

#             {% if user_profile.jobTitle1 or user_profile.jobTitle2 or user_profile.jobTitle3 or user_profile.jobTitle4 or user_profile.jobTitle5 or user_profile.projectTitle1 or user_profile.projectTitle2 or user_profile.projectTitle3 or user_profile.projectTitle4 or user_profile.projectTitle5 %}

#             <hr class="hl">

#             <h4 class="py-3 vl px-2">EXPERIENCE</h4>

#             {% if user_profile.jobTitle1 %}

#             <p class="font-weight-bold">{{user_profile.jobTitle1}} --- ( {{user_profile.jobStartDate1}} -
#                 {{user_profile.jobEndDate1}} ) </p>
#             <p>{{user_profile.jobDescription1}} </p>

#             {%endif%}
#             {% if user_profile.jobTitle2 %}

#             <p class="font-weight-bold">{{user_profile.jobTitle2}} --- ( {{user_profile.jobStartDate2}} -
#                 {{user_profile.jobEndDate2}} ) </p>
#             <p>{{user_profile.jobDescription2}} </p>

#             {%endif%}
#             {% if user_profile.jobTitle3 %}

#             <p class="font-weight-bold">{{user_profile.jobTitle3}} --- ( {{user_profile.jobStartDate3}} -
#                 {{user_profile.jobEndDate3}} ) </p>
#             <p>{{user_profile.jobDescription3}} </p>

#             {%endif%}
#             {% if user_profile.jobTitle4 %}

#             <p class="font-weight-bold">{{user_profile.jobTitle4}} --- ( {{user_profile.jobStartDate4}} -
#                 {{user_profile.jobEndDate4}} ) </p>
#             <p>{{user_profile.jobDescription4}} </p>

#             {%endif%}
#             {% if user_profile.jobTitle5 %}

#             <p class="font-weight-bold">{{user_profile.jobTitle5}} --- ( {{user_profile.jobStartDate5}} -
#                 {{user_profile.jobEndDate5}} ) </p>
#             <p>{{user_profile.jobDescription5}} </p>

#             {%endif%}

#             {% if user_profile.projectTitle1 %}

#             <p class="font-weight-bold">{{user_profile.projectTitle1}} --- ( {{user_profile.projectStartDate1}} -
#                 {{user_profile.projectEndDate1}} ) </p>
#             <p>{{user_profile.projectDescription1}} </p>

#             {%endif%}
#             {% if user_profile.projectTitle2 %}

#             <p class="font-weight-bold">{{user_profile.projectTitle2}} --- ( {{user_profile.projectStartDate2}} -
#                 {{user_profile.projectEndDate2}} ) </p>
#             <p>{{user_profile.projectDescription2}} </p>

#             {%endif%}
#             {% if user_profile.projectTitle3 %}

#             <p class="font-weight-bold">{{user_profile.projectTitle3}} --- ( {{user_profile.projectStartDate3}} -
#                 {{user_profile.projectEndDate3}} ) </p>
#             <p>{{user_profile.projectDescription3}} </p>

#             {%endif%}
#             {% if user_profile.projectTitle4 %}

#             <p class="font-weight-bold">{{user_profile.projectTitle4}} --- ( {{user_profile.projectStartDate4}} -
#                 {{user_profile.projectEndDate4}} ) </p>
#             <p>{{user_profile.projectDescription4}} </p>

#             {%endif%}
#             {% if user_profile.projectTitle5 %}

#             <p class="font-weight-bold">{{user_profile.projectTitle5}} --- ( {{user_profile.projectStartDate5}} -
#                 {{user_profile.projectEndDate5}} ) </p>
#             <p>{{user_profile.projectDescription5}} </p>

#             {%endif%}

#             {%endif%}

#             </div>
#         </div>

#         <div class="row">
#             <div class="col-sm-4">
#             </div>
#             <div class="col-sm-8">

#             {% if user_profile.areaOfInterest %}

#             <hr class="hl">
#             <h4 class="py-3 vl px-2">AREAS OF INTEREST</h4>
#             <p>{{user_profile.areaOfInterest}} </p>

#             {%endif%}

#             </div>
#         </div>

#         <div class="row">
#             <div class="col-sm-4">
#             <p> </p>
#             </div>

#             <div class="col-sm-8">

#             {% if user_profile.extracurricularDetail %}

#             <hr class="hl">
#             <h4 class="py-3 vl px-2">EXTRA CURRICULAR ACTIVITIES</h4>
#             <p>{{user_profile.extracurricularDetail}} </p>

#             {%endif%}

#             </div>
#         </div>
#         </div>

#         <div class="col-md-2">
#         </div>
#     </div>
#     </div>
#         """
#     response = HttpResponse(resume_content, content_type='text/html')
#     response['Content-Disposition'] = 'attachment; filename=resume.html'
#     return response

# def generate_resume(request):

#     url = "http://127.0.0.1:8000/8/"

#     div_selector = "div#myresume"

#     url = "https://example.com"
#     response = requests.get(url)

#     if response.status_code == 200:
#         page_content = response.content
#         soup = BeautifulSoup(page_content, "html.parser")
#         target_div = soup.select_one(div_selector)
#         if target_div:
#             # Save the div's content to a file
#             with open("extracted_div.html", "w", encoding="utf-8") as file:
#                 file.write(str(target_div))
#             print("Div content saved successfully as 'extracted_div.html'")
#         else:
#             print("Specified div not found on the webpage")
       
#     else:
#         print("Failed to download the resume")
    
def resumepdf(request):
    html = render(request, 'viewResume.html')
    wkhtmltopdf_path = '"D:\download\wkhtmltox-0.12.6-2.macos-cocoa.pkg"'

    pdf = pdfkit.from_string(html.content, False,configuration=pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path))
    
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    return response