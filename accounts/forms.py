from .models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm): # 장고가 만들어놓은것
    class Meta(): # 얘가 대체 뭘 보여주냐 !
        model = User # 얘만 바꿈 !
        # fields = '__all__'
        fields = ('username', )