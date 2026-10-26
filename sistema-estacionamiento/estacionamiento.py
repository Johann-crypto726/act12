from datetime import datetime
class Estacionamiento:
    def __init__(self, capacidad_total):
        self.capacidad_total = capacidad_total
        self.vehiculos_registrados = {} 
        
    # MÓDULO 3: Disponibilidad de lugares en tiempo real
    def consultar_disponibilidad(self):
        ocupados = len(self.vehiculos_registrados)
        disponibles = self.capacidad_total - ocupados
        print(f"\n--- ESTADO DEL ESTACIONAMIENTO ---")
        print(f"Lugares totales: {self.capacidad_total}")
        print(f"Lugares ocupados: {ocupados}")
        print(f"Lugares disponibles: {disponibles}")
        return disponibles

    # MÓDULO 1: Registro de ingreso de vehículo (placa, hora, tipo)
    def registrar_ingreso(self, placa, tipo):
        if len(self.vehiculos_registrados) >= self.capacidad_total:
            print("❌ Error: Estacionamiento lleno. No hay lugares disponibles.")
            return False
        
        if placa in self.vehiculos_registrados:
            print(f"⚠️ El vehículo con placa {placa} ya se encuentra registrado.")
            return False
            
        hora_ingreso = datetime.now()
        self.vehiculos_registrados[placa] = {
            "tipo": tipo,
            "hora_ingreso": hora_ingreso
        }
        print(f"✅ Vehículo {placa} ({tipo}) registrado exitosamente a las {hora_ingreso.strftime('%H:%M:%S')}.")
        return True

    # MÓDULO 2: Cálculo de tarifa por hora y cobro
    def registrar_salida(self, placa, tarifa_por_hora):
        if placa not in self.vehiculos_registrados:
            print(f"❌ Error: No se encuentra ningún vehículo con la placa {placa}.")
            return None

        vehiculo = self.vehiculos_registrados[placa]
        hora_salida = datetime.now()
        hora_ingreso = vehiculo["hora_ingreso"]

        diferencia = hora_salida - hora_ingreso
        horas_transcurridas = diferencia.total_seconds() / 3600
        horas_cobro = max(1, round(horas_transcurridas, 2))
        total_a_pagar = horas_cobro * tarifa_por_hora

        del self.vehiculos_registrados[placa]

        print(f"\n--- TICKET DE SALIDA ---")
        print(f"Placa: {placa}")
        print(f"Tipo: {vehiculo['tipo']}")
        print(f"Total a pagar: ${total_a_pagar:.2f}")
        print(f"✅ Vehículo retirado. Lugar liberado.")
        return total_a_pagar

if __name__ == "__main__":
    parqueo = Estacionamiento(capacidad_total=5)
    tarifa = 10.0

    while True:
        print("\n=== MENÚ ESTACIONAMIENTO ===")
        print("1. Registrar ingreso de vehículo")
        print("2. Registrar salida y calcular cobro")
        print("3. Consultar disponibilidad")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            placa = input("Ingrese la placa del vehículo: ").strip().upper()
            tipo = input("Ingrese el tipo de vehículo (Auto, Moto, etc.): ").strip()
            parqueo.registrar_ingreso(placa, tipo)
        elif opcion == "2":
            placa = input("Ingrese la placa del vehículo a retirar: ").strip().upper()
            parqueo.registrar_salida(placa, tarifa)
        elif opcion == "3":
            parqueo.consultar_disponibilidad()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
