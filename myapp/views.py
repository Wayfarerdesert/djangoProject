# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    username = 'Oso'
    return render(request, 'about.html', {
        'username': username
    })

def hello(request, username):
    print(username)
    return HttpResponse('<h1>Hello %s</h1>' % username)

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    # return JsonResponse(projects, safe=False)
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

def tasks(request):
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    # return HttpResponse('task: %s' % task.title)
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

def createTask(request):
    if request.method == 'GET':
        # show interface
        return render(request, 'tasks/createTask.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], projectkey=1)
        return redirect('/tasks/')

def createProject(request):
    if request.method == 'GET':
        return render(request, 'projects/createProject.html', {
        'form': CreateNewProject()
    })
    else:
        # print(request.POST)
        Project.objects.create(name=request.POST['name'])
        redirect('projects')
    #     print(project)
    #     return render(request, 'projects/createProject.html', {
    #     'form': CreateNewProject()
    # })

def projectDetail(request, id):
    #project = Project.objects.get(id=id)
    project = get_object_or_404(Project, id=id)
    #tasks = Task.objects.all()
    tasks = Task.objects.filter(project_id=id)

    print(project)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })



