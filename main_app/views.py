from django.shortcuts import render
from django.views import View
from .forms import DoList
from django.http import HttpResponseRedirect
# Create your views here.


class IndexView(View) :

    def status(self, request) :
        status = False
        if len(dict(request.session)) > 0 :
            if len(request.session.get("items")) > 0 :
                status = True
        elif len(dict(request.session)) == 0:
            request.session["items"] = []

        return status

    def get(self, request):
        
        return render(request, "main_app/index.html", {
            "status" : self.status(request),
            "form" : DoList(),
            "sessions" : enumerate(request.session["items"]),
        })

    def post(self, request):
        form = DoList(request.POST)

        if form.is_valid() :
            stored_list = request.session.get("items")
            data = request.POST["item"]
            stored_list.append(data)
            request.session["items"] = stored_list

            return HttpResponseRedirect("/")
        
        return render(request, "main_app/index.html", {
            "status" : self.status(request),
            "form" : DoList(),
            "sessions" : enumerate(request.session["items"]),
        })

    
class DeleteView(View) :

    def get(self, request) :
        return HttpResponseRedirect("/")

    def post(self, request) :
        index = int(request.POST["index"])
        stored_list = request.session.get("items")
        del stored_list[index]
        request.session["items"] = stored_list

        return HttpResponseRedirect("/")
    

class DeleteAllView(View) :

    def get(self, request) :
        return HttpResponseRedirect("/")
    
    def post(self, request) :
        request.session["items"] = []
        return HttpResponseRedirect("/")
    