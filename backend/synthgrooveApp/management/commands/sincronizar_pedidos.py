from django.core.management.base import BaseCommand
from synthgrooveApp.models import Pago, Pedido
from decimal import Decimal


class Command(BaseCommand):
    help = 'Sincroniza los pagos confirmados con la tabla de Pedidos'

    def handle(self, *args, **options):
        pagos = Pago.objects.filter(
            pagado=True,
            producto__isnull=False,
            usuario__isnull=False
        )
        
        creados = 0
        existentes = 0
        errores = 0
        
        for pago in pagos:
            pedido_existe = Pedido.objects.filter(
                usuario=pago.usuario,
                producto=pago.producto,
                cantidad=pago.cantidad,
                precio_unitario=pago.monto / pago.cantidad if pago.cantidad > 0 else pago.monto,
                fecha=pago.fecha.date() if pago.fecha else None
            ).exists()
            
            if pedido_existe:
                existentes += 1
                self.stdout.write(
                    self.style.WARNING(
                        f'Pedido ya existe: {pago.usuario.usuario} - {pago.producto.nombre}'
                    )
                )
                continue
            
            try:
                precio_unitario = Decimal(pago.monto) / Decimal(pago.cantidad) if pago.cantidad > 0 else pago.monto
                
                pedido = Pedido.objects.create(
                    usuario=pago.usuario,
                    producto=pago.producto,
                    cantidad=pago.cantidad,
                    precio_unitario=precio_unitario
                )
                creados += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f'✓ Pedido creado: {pago.usuario.usuario} - {pago.producto.nombre} ({pago.cantidad}x)'
                    )
                )
            except Exception as e:
                errores += 1
                self.stdout.write(
                    self.style.ERROR(
                        f'✗ Error al crear Pedido para {pago.usuario.usuario}: {str(e)}'
                    )
                )
        
        self.stdout.write(self.style.SUCCESS(f'\n--- Resumen ---'))
        self.stdout.write(self.style.SUCCESS(f'Pedidos creados: {creados}'))
        self.stdout.write(self.style.WARNING(f'Pedidos existentes: {existentes}'))
        self.stdout.write(self.style.ERROR(f'Errores: {errores}'))
