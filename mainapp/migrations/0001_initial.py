# Generated by Django 3.2.8 on 2021-11-03 08:53

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter', mainapp.models.ParameterField(max_length=128, unique=True)),
                ('reference_value_min', models.CharField(blank=True, default=0, max_length=8, verbose_name='reference value')),
                ('reference_value_max', models.CharField(blank=True, max_length=8, verbose_name='reference value')),
                ('unit_of_measure', models.CharField(blank=True, max_length=32, verbose_name='unit of measure')),
            ],
            options={
                'verbose_name': 'analysis',
                'verbose_name_plural': 'analyzes',
            },
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.TextField(max_length=256, unique=True)),
                ('analyzes', models.ManyToManyField(related_name='analyzes_disease', to='mainapp.Analysis')),
            ],
            options={
                'verbose_name': 'disease',
                'verbose_name_plural': 'diseases',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64, verbose_name='first name')),
                ('last_name', models.CharField(max_length=64, verbose_name='last name')),
                ('country', models.CharField(choices=[(None, 'Select a country'), ('AD', 'Andorra'), ('AE', 'United Arab Emirates'), ('AF', 'Afghanistan'), ('AG', 'Antigua & Barbuda'), ('AI', 'Anguilla'), ('AL', 'Albania'), ('AM', 'Armenia'), ('AO', 'Angola'), ('AQ', 'Antarctica'), ('AR', 'Argentina'), ('AS', 'Samoa (American)'), ('AT', 'Austria'), ('AU', 'Australia'), ('AW', 'Aruba'), ('AX', 'Åland Islands'), ('AZ', 'Azerbaijan'), ('BA', 'Bosnia & Herzegovina'), ('BB', 'Barbados'), ('BD', 'Bangladesh'), ('BE', 'Belgium'), ('BF', 'Burkina Faso'), ('BG', 'Bulgaria'), ('BH', 'Bahrain'), ('BI', 'Burundi'), ('BJ', 'Benin'), ('BL', 'St Barthelemy'), ('BM', 'Bermuda'), ('BN', 'Brunei'), ('BO', 'Bolivia'), ('BQ', 'Caribbean NL'), ('BR', 'Brazil'), ('BS', 'Bahamas'), ('BT', 'Bhutan'), ('BV', 'Bouvet Island'), ('BW', 'Botswana'), ('BY', 'Belarus'), ('BZ', 'Belize'), ('CA', 'Canada'), ('CC', 'Cocos (Keeling) Islands'), ('CD', 'Congo (Dem. Rep.)'), ('CF', 'Central African Rep.'), ('CG', 'Congo (Rep.)'), ('CH', 'Switzerland'), ('CI', "Côte d'Ivoire"), ('CK', 'Cook Islands'), ('CL', 'Chile'), ('CM', 'Cameroon'), ('CN', 'China'), ('CO', 'Colombia'), ('CR', 'Costa Rica'), ('CU', 'Cuba'), ('CV', 'Cape Verde'), ('CW', 'Curaçao'), ('CX', 'Christmas Island'), ('CY', 'Cyprus'), ('CZ', 'Czech Republic'), ('DE', 'Germany'), ('DJ', 'Djibouti'), ('DK', 'Denmark'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('DZ', 'Algeria'), ('EC', 'Ecuador'), ('EE', 'Estonia'), ('EG', 'Egypt'), ('EH', 'Western Sahara'), ('ER', 'Eritrea'), ('ES', 'Spain'), ('ET', 'Ethiopia'), ('FI', 'Finland'), ('FJ', 'Fiji'), ('FK', 'Falkland Islands'), ('FM', 'Micronesia'), ('FO', 'Faroe Islands'), ('FR', 'France'), ('GA', 'Gabon'), ('GB', 'Britain (UK)'), ('GD', 'Grenada'), ('GE', 'Georgia'), ('GF', 'French Guiana'), ('GG', 'Guernsey'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GL', 'Greenland'), ('GM', 'Gambia'), ('GN', 'Guinea'), ('GP', 'Guadeloupe'), ('GQ', 'Equatorial Guinea'), ('GR', 'Greece'), ('GS', 'South Georgia & the South Sandwich Islands'), ('GT', 'Guatemala'), ('GU', 'Guam'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HK', 'Hong Kong'), ('HM', 'Heard Island & McDonald Islands'), ('HN', 'Honduras'), ('HR', 'Croatia'), ('HT', 'Haiti'), ('HU', 'Hungary'), ('ID', 'Indonesia'), ('IE', 'Ireland'), ('IL', 'Israel'), ('IM', 'Isle of Man'), ('IN', 'India'), ('IO', 'British Indian Ocean Territory'), ('IQ', 'Iraq'), ('IR', 'Iran'), ('IS', 'Iceland'), ('IT', 'Italy'), ('JE', 'Jersey'), ('JM', 'Jamaica'), ('JO', 'Jordan'), ('JP', 'Japan'), ('KE', 'Kenya'), ('KG', 'Kyrgyzstan'), ('KH', 'Cambodia'), ('KI', 'Kiribati'), ('KM', 'Comoros'), ('KN', 'St Kitts & Nevis'), ('KP', 'Korea (North)'), ('KR', 'Korea (South)'), ('KW', 'Kuwait'), ('KY', 'Cayman Islands'), ('KZ', 'Kazakhstan'), ('LA', 'Laos'), ('LB', 'Lebanon'), ('LC', 'St Lucia'), ('LI', 'Liechtenstein'), ('LK', 'Sri Lanka'), ('LR', 'Liberia'), ('LS', 'Lesotho'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('LV', 'Latvia'), ('LY', 'Libya'), ('MA', 'Morocco'), ('MC', 'Monaco'), ('MD', 'Moldova'), ('ME', 'Montenegro'), ('MF', 'St Martin (French)'), ('MG', 'Madagascar'), ('MH', 'Marshall Islands'), ('MK', 'North Macedonia'), ('ML', 'Mali'), ('MM', 'Myanmar (Burma)'), ('MN', 'Mongolia'), ('MO', 'Macau'), ('MP', 'Northern Mariana Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MS', 'Montserrat'), ('MT', 'Malta'), ('MU', 'Mauritius'), ('MV', 'Maldives'), ('MW', 'Malawi'), ('MX', 'Mexico'), ('MY', 'Malaysia'), ('MZ', 'Mozambique'), ('NA', 'Namibia'), ('NC', 'New Caledonia'), ('NE', 'Niger'), ('NF', 'Norfolk Island'), ('NG', 'Nigeria'), ('NI', 'Nicaragua'), ('NL', 'Netherlands'), ('NO', 'Norway'), ('NP', 'Nepal'), ('NR', 'Nauru'), ('NU', 'Niue'), ('NZ', 'New Zealand'), ('OM', 'Oman'), ('PA', 'Panama'), ('PE', 'Peru'), ('PF', 'French Polynesia'), ('PG', 'Papua New Guinea'), ('PH', 'Philippines'), ('PK', 'Pakistan'), ('PL', 'Poland'), ('PM', 'St Pierre & Miquelon'), ('PN', 'Pitcairn'), ('PR', 'Puerto Rico'), ('PS', 'Palestine'), ('PT', 'Portugal'), ('PW', 'Palau'), ('PY', 'Paraguay'), ('QA', 'Qatar'), ('RE', 'Réunion'), ('RO', 'Romania'), ('RS', 'Serbia'), ('RU', 'Russia'), ('RW', 'Rwanda'), ('SA', 'Saudi Arabia'), ('SB', 'Solomon Islands'), ('SC', 'Seychelles'), ('SD', 'Sudan'), ('SE', 'Sweden'), ('SG', 'Singapore'), ('SH', 'St Helena'), ('SI', 'Slovenia'), ('SJ', 'Svalbard & Jan Mayen'), ('SK', 'Slovakia'), ('SL', 'Sierra Leone'), ('SM', 'San Marino'), ('SN', 'Senegal'), ('SO', 'Somalia'), ('SR', 'Suriname'), ('SS', 'South Sudan'), ('ST', 'Sao Tome & Principe'), ('SV', 'El Salvador'), ('SX', 'St Maarten (Dutch)'), ('SY', 'Syria'), ('SZ', 'Eswatini (Swaziland)'), ('TC', 'Turks & Caicos Is'), ('TD', 'Chad'), ('TF', 'French Southern & Antarctic Lands'), ('TG', 'Togo'), ('TH', 'Thailand'), ('TJ', 'Tajikistan'), ('TK', 'Tokelau'), ('TL', 'East Timor'), ('TM', 'Turkmenistan'), ('TN', 'Tunisia'), ('TO', 'Tonga'), ('TR', 'Turkey'), ('TT', 'Trinidad & Tobago'), ('TV', 'Tuvalu'), ('TW', 'Taiwan'), ('TZ', 'Tanzania'), ('UA', 'Ukraine'), ('UG', 'Uganda'), ('UM', 'US minor outlying islands'), ('US', 'United States'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VA', 'Vatican City'), ('VC', 'St Vincent'), ('VE', 'Venezuela'), ('VG', 'Virgin Islands (UK)'), ('VI', 'Virgin Islands (US)'), ('VN', 'Vietnam'), ('VU', 'Vanuatu'), ('WF', 'Wallis & Futuna'), ('WS', 'Samoa (western)'), ('YE', 'Yemen'), ('YT', 'Mayotte'), ('ZA', 'South Africa'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')], max_length=32)),
                ('language', models.CharField(choices=[(None, 'Select a language'), ('af', 'Afrikaans'), ('ar', 'Arabic'), ('ar-dz', 'Algerian Arabic'), ('ast', 'Asturian'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('br', 'Breton'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('dsb', 'Lower Sorbian'), ('el', 'Greek'), ('en', 'English'), ('en-au', 'Australian English'), ('en-gb', 'British English'), ('eo', 'Esperanto'), ('es', 'Spanish'), ('es-ar', 'Argentinian Spanish'), ('es-co', 'Colombian Spanish'), ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'), ('es-ve', 'Venezuelan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('ga', 'Irish'), ('gd', 'Scottish Gaelic'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hsb', 'Upper Sorbian'), ('hu', 'Hungarian'), ('hy', 'Armenian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('ig', 'Igbo'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('kab', 'Kabyle'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('ky', 'Kyrgyz'), ('lb', 'Luxembourgish'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'Marathi'), ('my', 'Burmese'), ('nb', 'Norwegian Bokmål'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('nn', 'Norwegian Nynorsk'), ('os', 'Ossetic'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('tg', 'Tajik'), ('th', 'Thai'), ('tk', 'Turkmen'), ('tr', 'Turkish'), ('tt', 'Tatar'), ('udm', 'Udmurt'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('vi', 'Vietnamese'), ('zh-hans', 'Simplified Chinese'), ('zh-hant', 'Traditional Chinese')], max_length=32)),
                ('age', models.PositiveSmallIntegerField(default=18)),
                ('is_active', models.BooleanField(default=True)),
                ('disease', models.ManyToManyField(related_name='disease_patient', to='mainapp.Disease')),
            ],
            options={
                'verbose_name': 'patient',
                'verbose_name_plural': 'patients',
            },
        ),
    ]
