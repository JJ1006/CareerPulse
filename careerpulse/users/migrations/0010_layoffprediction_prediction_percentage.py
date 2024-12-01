from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_layoffprediction_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='layoffprediction',
            name='prediction_percentage',
            field=models.FloatField(default='0'),
            preserve_default=False,
        ),
    ]
