from decimal import Decimal

from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from complectations.models import Service, Complectation
from complectations.forms import ServiceForm


class ServicesViewList(ListView):
    """View вывода услуг"""
    template_name = 'complectations/service/service.html'
    model = Service
    context_object_name = 'services'

    def get_queryset(self):
        slug = self.kwargs['slug']
        # Предзагружаем complectation, чтобы избежать лишних запросов при доступе
        return Service.objects.filter(complectation__slug=slug).select_related('complectation')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']

        # Получаем объект Complectation и данные агрегатов в одном запросе
        comp = get_object_or_404(Complectation, slug=slug)

        # Агрегируем данные для цены
        prices = Service.objects.filter(complectation=comp).aggregate(
            total_price_all=Sum('price_all'),
            total_price_procent=Sum('price_procent')
        )

        # Вычисляем сумму price_all + price_procent
        total_sum = (prices['total_price_all'] or 0) + (prices['total_price_procent'] or 0)

        context.update({
            'comp_id': comp.id,
            'comp_name': comp.name,
            'comp_slug': comp.slug,
            'price_all': prices['total_price_all'],
            'price_procent': prices['total_price_procent'],
            'total_sum': total_sum,  # Добавляем новую сумму в контекст
        })

        return context


class ServicesViewPaidList(ListView):
    """View вывода оплаченных услуг"""
    pass


class ServicesViewUnpaidList(ListView):
    """View вывода не оплаченных услуг"""
    pass


class ServicesViewAdd(CreateView):
    """View добавления услуг"""
    template_name = "complectations/service/serviceadd.html"
    model = Service
    form_class = ServiceForm

    def form_valid(self, form, **kwargs):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.price_all = obj.price * obj.count
        obj.price_procent = obj.price_all * (Decimal(obj.procent) / 100)

        # Получаем Complectation по ID один раз
        comp = get_object_or_404(Complectation, id=self.kwargs['comp_id'])
        obj.complectation = comp
        self.url = comp.slug

        obj.save()  # Сохраняем объект перед возвратом родительского метода
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('serviceslistpage', kwargs={'slug': self.url})


class ServicesViewEdit(UpdateView):
    """View редактирования услуг"""
    pass


class ServicesViewDelete(DeleteView):
    """View удаления услуг"""
    pass


class ServicesViewPDF(View):
    """View вывода PDF услуг"""
    pass


class ServicesViewXlsx(View):
    """View вывода XLSX услуг"""
    pass
