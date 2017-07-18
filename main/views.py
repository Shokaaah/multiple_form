from django.http import JsonResponse
from django.views.generic import ListView
from django.views.generic.edit import FormView

from main.forms import MyForm
from main.models import FormDataModel


class MultipleFormView(FormView):
    template_name = 'home.html'
    form_class = MyForm
    success_url = '/list/'

    def get_form_kwargs(self):
        kwargs = super(MultipleFormView, self).get_form_kwargs()
        fields_count = int(self.request.POST.get('extra_field_count', 0))
        kwargs.update({'extra': fields_count})
        return kwargs

    def form_valid(self, form):
        model = FormDataModel(form_data=form.cleaned_data)
        model.save()
        return super(MultipleFormView, self).form_valid(form)


class FormsList(ListView):
    queryset = FormDataModel.objects.values()

    def render_to_response(self, context, **response_kwargs):
        data = list(context.get('object_list'))
        return JsonResponse({'data': data})


