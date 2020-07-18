from django.shortcuts import render,get_object_or_404
from .models import Project
from django.template import loader
from django.views import generic
#def index(request):
#    projects = Project.objects.order_by('-pub_date')[:5]
    #context dictionary is loaded in html template
#    context = {'projects': projects}
#    return render(request,'projects/index.html',context)

#def detail(request, project_url_str):
#    project=get_object_or_404(Project,url_str=project_url_str)
#    context = {'project': project}
#    return render(request,'projects/detail.html',context)
    

class IndexView(generic.ListView):
    template_name = 'projects/index.html'
    context_object_name = 'projects'

    def get_queryset(self):
        """Return the last five published questions."""
        #print(Project.objects.order_by('-pub_date')[:5])
        return Project.objects.order_by('-pub_date')[:5]
class DetailView(generic.DetailView):
    model = Project
    slug_field='url_str'
    slug_url_kwarg='slug'
    template_name = 'projects/detail.html'

