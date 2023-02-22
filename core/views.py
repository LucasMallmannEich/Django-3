from django.views.generic import FormView
from core.models import Servico, Team, Features
from core.forms import ContatoForm
from django.urls import reverse_lazy
from django.contrib import messages


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('rota_index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['team'] = Team.objects.order_by('?').all()
        context['features'] = Features.objects.order_by('?').all()
        if len(context['features']) % 2 == 0:
            metade1 = len(context['features'])/2
            metade2 = metade1
        else:
            metade1 = int(len(context['features'])/2 + 0.5)
            metade2 = metade1 - 1
        context['metade1'] = str(int(metade1)) + ':'
        context['metade2'] = ':' + str(int(metade2))
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Email enviado com sucesso.')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o email.')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
