from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from complectations.forms import ComplectationForm
from complectations.models import Complectation


class ComplectationsViewHome(ListView):
    """View для вывода комплектации на главной странице"""
    model = Complectation
    template_name = "complectations/home.html"
    context_object_name = "complectations"


class ComplectationViewAdd(CreateView):
    """View для добавления комплектации"""
    template_name = "complectations/complectationadd.html"
    model = Complectation
    form_class = ComplectationForm
    success_url = "/"

    def form_valid(self, form):
        messages.success(self.request, "Комплектация добавлена!")
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


class ComplectationViewEdit(UpdateView):
    """View для редактирования комплектации"""
    template_name = "complectations/complectationedit.html"
    model = Complectation
    form_class = ComplectationForm
    success_url = "/"

    def form_valid(self, form):
        messages.success(self.request, "Комплектация сохранена!")
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


class ComplectationViewDelete(DeleteView):
    """View для удаления комплектации"""
    model = Complectation
    success_url = "/"
    template_name = "complectations/complectationdelete.html"

    def form_valid(self, form):
        messages.success(self.request, "Комплектация удалена!")
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

