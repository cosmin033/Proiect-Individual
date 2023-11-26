# Generated by Django 4.2.4 on 2023-09-07 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0020_booking_coupons'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='used_by',
        ),
        migrations.CreateModel(
            name='CouponUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
                ('mobile', models.CharField(max_length=1000)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.booking')),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.coupon')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
