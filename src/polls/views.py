from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import RequestContext,loader
from polls.models import Question,Choice
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
# def index(request):
#     latest_question_list=Question.objects.order_by("-pub_date")[:5]
#     #output=', '.join([p.question_text for p in latest_question_list])
#     template=loader.get_template('polls/index.html')
#     context=RequestContext(request,{
#         'latest_question_list':latest_question_list,                 
#     })
#     return HttpResponse(template.render(context))
# def index(request):
#     latest_question_list=Question.objects.order_by("-pub_date")[:5]
#     ditionary={'latest_question_list':latest_question_list}
#     return render(request,'polls/index.html',ditionary)
class IndexView(generic.ListView):
    template_name='polls/index.html'
    context_object_name='latest_question_list'
    def get_queryset(self):
        """Return the last five published questions."""
        #return Question.objects.order_by('pub_date')[:5]
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
        
class DetailView(generic.DetailView):
    model=Question
    template_name='polls/detail.html'
class ResultsView(generic.DetailView):
    model = Question
    template_name='polls/result.html'

# def detail(request,question_id):
#     try:
#         question=Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404
#     #return HttpResponse("You're looking at question %s." % question_id)
#     return render(request,'polls/detail.html',{'question':question})
# def detail(request,question_id):
#     question= get_object_or_404(Question,pk=question_id)
#     return render(request,"polls/detail.html",{'question':question})
#     
# def results(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,"polls/result.html",{'question':question})

def vote(request,question_id):
    p = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/details.html',{'question':p,'error_message':"You didn't select a choice",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))
