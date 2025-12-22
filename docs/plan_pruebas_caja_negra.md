# Plan de pruebas de caja negra

## Alcance
Pruebas funcionales y no funcionales desde la interfaz: autenticación, gestión de empleados y productos, generación de reportes, backups, seguridad observable y usabilidad. No se inspecciona código fuente.

## Formato de un caso de prueba
- ID | Título | Tipo | Precondición | Pasos | Datos de prueba | Resultado esperado | Prioridad

## Casos representativos

### A. Autenticación
- TC-LOGIN-01 | Login válido | Funcional | Usuario registrado | 1) Abrir login 2) Ingresar número empleado y contraseña 3) Enviar | emp:1001 / pass:P@ss123 | Acceso exitoso, redirige al dashboard según rol | Alta
- TC-LOGIN-02 | Usuario inexistente | Funcional | — | Intentar login con número no registrado | emp:9999 | Mensaje: "Usuario no existe" | Alta
- TC-LOGIN-03 | Contraseña incorrecta | Funcional | Usuario existente | Intentar login con pass incorrecta | emp:1001 / pass:wrong | Mensaje: "Contraseña incorrecta" | Alta
- TC-LOGIN-04 | Inyección SQL en usuario | Seguridad | — | Ingresar payload ' OR '1'='1 en número de empleado | emp: ' OR '1'='1 | Rechazo de entrada, no autenticación | Alta
- TC-LOGIN-05 | Expiración de sesión | Seguridad/Funcional | Login válido | 1) Loguear 2) Esperar expiración 3) Acceder a recurso protegido | — | Redirección a login | Media

### B. Gestión de empleados (Admin)
- TC-EMP-01 | Alta empleado válido | Funcional | Login como Admin | Crear empleado con número único | num:2002 | Empleado creado y registrado en BD | Alta
- TC-EMP-02 | Alta empleado duplicado | Funcional | Empleado ya existe | Intentar alta con número duplicado | num:2002 | Error: "Empleado ya existe" | Alta
- TC-EMP-03 | Alta por empleado sin permiso | Seguridad | Login como Empleado | Intentar acceder a alta de empleados | — | Acceso denegado (403) | Alta

### C. Gestión de productos (Empleado)
- TC-PROD-01 | Alta producto válido | Funcional | Login como Empleado | Crear producto con SKU único | sku:PROD-001 | Producto agregado y listado actualizado | Alta
- TC-PROD-02 | Alta producto duplicado | Funcional | SKU ya existe | Intentar crear con SKU duplicado | sku:PROD-001 | Error: "Producto ya existe" | Alta

### D. Reportes
- TC-REPORT-01 | Generar reporte inventario | Funcional | Datos en inventario | Seleccionar filtros y generar | — | Reporte descargable, formato corporativo | Alta
- TC-REPORT-02 | Reporte con muchos registros | Rendimiento | >10k registros | Generar reporte | — | Generación aceptable (<15s) o proceso por lotes | Media

### E. UI y formatos corporativos
- TC-UI-01 | Verificación visual de estilo | Manual | Cualquier página | Revisar header/footer, colores, tipografía | — | Cumple guía de estilo | Alta

### F. Seguridad observable
- TC-SEC-01 | HTTPS forzado | Seguridad | Herramienta de interceptación | Acceder vía HTTP | — | Redirección a HTTPS; credenciales no en texto claro | Alta
- TC-SEC-02 | Hash de contraseñas en BD | Seguridad | Acceso restringido a BD | Revisar campo de contraseña | — | Contraseñas hashed, no en texto plano | Alta

### G. Backups
- TC-BACKUP-01 | Backup programado | Procedimiento | DB con datos | Ejecutar backup (cron) | — | Archivo generado con timestamp y checksum | Alta
- TC-BACKUP-02 | Restauración de backup | Procedimiento | Backup válido | Restaurar en entorno de pruebas | — | Datos restaurados y consistentes | Alta

### H. Rendimiento / Carga
- TC-LOAD-01 | Carga concurrente de logins | Rendimiento | Herramienta (JMeter) | Ejecutar 100 logins concurrentes | — | Sin errores 5xx, latencia aceptable | Media-Alta

### I. Mensajería de errores
- TC-ERR-01 | Mensajes claros para duplicados | Usabilidad | Intento de alta duplicada | — | Mensaje claro y accionable | Alta

## Registro de resultados
- Para cada caso se registrará: Pass/Fail, evidencias (screenshots, logs), tiempo, tester, fecha.

