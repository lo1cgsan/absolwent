from django.shortcuts import render
from wiadomosci.models import Wiadomosc
from wiadomosci.forms import WiadomoscForm
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DeleteView


def lista_wiadomosci(request):
    wiadomosci = Wiadomosc.objects.all()
    context = {'wiadomosci': wiadomosci}
    return render(request, 'wiadomosci/lista_wiadomosci2.html', context)


class ListaWiadomosci(ListView):
    model = Wiadomosc
    context_object_name = 'wiadomosci'
    template_name = 'wiadomosci/lista_wiadomosci2.html'


@login_required()
def dodaj_wiadomosc(request):
    if request.method == 'POST':
        form = WiadomoscForm(request.POST)
        if form.is_valid():
            w = Wiadomosc(tresc=form.cleaned_data['tresc'], autor=request.user, data_d=form.cleaned_data['data_d'])
            w.save()
            messages.success(request, "Dodano nową wiadomość!")
            return redirect(reverse('wiadomosci:lista'))
    else:
        form = WiadomoscForm()
    if request.user.has_perm('wiadomosci.add_wiadomosc'):
        return render(request, 'wiadomosci/dodaj_wiadomosc3.html', {'form': form})
    else:
        messages.info(request, "Nie możesz dodawać wiadomości!")
        return redirect(reverse('wiadomosci:lista'))


@method_decorator(login_required, name='dispatch')
class DodajWiadomosc(CreateView):
    model = Wiadomosc
    form_class = WiadomoscForm
    # fields = ('tresc', 'data_d')
    context_object_name = 'wiadomosci'
    template_name = 'wiadomosci/dodaj_wiadomosc3.html'
    success_url = '/'

    # def get_initial(self):
    #     initial = super(DodajWiadomosc, self).get_initial()
    #     initial['data_pub'] = timezone.now()
    #     return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wiadomosci'] = Wiadomosc.objects.filter(autor=self.request.user)
        return context

    def form_valid(self, form):
        wiadomosc = form.save(commit=False)
        wiadomosc.autor = self.request.user
        wiadomosc.save()
        messages.success(self.request, "Dodano wiadomość!")
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EdytujWiadomosc(SuccessMessageMixin, UpdateView):
    model = Wiadomosc
    form_class = WiadomoscForm
    context_object_name = 'wiadomosci'
    template_name = 'wiadomosci/dodaj_wiadomosc3.html'
    success_url = '/'
    success_message = 'Wiadomość zaktualizowano!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wiadomosci'] = Wiadomosc.objects.filter(autor=self.request.user)
        return context

    # def get_object(self, queryset=None):
    #     wiadomosc = Wiadomosc.objects.get(id=self.kwargs['pk'])
    #     return wiadomosc

@method_decorator(login_required, name='dispatch')
class UsunWiadomosc(DeleteView):
    model = Wiadomosc
    context_object_name = 'wiadomosc'
    template_name = 'wiadomosci/usun_wiadomosc1.html'
    success_url = '/'
    success_message = 'Wiadomość usunięto!'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wiadomosci'] = Wiadomosc.objects.filter(autor=self.request.user)
        return context