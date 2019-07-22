from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from base_app.forms import Survey1Form, Survey2Form
from base_app.models import Survey1, Survey2


class BaseCreateView(CreateView):

    def form_valid(self, form_class):
        print("Form valid",form_class)
        form_class.instance.creator = self.request.user
        form_class.instance.updater = self.request.user
        return super(BaseCreateView, self).form_valid(form_class)

    def get_context_data(self, **kwargs):
        context = super(BaseCreateView, self).get_context_data(**kwargs)
        context.update({'title': self.form_class.Meta.model.__name__, 'redirect': True, 'panel_title': 'Create'})
        return context


class DashboardView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['title'] = 'Dashboard'
        return context


class Survey1View(TemplateView):
    template_name = "survey1.html"

    def get_context_data(self, **kwargs):
        context = super(Survey1View, self).get_context_data(**kwargs)
        context['title'] = 'Survey1'
        return context


class Survey2View(TemplateView):
    template_name = "survey2.html"

    def get_context_data(self, **kwargs):
        context = super(Survey2View, self).get_context_data(**kwargs)
        context['title'] = 'Survey2'
        return context


class CreateSurvey1(BaseCreateView):
    form_class = Survey1Form
    model = Survey1
    template_name = 'create_survey1.html'
    success_url = '/course-feedback/create-survey1'


class CreateSurvey2(BaseCreateView):
    form_class = Survey2Form
    model = Survey2
    template_name = 'create_survey2.html'
    success_url = '/course-feedback/create-survey2'
