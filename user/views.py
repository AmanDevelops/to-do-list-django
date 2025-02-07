from django.shortcuts import render
from .models import ToDoList


# Create your views here.
def home(request):
    if request.method == "POST":
        try:
            todo = ToDoList()
            todo.status = False
            todo.task = request.POST['todo']
            todo.user = request.user.username
            todo.save()
        except KeyError:
            try:
                print("isChecked:", request.POST)
                print("id:", request.POST.get("id"))
                if "id" in request.POST:
                    is_checked = request.POST.get("isChecked") == "True"
                    print("Status:", is_checked)
                    ToDoList.objects.filter(id=request.POST['id']).update(status=not is_checked)
            except KeyError:
                pass
    data = ToDoList.objects.all()

    return render(request, 'user/index.html', {"data": data})