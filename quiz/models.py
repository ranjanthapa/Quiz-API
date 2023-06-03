from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Quizzes(models.Model):
    class Meta:
        ordering = ['id']
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

    title = models.CharField(max_length=225, default=_("New Quiz"), verbose_name=_("New Title"))
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=1)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Updated(models.Model):
    date_updated = models.DateTimeField(auto_now=True, verbose_name=_("Last Updated"))

    class Meta:
        abstract = True


class Question(models.Model):
    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ['id']

    SCALE = (
        (0, _('Fundamental')),
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advance')),
        (4, _('Advance')),
    )
    TYPE = (
        (0, _("Multiple Choice")),
    )
    quiz = models.ForeignKey(Quizzes, on_delete=models.DO_NOTHING, related_name='question')
    technique = models.IntegerField(default=0, choices=TYPE, verbose_name=_("Type of Question"))
    title = models.CharField(verbose_name=_("Title"), max_length=225)
    difficult = models.IntegerField(choices=SCALE, verbose_name=_("Difficulty"), default=0)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(default=False, verbose_name=_("Active Status"))

    def __str__(self):
        return self.title


class Answer(models.Model):
    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')
        ordering = ['id']

    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, related_name='answer')
    answer_text = models.CharField(max_length=225, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text