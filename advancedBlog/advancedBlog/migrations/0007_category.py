# Generated by Django 5.0b1 on 2024-03-20 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advancedBlog', '0006_post_category_alter_post_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=150)),
            ],
        ),
    ]