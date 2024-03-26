from django.utils.translation import gettext_lazy as _


def format_time(days, seconds):
    hours = (seconds % (24 * 3600)) // 3600

    hours_form = [_("час"), _("часа"), _("часов")]
    days_form = [_("день"), _("дня"), _("дней")]

    if days > 0:
        if hours > 0:
            return f"{days} {plural_form(days, days_form)} {hours} {plural_form(hours, hours_form)}"
        else:
            return f"{days} {plural_form(days, days_form)}"
    elif hours > 0:
        return f"{hours} {plural_form(hours, hours_form)}"
    else:
        return _("Меньше часа")


def plural_form(n, forms):
    if n % 10 == 1 and n % 100 != 11:
        return forms[0]
    elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        return forms[1]
    else:
        return forms[2]
