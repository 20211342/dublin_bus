# Generated by Django 4.0.5 on 2022-07-14 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HistWeather',
            fields=[
                ('id_hist_weather', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(blank=True, max_length=45, null=True, unique=True)),
                ('indicator', models.IntegerField(blank=True, null=True)),
                ('precip_amt', models.FloatField(blank=True, null=True)),
                ('indicator2', models.IntegerField(blank=True, null=True)),
                ('temp', models.FloatField(blank=True, null=True)),
                ('indicator3', models.IntegerField(blank=True, null=True)),
                ('wet_bulb_temp', models.FloatField(blank=True, null=True)),
                ('dew_pt_temp', models.FloatField(blank=True, null=True)),
                ('vapor_pressure', models.FloatField(blank=True, null=True)),
                ('relative_humid', models.IntegerField(blank=True, null=True)),
                ('mean_sea_level_pressure', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'hist_weather',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HistWeatherOw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_ow', models.IntegerField(blank=True, null=True)),
                ('dt', models.IntegerField(blank=True, null=True)),
                ('dt_iso', models.TextField(blank=True, null=True)),
                ('timezone', models.IntegerField(blank=True, null=True)),
                ('city_name', models.TextField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('temp', models.FloatField(blank=True, null=True)),
                ('visibility', models.IntegerField(blank=True, null=True)),
                ('dew_point', models.FloatField(blank=True, null=True)),
                ('feels_like', models.FloatField(blank=True, null=True)),
                ('temp_min', models.FloatField(blank=True, null=True)),
                ('temp_max', models.FloatField(blank=True, null=True)),
                ('pressure', models.IntegerField(blank=True, null=True)),
                ('sea_level', models.TextField(blank=True, null=True)),
                ('grnd_level', models.TextField(blank=True, null=True)),
                ('humidity', models.IntegerField(blank=True, null=True)),
                ('wind_speed', models.FloatField(blank=True, null=True)),
                ('wind_deg', models.IntegerField(blank=True, null=True)),
                ('wind_gust', models.TextField(blank=True, null=True)),
                ('rain_1h', models.TextField(blank=True, null=True)),
                ('rain_3h', models.TextField(blank=True, null=True)),
                ('snow_1h', models.TextField(blank=True, null=True)),
                ('snow_3h', models.TextField(blank=True, null=True)),
                ('clouds_all', models.IntegerField(blank=True, null=True)),
                ('weather_id', models.IntegerField(blank=True, null=True)),
                ('weather_main', models.TextField(blank=True, null=True)),
                ('weather_description', models.TextField(blank=True, null=True)),
                ('weather_icon', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'hist_weather_ow',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Import',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_hist_weather', models.IntegerField(blank=True, null=True)),
                ('date', models.TextField(blank=True, null=True)),
                ('indicator', models.IntegerField(blank=True, null=True)),
                ('precip_amt', models.IntegerField(blank=True, null=True)),
                ('indicator2', models.IntegerField(blank=True, null=True)),
                ('temp', models.FloatField(blank=True, null=True)),
                ('indicator3', models.IntegerField(blank=True, null=True)),
                ('wet_bulb_temp', models.FloatField(blank=True, null=True)),
                ('dew_pt_temp', models.FloatField(blank=True, null=True)),
                ('vapor_pressure', models.FloatField(blank=True, null=True)),
                ('relative_humid', models.IntegerField(blank=True, null=True)),
                ('mean_sea_level_pressure', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'import',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Justifications',
            fields=[
                ('justificationid', models.IntegerField(db_column='JUSTIFICATIONID', primary_key=True, serialize=False)),
                ('justificationtype', models.CharField(blank=True, db_column='JUSTIFICATIONTYPE', max_length=45, null=True)),
                ('operatorid', models.CharField(blank=True, db_column='OPERATORID', max_length=45, null=True)),
                ('description', models.CharField(blank=True, db_column='DESCRIPTION', max_length=45, null=True)),
                ('lastupdate', models.CharField(blank=True, db_column='LASTUPDATE', max_length=45, null=True)),
                ('note', models.CharField(blank=True, db_column='NOTE', max_length=45, null=True)),
            ],
            options={
                'db_table': 'justifications',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Leavetimes',
            fields=[
                ('leaveid', models.IntegerField(db_column='leaveID', primary_key=True, serialize=False)),
                ('datasource', models.CharField(blank=True, db_column='DATASOURCE', max_length=10, null=True)),
                ('dayofservice', models.CharField(blank=True, db_column='DAYOFSERVICE', max_length=45, null=True)),
                ('tripid', models.IntegerField(blank=True, db_column='TRIPID', null=True)),
                ('progrnumber', models.IntegerField(blank=True, db_column='PROGRNUMBER', null=True)),
                ('stoppointid', models.IntegerField(blank=True, db_column='STOPPOINTID', null=True)),
                ('plannedtime_arr', models.IntegerField(blank=True, db_column='PLANNEDTIME_ARR', null=True)),
                ('plannedtime_dep', models.IntegerField(blank=True, db_column='PLANNEDTIME_DEP', null=True)),
                ('actualtime_arr', models.IntegerField(blank=True, db_column='ACTUALTIME_ARR', null=True)),
                ('actualtime_dep', models.IntegerField(blank=True, db_column='ACTUALTIME_DEP', null=True)),
                ('vehicleid', models.IntegerField(blank=True, db_column='VEHICLEID', null=True)),
                ('passengers', models.IntegerField(blank=True, db_column='PASSENGERS', null=True)),
                ('passengersin', models.IntegerField(blank=True, db_column='PASSENGERSIN', null=True)),
                ('passengersout', models.IntegerField(blank=True, db_column='PASSENGERSOUT', null=True)),
                ('distance', models.IntegerField(blank=True, db_column='DISTANCE', null=True)),
                ('suppressed', models.IntegerField(blank=True, db_column='SUPPRESSED', null=True)),
                ('justificationid', models.IntegerField(blank=True, db_column='JUSTIFICATIONID', null=True)),
                ('lastupdate', models.CharField(blank=True, db_column='LASTUPDATE', max_length=45, null=True)),
                ('note', models.CharField(blank=True, db_column='NOTE', max_length=45, null=True)),
            ],
            options={
                'db_table': 'leavetimes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LeavetimesImport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaveid', models.IntegerField(blank=True, db_column='leaveID', null=True)),
                ('datasource', models.TextField(blank=True, db_column='DATASOURCE', null=True)),
                ('dayofservice', models.TextField(blank=True, db_column='DAYOFSERVICE', null=True)),
                ('tripid', models.IntegerField(blank=True, db_column='TRIPID', null=True)),
                ('progrnumber', models.IntegerField(blank=True, db_column='PROGRNUMBER', null=True)),
                ('stoppointid', models.IntegerField(blank=True, db_column='STOPPOINTID', null=True)),
                ('plannedtime_arr', models.IntegerField(blank=True, db_column='PLANNEDTIME_ARR', null=True)),
                ('plannedtime_dep', models.IntegerField(blank=True, db_column='PLANNEDTIME_DEP', null=True)),
                ('actualtime_arr', models.IntegerField(blank=True, db_column='ACTUALTIME_ARR', null=True)),
                ('actualtime_dep', models.IntegerField(blank=True, db_column='ACTUALTIME_DEP', null=True)),
                ('vehicleid', models.IntegerField(blank=True, db_column='VEHICLEID', null=True)),
                ('passengers', models.BigIntegerField(blank=True, db_column='PASSENGERS', null=True)),
                ('passengersin', models.BigIntegerField(blank=True, db_column='PASSENGERSIN', null=True)),
                ('passengersout', models.BigIntegerField(blank=True, db_column='PASSENGERSOUT', null=True)),
                ('distance', models.BigIntegerField(blank=True, db_column='DISTANCE', null=True)),
                ('suppressed', models.BigIntegerField(blank=True, db_column='SUPPRESSED', null=True)),
                ('justificationid', models.BigIntegerField(blank=True, db_column='JUSTIFICATIONID', null=True)),
                ('lastupdate', models.TextField(blank=True, db_column='LASTUPDATE', null=True)),
                ('note', models.TextField(blank=True, db_column='NOTE', null=True)),
            ],
            options={
                'db_table': 'leavetimes_import',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LineStop',
            fields=[
                ('line_stop_id', models.IntegerField(db_column='line_stop_ID', primary_key=True, serialize=False)),
                ('lineid', models.IntegerField(blank=True, db_column='LINEID', null=True)),
                ('stoppointid', models.IntegerField(blank=True, db_column='STOPPOINTID', null=True)),
            ],
            options={
                'db_table': 'line_stop',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RawData',
            fields=[
                ('rawid', models.IntegerField(db_column='rawID', primary_key=True, serialize=False)),
                ('datasource', models.CharField(blank=True, db_column='DATASOURCE', max_length=45, null=True)),
                ('dayofservice', models.CharField(blank=True, db_column='DAYOFSERVICE', max_length=45, null=True)),
                ('vehicleid', models.IntegerField(blank=True, db_column='VEHICLEID', null=True)),
                ('timepos', models.CharField(blank=True, db_column='TIMEPOS', max_length=45, null=True)),
                ('posx', models.IntegerField(blank=True, db_column='POSX', null=True)),
                ('posy', models.IntegerField(blank=True, db_column='POSY', null=True)),
                ('odometer', models.IntegerField(blank=True, db_column='ODOMETER', null=True)),
                ('tripid', models.IntegerField(blank=True, db_column='TRIPID', null=True)),
                ('tripodometer', models.IntegerField(blank=True, db_column='TRIPODOMETER', null=True)),
                ('passengersin', models.IntegerField(blank=True, db_column='PASSENGERSIN', null=True)),
                ('passengersout', models.IntegerField(blank=True, db_column='PASSENGERSOUT', null=True)),
            ],
            options={
                'db_table': 'raw_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datasource', models.TextField(blank=True, db_column='DATASOURCE', null=True)),
                ('dayofservice', models.TextField(blank=True, db_column='DAYOFSERVICE', null=True)),
                ('vehicleid', models.IntegerField(blank=True, db_column='VEHICLEID', null=True)),
                ('distance', models.IntegerField(blank=True, db_column='DISTANCE', null=True)),
                ('minutes', models.IntegerField(blank=True, db_column='MINUTES', null=True)),
                ('lastupdate', models.TextField(blank=True, db_column='LASTUPDATE', null=True)),
                ('note', models.TextField(blank=True, db_column='NOTE', null=True)),
            ],
            options={
                'db_table': 'vehicle',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='XpressbusBus',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('routeid', models.IntegerField(db_column='routeId')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
            options={
                'db_table': 'xpressbus_bus',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stoprouteinfo',
            fields=[
                ('stopid', models.IntegerField(db_column='stopId', primary_key=True, serialize=False)),
                ('routesid', models.CharField(blank=True, db_column='routesId', max_length=120, null=True)),
                ('searchname', models.CharField(blank=True, db_column='searchName', max_length=100, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'stopRouteInfo',
                'managed': True,
            },
        ),
    ]