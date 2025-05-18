from django.db import models
from django.contrib.auth.models import User


class Ad(models.Model):
    class Condition(models.TextChoices):
        NEW = "new", "Новый"
        USED = "used", "Б/у"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="ads",
        verbose_name="владелец",
    )
    title = models.CharField("Заголовок", max_length=200)
    description = models.TextField("Описание")
    image_url = models.URLField("URL изображения", max_length=500, blank=True)
    category = models.CharField("Категория", max_length=100)
    condition = models.CharField(
        "Состояние",
        max_length=20,
        choices=Condition.choices,
        default=Condition.USED,
    )
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.user.username})"


class ExchangeProposal(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Ожидает"
        ACCEPTED = "accepted", "Принята"
        DECLINED = "declined", "Отклонена"

    ad_sender = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        related_name="sent_proposals",
        verbose_name="отправитель",
    )
    ad_receiver = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        related_name="received_proposals",
        verbose_name="получатель",
    )
    comment = models.TextField("Комментарий", blank=True)
    status = models.CharField(
        "статус",
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
    )
    created_at = models.DateTimeField("Дата предложения", auto_now_add=True)

    def __str__(self):
        return f"{self.ad_sender} → {self.ad_receiver} [{self.get_status_display()}]"
