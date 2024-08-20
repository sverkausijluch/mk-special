from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'special/index.html'

class PresentationView(TemplateView):
    template_name = 'special/presentation.html'
    