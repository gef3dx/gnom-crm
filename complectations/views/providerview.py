from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from complectations.forms import ProviderForm
from complectations.models import Provider


class ProviderViewList(ListView):
    """View для вывода поставщиков"""
    model = Provider
    template_name = "complectations/provider/provider.html"
    context_object_name = "providers"


class ProviderViewAdd(CreateView):
    """View для добавления поставщиков"""
    template_name = "complectations/provider/provideradd.html"
    model = Provider
    form_class = ProviderForm
    success_url = "/providers/"

    def form_valid(self, form):
        messages.success(self.request, "Поставщик добавлен!")
        return super().form_valid(form)

    # def get(self, request, *args, **kwargs):
    #     if self.request.user.is_staff:
    #         self.object = None
    #         return super().get(request, *args, **kwargs)
    #     else:
    #         return redirect('home')
    #
    # def post(self, request, *args, **kwargs):
    #     if self.request.user.is_staff:
    #         self.object = None
    #         return super().post(request, *args, **kwargs)
    #     else:
    #         return redirect('home')


class ProviderViewEdit(UpdateView):
    """View для редактирования поставщиков"""
    template_name = "complectations/provider/provideredit.html"
    model = Provider
    form_class = ProviderForm
    success_url = "/providers/"

    def form_valid(self, form):
        messages.success(self.request, "Поставщик сохранен!")
        return super().form_valid(form)

    # def get(self, request, *args, **kwargs):
    #     if self.request.user.is_staff:
    #         self.object = None
    #         return super().get(request, *args, **kwargs)
    #     else:
    #         return redirect('home')
    #
    # def post(self, request, *args, **kwargs):
    #     if self.request.user.is_staff:
    #         self.object = None
    #         return super().post(request, *args, **kwargs)
    #     else:
    #         return redirect('home')


class ProviderViewDelete(DeleteView):
    """View для удаления поставщиков"""
    model = Provider
    template_name = "complectations/provider/providerdelete.html"
    success_url = "/providers/"

    def form_valid(self, form):
        messages.success(self.request, "Поставщик удален!")
        return super().form_valid(form)

    # def get(self, request, *args, **kwargs):
    #     if self.request.user.is_staff:
    #         self.object = None
    #         return super().get(request, *args, **kwargs)
    #     else:
    #         return redirect('home')
    #
    # def post(self, request, *args, **kwargs):
    #     if self.request.user.is_staff:
    #         self.object = None
    #         return super().post(request, *args, **kwargs)
    #     else:
    #         return redirect('home')
