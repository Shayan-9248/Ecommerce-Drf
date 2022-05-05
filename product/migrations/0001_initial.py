# Generated by Django 4.0.4 on 2022-05-05 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("slug", models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated", models.DateTimeField(auto_now=True, null=True)),
                ("title", models.CharField(blank=True, max_length=50, null=True)),
                ("slug", models.SlugField(blank=True, null=True, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("available", models.BooleanField(default=True)),
                ("unit_price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("amount", models.PositiveIntegerField(blank=True, null=True)),
                ("discount", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "total_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=6, null=True
                    ),
                ),
                ("image", models.ImageField(default="1.jpg", upload_to="")),
                ("sell", models.PositiveIntegerField(default=0)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="product.category",
                    ),
                ),
                (
                    "dislike",
                    models.ManyToManyField(
                        blank=True,
                        related_name="p_dislike",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "favourite",
                    models.ManyToManyField(
                        blank=True, related_name="fav", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "like",
                    models.ManyToManyField(
                        blank=True, related_name="p_like", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "ordering": ("-created",),
                "abstract": False,
            },
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(fields=["title"], name="product_pro_title_07e491_idx"),
        ),
    ]
