 # Atributos de calidad

## Introducción
Un atributo de calidad es una propiedad medible del sistema que indica qué tan bien satisface las necesidades de las partes interesadas. En este documento se describen los atributos de calidad relevantes para el sistema de control de inventario y clientes de "Cajas y Derivados S.A. de C.V.", cómo se miden y qué actividades/controles se proponen para garantizar cada atributo.

## Lista descriptiva de atributos de calidad (con métricas y verificación)

1) Disponibilidad
	- Descripción: El sistema debe estar disponible para los usuarios durante las horas operativas y con un objetivo de tiempo de actividad (SLA).
	- Métrica: % uptime semanal (por ejemplo 99.5%).
	- Cómo garantizarlo: despliegue redundante, monitoreo y alertas, backups periódicos.
	- Verificación: monitoreo (Prometheus/CloudWatch), registros de uptime y pruebas de restauración de backup.

2) Rendimiento (Performance)
	- Descripción: Respuesta rápida en operaciones CRUD y generación de reportes.
	- Métrica: Latencia media para operaciones CRUD < 300 ms; generación de reportes < 5 s para conjuntos pequeños/medios.
	- Cómo garantizarlo: índices en PostgreSQL, consultas optimizadas, paginación, caché en la app si es necesario.
	- Verificación: pruebas de carga y benchmarks (JMeter, locust) con percentiles (p95, p99).

3) Seguridad
	- Descripción: Confidencialidad, integridad y disponibilidad de la información; protección contra ataques comunes.
	- Métrica: nº de vulnerabilidades críticas en auditorías; cumplimiento de hashing y TLS.
	- Cómo garantizarlo: HTTPS/TLS, hashing fuerte (bcrypt/argon2) para contraseñas, prepared statements/ORM para evitar inyección SQL, validación de entradas, control de acceso por roles.
	- Verificación: pruebas de penetración básicas, revisión de configuración TLS y revisión de almacenamiento de contraseñas en la BD.

4) Integridad de datos
	- Descripción: Evitar duplicados y mantener relaciones consistentes entre tablas.
	- Métrica: nº de conflictos/duplicados detectados en logs; integridad referencial verificada.
	- Cómo garantizarlo: constraints (UNIQUE, FK), transacciones ACID para operaciones compuestas, validaciones en la capa de aplicación.
	- Verificación: pruebas funcionales y pruebas de concurrencia que intenten crear duplicados.

5) Usabilidad
	- Descripción: Interfaz clara, adaptada al formato corporativo y fácil de entender para Admin y Empleado.
	- Métrica: tiempo medio para completar tareas comunes (p. ej., dar de alta un producto) y tasas de error de usuario.
	- Cómo garantizarlo: diseño responsivo, guía de estilos corporativos, mensajes de error claros y flujos simples.
	- Verificación: pruebas de usabilidad con usuarios y checklist de cumplimiento de estilo.

6) Mantenibilidad
	- Descripción: Código organizado que facilita cambios y correcciones.
	- Métrica: tiempo medio para resolver un bug simple; cobertura mínima de tests.
	- Cómo garantizarlo: patrón MVC, código modular, documentación y tests automatizados.
	- Verificación: análisis de cobertura, revisión de commits y calidad de código.

7) Escalabilidad
	- Descripción: Capacidad de soportar crecimiento de usuarios y volumen de datos.
	- Métrica: incremento viable de usuarios simultáneos sin degradación significativa.
	- Cómo garantizarlo: separación de capas, uso de base de datos escalable (PostgreSQL), despliegue en contenedores o infraestructura escalable.
	- Verificación: pruebas de escalado y stress tests.

8) Recuperabilidad (Backup/Restore)
	- Descripción: Backup automático cada 7 días y capacidad de restauración en entorno de prueba.
	- Métrica: tiempo de recuperación objetivo (RTO) y punto de recuperación (RPO).
	- Cómo garantizarlo: scripts de backup (pg_dump), verificación de checksums, pruebas periódicas de restore.
	- Verificación: reportes de backup y pruebas de restauración.

9) Portabilidad / Multiplataforma
	- Descripción: La aplicación debe ser accesible desde cualquier dispositivo con acceso web y desplegable en distintos entornos.
	- Métrica: compatibilidad con navegadores modernos y soporte móvil.
	- Cómo garantizarlo: HTML5/CSS responsivo, contenedores Docker para despliegue.
	- Verificación: pruebas en distintos navegadores y dispositivos, pruebas de despliegue en entornos distintos.

10) Conformidad con formatos corporativos
	- Descripción: Todas las vistas deben respetar colores, tipografías y formatos de datos de la organización.
	- Cómo garantizarlo: hoja de estilos central y templates compartidos.
	- Verificación: checklist visual y revisión por el cliente.

## Riesgos y consideraciones
- Condiciones de carrera en altas simultáneas -> usar transacciones y constraints.
- Exposición de datos sensibles -> asegurar TLS y no almacenar secretos en el código.

## Resumen (matriz rápida)
- Seguridad: hashing, TLS, prepared statements -> Verificación: auditoría, pruebas de penetración.
- Rendimiento: índices, paginación, caché -> Verificación: pruebas de carga (p95,p99).
- Disponibilidad/Backups: pg_dump semanal, restore-> Verificación: pruebas de restore.


