from django.shortcuts import render
from django.views.generic.edit import FormView

from django.http import HttpResponse

from .forms import ContactForm

# Create your views here.
class CommentView(FormView):

    template_name = "comment/comment.html"

    form_class = ContactForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        return self.render_to_response(self.get_context_data(post_id=kwargs['post_id']))


    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print("nice!")

