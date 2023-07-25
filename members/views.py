from django.urls import reverse_lazy
from django.views import generic
from .models import Member
from .forms import MemberForm, SignUPform


class SignUp(generic.CreateView):
    form_class = SignUPform
    success_url = "/"
    template_name = "registration/signup.html"


class MemberListView(generic.ListView):
    model = Member
    context_object_name = 'model'
    template_name = 'members.html'
    paginate_by = 5


class MemberCreateView(generic.CreateView):
    model = Member
    form_class = MemberForm
    template_name = 'members-create.html'
