from registration.backends.simple.views import RegistrationView


class AWRegistrationView(RegistrationView):
    
    
    def get_success_url(self, request, user):
        return 'item_list'