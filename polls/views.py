from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import F
from .models import Choice, Question,Vote
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]



class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get(self, request, *args, **kwargs):
        """
        If there is no question that can be voted, redirect to index page
        """
        question = self.get_object()
        if not question.can_vote():
            messages.error(request, "You can not vote on this question")
            return redirect('polls:index')
        return super().get(request, *args, **kwargs)


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })

    #Reference to the current user
    this_user = request.user

    #get the user's vote'
    try:
        # vote = user.votee_set.get(choice.question=question)
        vote = Vote.objects.get(user=this_user, choice__question=question )
        # User has a vote for this question! Update his choice.
        vote.choice = selected_choice
        vote.save()
        messages.success(request,f"Your vote was change to '{selected_choice.choice_text}'")
    except Vote.DoesNotExist:
        vote = Vote.objects.create(user=this_user, choice=selected_choice)
        # Does not have to vote yet
        # Auto save
        messages.success(request, f"Your vote was change to '{selected_choice.choice_text}'")
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
