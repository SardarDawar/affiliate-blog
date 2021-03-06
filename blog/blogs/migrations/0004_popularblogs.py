# Generated by Django 2.2.4 on 2021-05-24 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_subcategory_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopularBlogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Blog')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Category')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.SubCategory')),
            ],
        ),
    ]
