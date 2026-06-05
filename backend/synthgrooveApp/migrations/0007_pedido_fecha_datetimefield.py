from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synthgrooveApp', '0006_evento_precio_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
