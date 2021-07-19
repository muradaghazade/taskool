from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(('email adress'), unique=True, null=True)
    password2 = models.CharField(('password2'), max_length=200)
    age = models.IntegerField('Age',blank=True,null=True)
    is_teacher = models.BooleanField('is Teacher',default=0)
    is_student = models.BooleanField('is Student',default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        if self.is_teacher:
            print("Taskool'da ilk Kursunuzu yaradin!")
            send_mail("Taskool'da ilk Kursunuzu yaradin!", f'Sizin Instructor hesabiniz qəbul edilmişdir! Taskool heabizina daxil olun ve öz kurslarinizi yaradmaqa başlayin!\nhttps://taskool.com/login', 'husubayli@gmail.com', [self.email,])
        else:
            print("Sizin Instructor hesabiniz baxişdadir!")
            send_mail('Sizin Instructor hesabiniz baxişdadir!', f'Sizin Instructor hesabiniz baxişdadi!\nZəhmət olmasa hesabiniz qəbul olunana qədər gözləyin.', 'husubayli@gmail.com', [self.email,])
        # super(User, self).save(*args, **kwargs)