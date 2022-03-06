from django.shortcuts import render
from .models import ToDoList
from .form import CreateNewList
from django.http import HttpResponseRedirect
# Create your views here.

def index(response, id):
  ls = ToDoList.objects.get(id=id)

  if ls in response.user.todolist.all():

    if response.method == "POST":
      print(response.POST)
      if response.POST.get("save"):
          for item in ls.item_set.all():
            if response.POST.get("c" + str(item.id)) == "clicked":
              item.complete = True
            else:
              item.complete = False
  
            item.save()
      
      elif response.POST.get("newItem"):
        txt = response.POST.get("new")
  
        if len(txt) > 2:
          ls.item_set.create(text=txt, complete=False)
        else:
          print("invalid")
    
    return render(response, "main/list.html", {"ls":ls})
  return render(response, "main/view.html", {})

def home(response):
  return render(response, "main/home.html", {})

def create(response):
  if response.method == "POST":
      form = CreateNewList(response.POST)

      if form.is_valid():
          n = form.cleaned_data["name"]
          t = ToDoList(name=n)
          t.save()
          response.user.todolist.add(t)

      return HttpResponseRedirect("/%i" %t.id)
    
  else:
    form = CreateNewList()
  return render(response, "main/create.html", {"form":form})

def about(response):
  return render(response, "main/about.html", {})

def view(response):
  return render(response, "main/view.html", {})

# https://th.bing.com/th/id/OIP.Vp9A3P0j-XEIKgfkP7fwWwHaJX?pid=ImgDet&rs=1 KOOPA TROOPA JPG