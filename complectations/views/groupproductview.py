from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from complectations.forms import GroupForm
from complectations.models import GroupProduct


class GroupProductViewList(ListView):
    """View для вывода групп по которой сортируются продукты"""
    model = GroupProduct
    template_name = "complectations/group/group.html"
    context_object_name = "groups"


class GroupProductViewAdd(CreateView):
    """View для добавления групп"""
    template_name = "complectations/group/groupadd.html"
    model = GroupProduct
    form_class = GroupForm
    success_url = "/groups/"

    def form_valid(self, form):
        messages.success(self.request, "Группа добавлена!")
        return super().form_valid(form)


class GroupProductViewEdit(UpdateView):
    """View для редактирования групп"""
    template_name = "complectations/group/groupedit.html"
    model = GroupProduct
    form_class = GroupForm
    success_url = "/groups/"

    def form_valid(self, form):
        messages.success(self.request, "Группа изменена!")
        return super().form_valid(form)


class GroupProductViewDelete(DeleteView):
    """View для редактирования групп"""
    template_name = "complectations/group/groupdelete.html"
    model = GroupProduct
    success_url = "/groups/"

    def form_valid(self, form):
        messages.success(self.request, "Группа удалена!")
        return super().form_valid(form)
