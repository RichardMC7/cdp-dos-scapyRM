LINK DEL VIDEO DE LOS ATAQUES:
https://youtu.be/v5858w0WOPo

Ataque de Denegación de Servicio (DoS) mediante CDP con Scapy
Objetivo del Script

El objetivo de este laboratorio es demostrar cómo el protocolo Cisco Discovery Protocol (CDP) puede ser explotado para generar una condición de denegación de servicio (DoS) en dispositivos de red Cisco.

El script desarrollado en Python utilizando Scapy envía múltiples paquetes CDP falsificados hacia un switch o router Cisco con el propósito de saturar su plano de control, provocando degradación del rendimiento o interrupción parcial del servicio.

Este ejercicio permite comprender los riesgos asociados a protocolos de descubrimiento que se ejecutan en la Capa 2 del modelo OSI cuando no están correctamente protegidos.

Topología de Red

Ejemplo (modificar según tu laboratorio):

Dispositivo	Rol	Dirección IP	Interfaz
Kali Linux	Atacante	192.168.10.10	eth0
Switch Cisco (IOL)	Víctima	N/A (Capa 2)	e0/0
Host Linux	Equipo de prueba	192.168.10.20	eth0

Red: 192.168.10.0/24
VLAN: VLAN 10 (opcional si fue configurada).
Dominio de broadcast: Todos los dispositivos deben estar en el mismo segmento.

Nota técnica: CDP opera en Capa 2 y no requiere direccionamiento IP para funcionar.

Capturas de Pantalla

Insertar evidencia en el siguiente orden:

Topología en PNETLab


Verificación de CDP habilitado en el switch

Ejemplo de comando:

show cdp neighbors



Ejecución del script DoS
sudo python3 cdp_dos.py



Evidencia de degradación del dispositivo

Puede incluir:

Alto uso de CPU

Lentitud en la CLI

Pérdida de paquetes

Retrasos en respuestas

Ejemplo:

show processes cpu


Parámetros Usados

Ejemplo de configuración dentro del script:

interface = "eth0"
packet_count = 1000
interval = 0.01

Funcionalidad del Script

Construcción de paquetes CDP falsificados.

Envío masivo de tramas Ethernet al multicast de CDP.

Generación de carga excesiva en el dispositivo objetivo.

Requisitos para Utilizar la Herramienta
Software

Kali Linux o distribución Linux equivalente

Python 3

Scapy

Permisos de superusuario

PNETLab o entorno virtualizado

Imagen Cisco IOL o dispositivo compatible con CDP

Instalación de Scapy
pip install scapy

Ejecución con privilegios
sudo python3 cdp_dos.py

Medidas de Mitigación

Para reducir la exposición a este tipo de ataques se recomienda:

Deshabilitar CDP en interfaces donde no sea necesario:

no cdp enable


o globalmente:

no cdp run


Implementar Port Security: limita qué dispositivos pueden conectarse al switch.

Segmentación de red: reduce el alcance de ataques de Capa 2.

Control Plane Policing (CoPP): protege el plano de control contra tráfico excesivo.

Monitoreo de red: permite detectar comportamientos anómalos.

Conclusión Técnica

El laboratorio demuestra que los protocolos de descubrimiento pueden representar un riesgo significativo si permanecen habilitados sin controles de seguridad. Un atacante dentro del mismo segmento puede generar tráfico malicioso capaz de afectar la estabilidad del dispositivo.

La práctica fue realizada en un entorno controlado con fines educativos.
