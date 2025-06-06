# Generated by Django 4.2.20 on 2025-05-31 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0004_comment_notification_reaction_report_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='公告標題')),
                ('content', models.TextField(verbose_name='公告內容')),
                ('announcement_type', models.CharField(choices=[('system', '系統公告'), ('maintenance', '系統維護'), ('update', '功能更新'), ('promotion', '活動宣傳'), ('other', '其他')], default='system', max_length=15, verbose_name='公告類型')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='發布時間')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新時間')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否啟用')),
                ('is_pinned', models.BooleanField(default=False, verbose_name='是否置頂')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='開始日期')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='結束日期')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to=settings.AUTH_USER_MODEL, verbose_name='發布者')),
            ],
            options={
                'verbose_name': '系統公告',
                'verbose_name_plural': '系統公告',
                'ordering': ['-is_pinned', '-created_at'],
            },
        ),
    ]
