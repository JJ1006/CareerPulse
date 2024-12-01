from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='LayoffPrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('education_field', models.IntegerField(choices=[(0, 'Human Resources'), (1, 'Life Sciences'), (2, 'Marketing'), (3, 'Medical'), (4, 'Other'), (5, 'Technical Degree')])),
                ('job_role', models.IntegerField(choices=[(0, 'Healthcare Representative'), (1, 'Human Resources'), (2, 'Laboratory Technician'), (3, 'Network Engineer'), (4, 'Operational Executive'), (5, 'Project Manager'), (6, 'Research Director'), (7, 'Research Scientist'), (8, 'Sales Executive'), (9, 'Sales Representative'), (10, 'Software Developer'), (11, 'Team Lead')])),
                ('department', models.IntegerField(choices=[(0, 'Defence'), (1, 'Human Resources'), (2, 'IT department'), (3, 'Research & Development'), (4, 'Sales'), (5, 'Tech Development')])),
                ('industry', models.IntegerField(choices=[(0, 'Aerospace'), (1, 'Education'), (2, 'Finance'), (3, 'Fitness'), (4, 'Food'), (5, 'Healthcare'), (6, 'Logistics'), (7, 'Real Estate'), (8, 'Retail'), (9, 'Sales'), (10, 'Transportation'), (11, 'Travel')])),
                ('stage', models.IntegerField(choices=[(0, 'Acquired'), (1, 'Post-IPO'), (2, 'Private Equity'), (3, 'Seed'), (4, 'Series A'), (5, 'Series B'), (6, 'Series C'), (7, 'Series D'), (8, 'Series E'), (9, 'Series F'), (10, 'Series G'), (11, 'Series H'), (12, 'Series I'), (13, 'Series J'), (14, 'Subsidiary'), (15, 'Unknown')])),
                ('education', models.IntegerField()),
                ('funds_raised', models.DecimalField(decimal_places=2, max_digits=10)),
                ('performance_rating', models.IntegerField()),
                ('job_satisfaction', models.IntegerField()),
                ('job_involvement', models.IntegerField()),
                ('years_at_company', models.IntegerField()),
                ('years_in_current_role', models.IntegerField()),
                ('years_with_curr_manager', models.IntegerField()),
                ('monthly_income', models.IntegerField()),
                ('num_companies_worked', models.IntegerField()),
                ('gender', models.IntegerField(choices=[(0, 'Female'), (1, 'Male'), (2, 'Other')])),
            ],
        ),
    ]
