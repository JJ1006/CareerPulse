from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_layoffprediction_education_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layoffprediction',
            name='department',
            field=models.IntegerField(choices=[(0, 'Defence'), (1, 'Human Resources'), (2, 'IT department'), (3, 'Research & Development'), (4, 'Sales'), (5, 'Tech Development')], default=0),
        ),
        migrations.AlterField(
            model_name='layoffprediction',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Male'), (1, 'Female'), (2, 'Other')], default=0),
        ),
        migrations.AlterField(
            model_name='layoffprediction',
            name='industry',
            field=models.IntegerField(choices=[(0, 'Aerospace'), (1, 'Education'), (2, 'Finance'), (3, 'Fitness'), (4, 'Food'), (5, 'Healthcare'), (6, 'Logistics'), (7, 'Real Estate'), (8, 'Retail'), (9, 'Sales'), (10, 'Transportation'), (11, 'Travel')], default=0),
        ),
        migrations.AlterField(
            model_name='layoffprediction',
            name='job_role',
            field=models.IntegerField(choices=[(0, 'Healthcare Representative'), (1, 'Human Resources'), (2, 'Laboratory Technician'), (3, 'Network Engineer'), (4, 'Operational Executive'), (5, 'Project Manager'), (6, 'Research Director'), (7, 'Research Scientist'), (8, 'Sales Executive'), (9, 'Sales Representative'), (10, 'Software Developer'), (11, 'Team Lead')], default=0),
        ),
        migrations.AlterField(
            model_name='layoffprediction',
            name='stage',
            field=models.IntegerField(choices=[(0, 'Acquired'), (1, 'Post-IPO'), (2, 'Private Equity'), (3, 'Seed'), (4, 'Series A'), (5, 'Series B'), (6, 'Series C'), (7, 'Series D'), (8, 'Series E'), (9, 'Series F'), (10, 'Series G'), (11, 'Series H'), (12, 'Series I'), (13, 'Series J'), (14, 'Subsidiary'), (15, 'Unknown')], default=0),
        ),
    ]
