# Generated by Django 2.2.12 on 2022-04-10 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_books_tosell_borrowed_books_customers_ebooks_librarians_overdue_books_reviews_toreadlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books_tosell',
            name='isbn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.books_details'),
        ),
        migrations.AlterField(
            model_name='borrowed_books',
            name='isbn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.books_details'),
        ),
        migrations.AlterField(
            model_name='ebooks',
            name='isbn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.books_details'),
        ),
        migrations.AlterField(
            model_name='overdue_books',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.customers'),
        ),
        migrations.AlterField(
            model_name='overdue_books',
            name='isbn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.books_details'),
        ),
        migrations.AlterField(
            model_name='overdue_books',
            name='librarian_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.librarians'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='isbn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.books_details'),
        ),
        migrations.AlterField(
            model_name='toreadlist',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.customers'),
        ),
        migrations.AlterField(
            model_name='toreadlist',
            name='isbn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.books_details'),
        ),
    ]
