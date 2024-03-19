from django.utils.translation import activate


class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language_cookie = request.COOKIES.get('lang')
        if language_cookie:
            activate(language_cookie)
        response = self.get_response(request)
        return response
