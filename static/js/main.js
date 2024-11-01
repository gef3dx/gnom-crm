"use strict";

/* Aside & Navbar: dropdowns */
Array.from(document.getElementsByClassName('dropdown')).forEach(function (elA) {
  elA.addEventListener('click', function (e) {
    if (e.currentTarget.classList.contains('navbar-item')) {
      e.currentTarget.classList.toggle('active');
    } else {
      var dropdownIcon = e.currentTarget.getElementsByClassName('mdi')[1];
      e.currentTarget.parentNode.classList.toggle('active');
      dropdownIcon.classList.toggle('mdi-plus');
      dropdownIcon.classList.toggle('mdi-minus');
    }
  });
});
/* Aside Mobile toggle */

Array.from(document.getElementsByClassName('mobile-aside-button')).forEach(function (el) {
  el.addEventListener('click', function (e) {
    var dropdownIcon = e.currentTarget.getElementsByClassName('icon')[0].getElementsByClassName('mdi')[0];
    document.documentElement.classList.toggle('aside-mobile-expanded');
    dropdownIcon.classList.toggle('mdi-forwardburger');
    dropdownIcon.classList.toggle('mdi-backburger');
  });
});
/* NavBar menu mobile toggle */

Array.from(document.getElementsByClassName('--jb-navbar-menu-toggle')).forEach(function (el) {
  el.addEventListener('click', function (e) {
    var dropdownIcon = e.currentTarget.getElementsByClassName('icon')[0].getElementsByClassName('mdi')[0];
    document.getElementById(e.currentTarget.getAttribute('data-target')).classList.toggle('active');
    dropdownIcon.classList.toggle('mdi-dots-vertical');
    dropdownIcon.classList.toggle('mdi-close');
  });
});
/* Modal: open */

Array.from(document.getElementsByClassName('--jb-modal')).forEach(function (el) {
  el.addEventListener('click', function (e) {
    var modalTarget = e.currentTarget.getAttribute('data-target');
    document.getElementById(modalTarget).classList.add('active');
    document.documentElement.classList.add('clipped');
  });
});
/* Modal: close */

Array.from(document.getElementsByClassName('--jb-modal-close')).forEach(function (el) {
  el.addEventListener('click', function (e) {
    e.currentTarget.closest('.modal').classList.remove('active');
    document.documentElement.classList.remove('is-clipped');
  });
});
/* Notification dismiss */

Array.from(document.getElementsByClassName('--jb-notification-dismiss')).forEach(function (el) {
  el.addEventListener('click', function (e) {
    e.currentTarget.closest('.notification').classList.add('hidden');
  });
});

document.addEventListener("DOMContentLoaded", function () {
    // Находим все input с классом "formatted-input"
    document.querySelectorAll('.formatted-input').forEach((input) => {
        input.addEventListener("input", function () {
            let value = this.value;

            // Удаляем все нечисловые символы, кроме запятой и точки
            value = value.replace(/[^\d.,]/g, "");

            // Если пользователь ввел запятую, заменяем её на точку
            value = value.replace(",", ".");

            // Разделяем на целую и десятичную часть (если есть)
            let parts = value.split(".");
            let integerPart = parts[0];
            let decimalPart = parts[1] !== undefined ? '.' + parts[1].slice(0, 2) : '';

            // Форматируем целую часть числа, добавляя пробелы после каждой тройки цифр
            integerPart = integerPart.replace(/\B(?=(\d{3})+(?!\d))/g, "'");

            // Сохраняем позицию курсора
            let cursorPosition = this.selectionStart;

            // Обновляем значение поля с форматированием
            this.value = integerPart + decimalPart;

            // Восстанавливаем позицию курсора
            this.setSelectionRange(cursorPosition, cursorPosition);
        });

        // Убираем форматирование и преобразуем в число перед отправкой формы
        input.form.addEventListener("submit", function () {
            input.value = parseFloat(input.value.replace(/\s|'/g, "").replace(",", ".")) || 0;
        });
    });
});