from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class MessageManager(models.Manager):
    def get_queryset(self):
        return super(MessageManager, self).get_queryset().filter(status='unread')


class Message(models.Model):

    ANSWER_CHOICES = (
        ('ans_this_wk', 'this_week'),
        ('ans_this_wk<18', 'this_week<18'),
        ('ans_mr_this_wk', 'mr_this_week'),
        ('ans_ms_this_wk', 'ms_this_week'),
        ('ans_next_wk', 'next_week'),
        ('ans_next_wk<18', 'next_week<18'),
        ('ans_mr_next_wk', 'mr_next_week'),
        ('ans_ms_next_wk', 'ms_next_week'),
        ('ans_other_term', 'other_term'),
        ('ans_other_term_mr', 'mr_other_term'),
        ('ans_other_term_ms', 'ms_other_term'),
        ('ans_office', 'office'),
        ('inv_m_orday', 'inv_m'),
        ('inv_m_wknday', 'inv_m_wknd'),
        ('inv_f_orday', 'inv_f'),
        ('inv_f_wknday', 'inv_f_wknd'),
        ('inv_mr_orday', 'inv_mr'),
        ('inv_mr_wknday', 'inv_mr_wknd'),
        ('inv_ms_orday', 'inv_ms'),
        ('inv_ms_wknday', 'inv_ms_wknd'),
        ('inv_scnd', 'inv_rptd'),
        ('inv_mr_scnd', 'inv_mr_rptd'),
        ('inv_ms_scnd', 'inv_ms_rptd'),
        ('ans_blank', 'manual'),  # to discuss
    )

    selected = models.BooleanField(default=False)
    ans_choice = models.TextField(choices=ANSWER_CHOICES, default='ans_this_wk')
    author = models.CharField(max_length=50)
    msg_body = models.TextField()
    msg_date = models.DateTimeField(default=timezone.now)  # ultimate date of incoming how to?
    date_hierarchy = 'ad_date'
    # answer = models.TextField()
    status = models.CharField(max_length=10, default='incoming')
    objects = models.Manager()
    incoming = MessageManager()

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
            return self.msg_date


class Answer(models.Model):
    tmp_desc = models.CharField(max_length=20)
    tmp_body = models.TextField()
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
            return self.tmp_desc


