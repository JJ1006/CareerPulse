from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_layoffprediction_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layoffprediction',
            name='education_field',
            field=models.IntegerField(choices=[(0, 'Human Resources'), (1, 'Life Sciences'), (2, 'Marketing'), (3, 'Medical'), (4, 'Other'), (5, 'Technical Degree')], default=0),
        ),
    ]
