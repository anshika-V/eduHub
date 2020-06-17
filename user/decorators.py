from django.http import HttpResponseForbidden


# Decorotor to allow only instructor to view certail views use it after the login_required
def allow_instructor(func):
    def inner(request, *args, **kwargs):
        profile = request.user.profile
        if (profile.type != 'I'):
            return HttpResponseForbidden('Unauthorised Access: Only instructors are allowed to access this view')
        return func(request, *args, **kwargs)
    return inner
