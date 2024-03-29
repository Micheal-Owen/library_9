
import books.models
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
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('education', 'Education'), ('comics', 'Comics'), ('biography', 'Biography'), ('history', 'History'), ('novel', 'Novel'), ('fantasy', 'Fantasy'), ('thriller', 'Thriller'), ('romance', 'Romance'), ('scifi', 'Sci-Fi')], max_length=40)),
                ('status', models.BooleanField(default=True)),
                ('description', models.TextField(max_length=3000)),
                ('image', models.ImageField(blank=True, upload_to='pics')),
            ],
            options={
                'verbose_name_plural': 'books',
            },
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('username', models.CharField(max_length=300)),
                ('book_name', models.CharField(max_length=300)),
                ('reg_no', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'borrowers',
            },
        ),
        migrations.CreateModel(
            name='IssuedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(max_length=200)),
                ('issued_date', models.DateField(auto_now=True)),
                ('return_date', models.DateField(auto_now=True)),
                ('book_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('borrower', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.borrower')),
            ],
            options={
                'verbose_name_plural': 'issuedbooks',
            },
        ),
        migrations.CreateModel(
            name='RequestedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200)),
                ('return_date', models.DateField(default=books.models.get_return_date)),
                ('pickup_time', models.DateTimeField(default=books.models.book_time_limit)),
                ('borrower', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'requestedbooks',
            },
        ),
        migrations.CreateModel(
            name='Returned_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_return', models.DateTimeField(auto_now=True)),
                ('reg_no', models.BigIntegerField()),
                ('return_date', models.DateField(auto_now=True)),
                ('book_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.issuedbook')),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.borrower')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
