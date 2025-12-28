 # Lista de verificación de requerimientos

Formato: [ID] Requerimiento — Criterio de aceptación — Método de verificación — Prioridad — Estado — Evidencia

## Requerimientos técnicos

1. [T-001] Lenguajes: HTML5, CSS, Python
	- Criterio: Frontend construido en HTML5/CSS; lógica en Python (Flask).
	- Verificación: Revisión de archivos fuente (archivos .html/.css y .py).
	- Prioridad: Alta
	- Estado: Completo
	- Evidencia: Repositorio fuente

2. [T-002] Base de datos: PostgreSQL
	- Criterio: Capacidad de conectar a PostgreSQL y usar SQL estándar.
	- Verificación: Pruebas de conexión a BD, `docker-compose` con Postgres.
	- Prioridad: Alta
	- Estado: Completo

3. [T-003] Entorno multiplataforma (web)
	- Criterio: Accesible desde navegadores modernos y dispositivos móviles.
	- Verificación: Pruebas en Chrome, Firefox y Mobile viewport.
	- Prioridad: Media
	- State: Completo

4. [T-004] Backups automáticos
	- Criterio: Script de backup y política semanal.
	- Verificación: `backup.sh` y pruebas de restore.
	- Prioridad: Alta
	- State: Completo


## Requerimientos funcionales

1. [F-001] Autenticación por número de empleado y contraseña
	- Criterio: Login exitoso para credenciales válidas; mensajes claros para credenciales inválidas.
	- Verificación: TC-LOGIN-01..03
	- Prioridad: Alta
	- Estado: Completo

2. [F-002] Roles: Administrador y Empleado
	- Criterio: Admin puede registrar empleados; Empleado no.
	- Verificación: TC-EMP-01..03
	- Prioridad: Alta
	- Estado: Completo

3. [F-003] Alta de empleados por Admin; impedir duplicados
	- Criterio: No crear duplicados; mostrar error en intento duplicado.
	- Verificación: TC-EMP-02
	- Prioridad: Alta
	- Estado: Completo

4. [F-004] Alta de productos por Empleado; impedir duplicados
	- Criterio: SKU único; duplicado genera error.
	- Verificación: TC-PROD-01..02
	- Prioridad: Alta
	- Estado: Completo

5. [F-005] Generación de reportes (inventarios, clientes, empleados)
	- Criterio: Reportes descargables y conformes a formato corporativo.
	- Verificación: TC-REPORT-01..02
	- Prioridad: Alta
	- Estado: Completo

6. [F-006] Mensajes y manejo de errores
	- Criterio: Mensajes claros y sin filtrado de información sensible.
	- Verificación: TC-ERR-01 y revisión manual.
	- Prioridad: Alta
	- Estado: Completo


## Requerimientos no funcionales (NF)

1. [NF-001] Información conforme a formatos corporativos
	- Criterio: UI compliant con guía de estilo (colores, logos, formatos de datos).
	- Verificación: TC-UI-01
	- Prioridad: Alta
	- Estado: Completo

2. [NF-002] Encriptación y protección de datos
	- Criterio: Contraseñas hashed; TLS en tránsito; cifrado en reposo opcional según alcance.
	- Verificación: Revisión de hashes en BD y configuración de TLS.
	- Prioridad: Alta
	- Estado: Completo

3. [NF-003] Respaldo cada 7 días
	- Criterio: Backups automáticos y verificados.
	- Verificación: TC-BACKUP-01..02
	- Prioridad: Alta
	- State: Completo

4. [NF-004] Rendimiento
	- Criterio: CRUD <300ms promedio; reportes pequeños <5s.
	- Verificación: Pruebas de rendimiento (TC-LOAD-01).
	- Prioridad: Media-Alta
	- Estado: Completo

5. [SEC-001] Protección contra inyección y XSS
	- Criterio: Entradas saneadas y uso de prepared statements/ORM.
	- Verificación: Pruebas de seguridad.
	- Prioridad: Alta
	- Estado: Completo


## Checklist tipo inventario (resumen rápido)

- Requerimientos Técnicos:
  - HTML5/CSS (✔)
  - Python/Flask (✔)
  - PostgreSQL (✔)
  - Docker (opcional para despliegue) (✔)

- Requerimientos Funcionales:
  - Autenticación por número de empleado (✔)
  - Roles Admin/Empleado (✔)
  - Alta de empleados (Admin) con control de duplicados (✔)
  - Alta de productos (Empleado) con control de duplicados (✔)
  - Generación de reportes (✔)

## Observaciones
- Para cualquier ítem marcado como "Completo" se requiere evidencia (capturas, logs o registros de pruebas). Añadir evidencia en la columna "Evidencia" en el registro de verificación.
- Si algún requisito debe ampliarse (por ejemplo cifrado en reposo), anotar el detalle en la sección de observaciones y actualizar el alcance.

