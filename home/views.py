from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

# def index(request):
#     # now  = datetime.datetime.now()
#     # html = "<html><body><h3>the recent time is %s</h3></body></html>"% now
#     # return HttpResponse (html)

#     template = loader.get_template('myfirst.html')
#     name = {
#         'student':'Bhawani'
#     }
#     return HttpResponse(template.render(name))


# def blank(request):
#     return HttpResponse("This is a index Page")


# def registration(request):
#     return render(request, "myforth.html")


# def about(request):
    # template = (loader.get_template('myfirst.html'))
    # name = {
    #     'student' : 'Bhawani'
    # }
     # return HttpResponse(template.render(name))

#     return render(request, "myfirst.html")


# def contact(request):
#     template = loader.get_template("mysecond.html")
#     return HttpResponse(template.render())


# def services(request):
#     template = loader.get_template("mythird.html")
#     return HttpResponse(template.render())

# ----------------------------------------------------------------------------------------#

                                 #Session Set

def setsession(request):
    request.session['sname'] = "Bhawani"
    request.session['lname'] = "Patidar"
    request.session['semail'] = "bhawanipatidar@gmail.com"

    return HttpResponse("session is started")


def getsession(request):
    student_first_name = request.session['sname']
    student_last_name = request.session['lname']
    student_email = request.session['semail']

    return HttpResponse(student_first_name + " " + student_last_name + " " +student_email)


#---------------------------------------------------------------------------------------------------#

                                  #Cookie Set 


def setcookie(request):
    response = HttpResponse("Cookie set")
    response.set_cookie('GeeksforGeeks','GeeksforGeeks.com')
    return response

def getcookie(request):
    tutorial  = request.COOKIES['GeeksforGeeks']  
    return HttpResponse(" GeeksforGeeks @: "+  tutorial);   





