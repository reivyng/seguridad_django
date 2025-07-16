from api.models import User

def get_all_users():
    return User.objects.all()
