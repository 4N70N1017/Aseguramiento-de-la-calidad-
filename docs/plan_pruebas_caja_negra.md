# Plan de pruebas de caja negra

## Alcance
Pruebas funcionales y no funcionales desde la interfaz: autenticación, gestión de empleados y productos, generación de reportes, backups, seguridad observable y usabilidad. No se inspecciona código fuente.

## Formato de un caso de prueba
- ID | Título | Tipo | Precondición | Pasos | Datos de prueba | Resultado esperado | Prioridad

## Casos representativos (detallados)

### A. Autenticación

- TC-LOGIN-01 | Login válido | Funcional
	- Precondición: Usuario admin o empleado registrado.
	- Pasos:
		1) Abrir la página `/login`.
		2) Introducir `emp_number=1001` y `password=P@ss123`.
		3) Pulsar `Entrar`.
	- Resultado esperado: Inicio de sesión exitoso, redirección al dashboard adecuado y cookie de sesión establecida.
	- Prioridad: Alta

- TC-LOGIN-02 | Usuario inexistente | Funcional
	- Precondición: Ninguno
	- Pasos: Intentar loguear con `emp_number=9999`.
	- Resultado esperado: Mensaje "Usuario no existe"; no crear sesión.
	- Prioridad: Alta

- TC-LOGIN-03 | Contraseña incorrecta | Funcional
	- Precondición: Usuario registrado.
	- Pasos: Ingresar `emp_number=1001` y `password=wrong`.
	- Resultado esperado: Mensaje "Contraseña incorrecta"; no crear sesión.
	- Prioridad: Alta

- TC-LOGIN-04 | Inyección SQL en campos | Seguridad
	- Precondición: Ninguno.
	- Pasos: Introducir payloads de inyección en campos (ej.: `"' OR '1'='1"`).
	- Resultado esperado: Entrada saneada o rechazada; no autenticación no autorizada; sin divulgación de errores del servidor.
	- Prioridad: Alta


### B. Gestión de empleados (Admin)

- TC-EMP-01 | Alta empleado válido
	- Precondición: Login como Admin.
	- Pasos: Navegar a alta, completar `emp_number=2002`, `name=Juan`, `password=P@ss01`, `role=employee`, enviar.
	- Resultado esperado: Empleado creado, registro en BD, mensaje de éxito.
	- Prioridad: Alta

- TC-EMP-02 | Alta empleado duplicado
	- Precondición: Empleado con `emp_number=2002` ya existe.
	- Pasos: Repetir alta con mismo número.
	- Resultado esperado: Mensaje claro "Empleado ya existe" y no duplicación en BD.
	- Prioridad: Alta

- TC-EMP-03 | Restricción de permisos
	- Precondición: Login como Empleado.
	- Pasos: Intentar acceder a `/admin/employees/create`.
	- Resultado esperado: Acceso denegado (403) o la opción no visible; registro en logs.
	- Prioridad: Alta


### C. Gestión de productos (Empleado)

- TC-PROD-01 | Alta producto válido
	- Precondición: Login como Empleado.
	- Pasos: Crear producto con `sku=PROD-001`, `name=Caja`, `quantity=10`.
	- Resultado esperado: Producto agregado; listado actualizado.
	- Prioridad: Alta

- TC-PROD-02 | Alta producto duplicado
	- Precondición: SKU ya existente.
	- Pasos: Intentar crear con mismo SKU.
	- Resultado esperado: Mensaje "Producto ya existe"; no duplicación.
	- Prioridad: Alta


### D. Reportes

- TC-REPORT-01 | Generar reporte inventario (pequeño)
	- Precondición: Datos en inventario (< 1000 registros).
	- Pasos: Generar reporte desde UI.
	- Resultado esperado: Archivo CSV descargable; contenido correcto; formato conforme a guía.
	- Prioridad: Alta

- TC-REPORT-02 | Generar reporte grande (rendimiento)
	- Precondición: > 10k registros en inventario.
	- Pasos: Generar reporte.
	- Resultado esperado: Proceso completado o generación por lotes; tiempo aceptable (definir umbral, ej. < 15 s) y sin errores 5xx.
	- Prioridad: Media


### E. Backups y restauración

- TC-BACKUP-01 | Ejecución del backup programado
	- Precondición: DB con datos.
	- Pasos: Ejecutar `backup.sh` o simular cron.
	- Resultado esperado: Archivo SQL creado con timestamp; checksum correcto.
	- Prioridad: Alta

- TC-BACKUP-02 | Restauración desde backup
	- Precondición: Backup existente.
	- Pasos: Restaurar en entorno de prueba.
	- Resultado esperado: Datos restaurados y consistentes; validaciones básicas OK.
	- Prioridad: Alta


### F. Seguridad observable (caja negra)

- TC-SEC-01 | Forzar HTTP -> HTTPS
	- Precondición: Servicio corriendo.
	- Pasos: Acceder por `http://`.
	- Resultado esperado: Redirección a `https://` (si está configurado en entorno de despliegue); credenciales no visibles.
	- Prioridad: Alta

- TC-SEC-02 | Almacenamiento de contraseñas
	- Precondición: Acceso restringido a BD.
	- Pasos: Revisar campo `password_hash` en BD.
	- Resultado esperado: Hashes, no texto claro; algoritmo fuerte.
	- Prioridad: Alta


### G. Usabilidad y formatos corporativos

- TC-UI-01 | Verificación visual
	- Precondición: Acceso a interfaz.
	- Pasos: Revisar header/footer, colores, tipografías, formatos de fecha y moneda.
	- Resultado esperado: Cumple guía de estilo.
	- Prioridad: Alta


### H. Rendimiento / Carga (externo)

- TC-LOAD-01 | Carga concurrente (ejemplo)
	- Precondición: Herramienta de pruebas (JMeter/locust)
	- Pasos: Ejecutar 100 logins concurrentes y medir latencias.
	- Resultado esperado: Latencias dentro de SLA; sin errores 5xx.
	- Prioridad: Media-Alta


## Registro y ejecución de tests
- Para cada caso se registrará: ID, resultado (Pass/Fail), evidencias (screenshots, logs), tiempo de ejecución, tester y fecha.
- Se recomienda usar una planilla CSV/exportable con columnas: ID, Caso, Precondición, Pasos, Datos, Resultado esperado, Resultado real, Evidencias, Tester, Fecha, Observaciones.

## Priorización
- Alta: Autenticación, control de roles, prevención de duplicados, backups, seguridad básica, UI corporativa.
- Media: Reportes de gran tamaño, pruebas de carga extensivas, usabilidad detallada.


