from django.db import models
from django.contrib.auth.models import User


class IventUserProfile(models.Model):
    user = models.ForeignKey(User, verbose_name='Участник', on_delete=models.CASCADE)
    name = models.CharField("Прогресс пользователей", max_length=150, )
    description = models.TextField("Описание")
    # url = models.SlugField(max_length=150, unique=True)
    DateCheck = models.DateField(verbose_name="Дата фиксации", auto_now=True)  # Дата фиксации результата
    Weight = models.IntegerField(null=True)  # Вес
    Growth = models.IntegerField(null=True)  # Рост

    class Meta:
        verbose_name = "Прогресс пользователей"
        verbose_name_plural = "Прогресс пользователей"

    def __str__(self):
        return self.name

    def all_images(self):
        all_images = IventUserProfile_photo.objects.filter(IventUserProfile=self)
        return all_images


class IventUserProfile_photo(models.Model):
    image = models.ImageField("Изображение", upload_to='PhotoUsers')
    IventUserProfile = models.ForeignKey(IventUserProfile, on_delete=models.CASCADE, related_name='images')


class ivent(models.Model):
    name = models.CharField("Соревнование", max_length=150)
    description = models.TextField("Описание")
    #  url = models.SlugField(max_length=150, unique=True)
    data_start = models.DateField(verbose_name="Дата старта")
    data_stop = models.DateField(verbose_name="Дата окончания")
    users = models.ManyToManyField(User, verbose_name="Участники")
    IventUserProfils = models.ManyToManyField(IventUserProfile, verbose_name="Профиль участника", blank=True)
    image_logo = models.ImageField("Изображение комнаты", upload_to='IventLogo', default='IventLogo/def.png',
                                   blank=True)

    class Meta:
        verbose_name = "Соревнование"
        verbose_name_plural = "Соревнования"

    def __str__(self):
        return self.name

    def get_IventUserProfils(self):
        return self.IventUserProfils.all()

    def get_users(self):
        users = []
        for user in self.users.all():
            users.append(user.username)
        return users

    def get_IventUserProfils_image(self):
        spisok = []
        prof = self.IventUserProfils.all()
        for profile in prof:
            x = IventUserProfile_photo.objects.get(IventUserProfile=profile)
            spisok.append(x)
        return spisok
