# Lista de verificación de requerimientos

Formato: [ID] Requerimiento — Criterio de aceptación — Método de verificación — Prioridad — Estado — Evidencia

1. [F-001] Autenticación por número de empleado y contraseña
- Criterio: Login exitoso para credenciales válidas; mensajes claros para credenciales inválidas.
- Verificación: TC-LOGIN-01..03
- Prioridad: Alta
- Estado: Pendiente

2. [F-002] Roles: Administrador y Empleado
- Criterio: Admin puede registrar empleados; Empleado no.
- Verificación: TC-EMP-01..03
- Prioridad: Alta
- Estado: Pendiente

3. [F-003] Alta de empleados por Admin; impedir duplicados
- Criterio: No crear duplicados; mostrar error en intento duplicado.
- Verificación: TC-EMP-02
- Prioridad: Alta
- Estado: Pendiente

4. [F-004] Alta de productos por Empleado; impedir duplicados
- Criterio: SKU único; duplicado genera error.
- Verificación: TC-PROD-01..02
- Prioridad: Alta
- Estado: Pendiente

5. [F-005] Generación de reportes (inventarios, clientes, empleados)
- Criterio: Reportes descargables y conformes a formato corporativo.
- Verificación: TC-REPORT-01..02
- Prioridad: Alta
- Estado: Pendiente

6. [NF-001] Información conforme a formatos corporativos
- Criterio: UI compliant con guía de estilo
- Verificación: TC-UI-01
- Prioridad: Alta
- Estado: Pendiente

7. [NF-002] Información encriptada
- Criterio: Contraseñas hashed; TLS en tránsito; cifrado en reposo si aplica.
- Verificación: Inspección de configuración TLS y DB
- Prioridad: Alta
- Estado: Pendiente

8. [NF-003] Respaldo automático cada 7 días
- Criterio: Backup generado cada 7 días con verificación
- Verificación: TC-BACKUP-01..02
- Prioridad: Alta
- Estado: Pendiente

9. [NF-004] Tiempo de respuesta aceptable
- Criterio: CRUD <300ms promedio; reportes <5s
- Verificación: Pruebas de rendimiento (TC-LOAD-01)
- Prioridad: Media-Alta
- Estado: Pendiente

10. [SEC-001] Protección contra inyección y XSS
- Criterio: Entradas saneadas y uso de prepared statements/ORM
- Verificación: Pruebas de seguridad
- Prioridad: Alta
- Estado: Pendiente

11. [OPS-001] Logs y auditoría
- Criterio: Registros de acceso y eventos críticos
- Verificación: Revisión de logs
- Prioridad: Media
- Estado: Pendiente

12. [DEPLOY-001] Multiplataforma (acceso web desde cualquier dispositivo)
- Criterio: UI responsiva y compatible con navegadores modernos
- Verificación: Pruebas en dispositivos móviles y desktop
- Prioridad: Media
- Estado: Pendiente

Notas:
- Para requerimientos ambiguos (por ejemplo: "información encriptada"), se asume aplicación a tránsito y reposo; confirmar con el cliente si se requieren medidas adicionales.
- Añadir campo de evidencia para cada ítem: capturas, logs, resultados de tests.

