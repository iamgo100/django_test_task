from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField('Название пункта', help_text='Название, которое будет отображено пользователям', max_length=100)
    url = models.CharField('Ссылка, куда будет вести пункт меню', max_length=250)
    position = models.PositiveIntegerField('Позиция пункта в меню')
    code_name = models.CharField(
        'Кодовое название меню/подменю', 
        help_text='По этому названию будет вызываться меню в коде. Необязательное поле', 
        max_length=50,
        blank=True
    )
    parent = models.ForeignKey(
        'self',
        verbose_name='Родительский пункт меню',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )

    # Данное поле было упразднено и заменено на поле выше с целью сокращения запросов к БД
    # childs = models.ManyToManyField(
    #     'self',
    #     verbose_name='Выберите пункты данного меню/подменю',
    #     blank=True,
    #     symmetrical=False
    # )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
