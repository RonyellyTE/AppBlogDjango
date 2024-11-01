from django.shortcuts import render


def user_profile_view(request):
    return render(request,
                  template_name="user/profile.html",
                  context={
                      'name':'Area do Usuário'
                  })
