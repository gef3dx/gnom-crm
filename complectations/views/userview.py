from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth.views import PasswordChangeView
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from complectations.forms import UserEditForm, UserCreationForm
from users.models import CustomUser


class UserViewList(ListView):
    """View для вывода пользователей"""
    template_name = 'users/user.html'
    model = CustomUser
    context_object_name = 'users'

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

    def get_queryset(self, **kwargs):
        queryset = CustomUser.objects.all()
        return queryset


class UserViewDetale(DetailView):
    """View для вывода одного пользователей"""
    model = CustomUser
    template_name = 'users/userdetail.html'
    context_object_name = 'user'


class UserViewEdit(UpdateView):
    """View для редактирования пользователей"""
    model = CustomUser
    template_name = 'users/useredit.html'
    form_class = UserEditForm
    context_object_name = 'user_edit'
    success_url = '/users/'
    success_message = 'Изменения сохранены'

    def get_object(self, queryset=None):
        return get_object_or_404(CustomUser, pk=self.kwargs['pk'])

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        # Если пароль был изменен, он уже хеширован в форме, поэтому дополнительных действий не требуется
        return super().form_valid(form)


class UserViewAdd(CreateView):
    """View для добавления пользователей"""
    model = CustomUser
    template_name = 'users/useradd.html'
    context_object_name = 'user_add'
    success_url = '/users/'
    form_class = UserCreationForm

    def form_valid(self, form):
        messages.success(self.request, 'Пользователь добавлен')
        if form.is_valid():
            try:
                obj = form.save(commit=False)
                # Присваиваем имя пользователя на основе email
                username_base = obj.email.split("@")[0]
                obj.username = username_base

                # Проверяем уникальность имени пользователя
                User = get_user_model()
                count = 1
                while User.objects.filter(username=obj.username).exists():
                    obj.username = f"{username_base}_{count}"
                    count += 1

                obj.save()
                return super().form_valid(form)
            except IntegrityError:
                form.add_error(None, "Ошибка сохранения пользователя.")
                return self.form_invalid(form)
        return super().form_invalid(form)


class UserViewDelete(DeleteView):
    """View для удаления пользователей"""
    model = CustomUser
    template_name = 'users/userdelete.html'
    context_object_name = 'user_delete'
    success_url = '/users/'

    def form_valid(self, form):
        messages.success(self.request, 'Пользователь удалён')
        return super().form_valid(form)


class UserPasswordChangeView(PasswordChangeView):
    """View для изменения пароля пользователя без проверки старого пароля"""
    template_name = 'users/userpasswordchange.html'  # Укажите свой шаблон
    form_class = SetPasswordForm  # Используем SetPasswordForm
    success_url = reverse_lazy('userpage')  # URL для перенаправления после успешного изменения

    def form_valid(self, form):
        # Сохраняем новый пароль
        user = self.request.user
        form.save(user)
        messages.success(self.request, "Пароль успешно изменён!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # Добавляем текущий контекст, если нужно
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context