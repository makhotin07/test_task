from django.db import models
from django.conf import settings
from django.urls import reverse


class TypeTicket(models.Model):
    name = models.TextField(max_length=40, verbose_name='Тип заявки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип заявки'
        verbose_name_plural = 'Типы заявки'


class Ticket(models.Model):
    class Priority(models.TextChoices):
        LOW = 'LO', 'Низкий'
        MEDIUM = 'ME', 'Средний'
        HIGH = 'HI', 'Высокий'

    class Status(models.TextChoices):
        REFUSED = 'RE', 'Отказано'
        ACCEPTED = 'AC', 'Принято'
        EXECUTED = 'EX', 'Исполнено'

    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    organization_name = models.CharField(max_length=255,verbose_name='Наименование организации')
    applicant = models.CharField(max_length=255, verbose_name='Заявитель')
    priority = models.CharField(
        max_length=2,
        choices=Priority.choices,
        default=Priority.MEDIUM,verbose_name='Уровень приоритета'
    )
    type = models.ForeignKey(
        TypeTicket, on_delete=models.SET_NULL, blank=True, null=True,verbose_name='Тип заявки'
    )
    ticket_name = models.CharField(max_length=255, verbose_name='Наименование заявки')
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.ACCEPTED,
        verbose_name='Статус заявки'
    )
    executor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name= 'Исполнитель'
    )

    def __str__(self):
        return f"""Id: {self.id} Название: {self.ticket_name}"""

    def get_absolute_url(self):
        return reverse("ticket_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'