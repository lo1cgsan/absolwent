from django.shortcuts import render
from django.views.generic import ListView, DetailView
from ankiety.models import Pytanie, Odpowiedz
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ListaPytan(ListView):
    model = Pytanie
    template_name = 'ankiety/lista_pytan.html'
    context_object_name = 'pytania'

    def get_queryset(self):
        return Pytanie.objects.order_by('-data_d')[:10]


@method_decorator(login_required, name='dispatch')
class LiczbaGlosow(DetailView):
    model = Pytanie
    template_name = 'ankiety/liczba_glosow.html'
    context_object_name = 'pytanie'


@login_required()
def pytanie_glosuj(request, pid):
    pytanie = get_object_or_404(Pytanie, pk=pid)
    if request.method == 'POST':
        try:
            odpowiedz = pytanie.odpowiedz_set.get(pk=request.POST['odpowiedz'])
        except (KeyError, Odpowiedz.DoesNotExist):
            return render(request, 'ankiety/pytanie_glosuj.html', {
                'pytanie': pytanie,
                'komunikat_bledu': 'Nie wybrałeś odpowiedzi.',
            })
        else:
            odpowiedz.glosy += 1
            odpowiedz.save()
            return redirect(reverse('ankiety:liczba-glosow', args=(pytanie.id,)))
    else:
        return render(request, 'ankiety/pytanie_glosuj.html', {'pytanie': pytanie})
