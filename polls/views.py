##############################
#polls/views.py autogenerated
##############################
#Example 3
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext    # Context, loader,
from polls.models import Poll, Choice
# redirect a form
# Create your views here.


def index(request):
    # displays the latest 5 poll questions in the system,
    #separated by commas, according to publication date:
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]

    # View 1 with no argument:
    #return HttpResponse("Hello, world. You're at the poll index.")

    # View 2:
    #output = ', '.join([p.question for p in latest_poll_list])
    #return HttpResponse(output)

    # View 3: load template polls/index.html
    #t = loader.get_template('polls/index.html')
    #c = Context({'latest_poll_list': latest_poll_list,})
    #return HttpResponse(t.render(c))
    return render_to_response(
        'polls/index.html', {'latest_poll_list': latest_poll_list}
    )


def detail(request, poll_id):
    # View 2-1 with argument: Polls/34/
    #return HttpResponse("You're looking at poll %s." % poll_id)
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        #raise Http404  if the requested poll_id does not exist
        p = get_object_or_404(Poll, pk=poll_id)
    #return render_to_response('polls/detail.html', {'poll': p})
    # redirect a form
    return render_to_response(
        'polls/detail.html', {'poll': p},
        context_instance=RequestContext(request))


def results(request, poll_id):
    # View 2-2 with argument: Polls/34/results/
    # return HttpResponse(
    #     "You're looking at the results of poll %s." % poll_id)
    # Part 4:
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/results.html', {'poll': p})


def vote(request, poll_id):
    # dummy implementation View 2-3 with argument: Polls/34/vote/
    # return HttpResponse("You're voting on poll %s." % poll_id)
    # Part 4:

    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(
            reverse('polls.views.results', args=(p.id,))
            )