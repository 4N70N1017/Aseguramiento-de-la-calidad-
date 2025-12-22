## Atributos de calidad

### Contrato corto
- Inputs: número de empleado, contraseña; datos de empleados y productos; parámetros de generación de reportes.
- Outputs: respuestas de autenticación, vistas HTML conforme a formato corporativo, reportes descargables, mensajes de error claros.
- Criterios de éxito: autenticación segura y roles correctamente aplicados; operaciones CRUD funcionales; reportes correctos; backups cada 7 días; tiempos de respuesta aceptables.

### Edge cases relevantes
- Altas simultáneas que puedan generar duplicados (condiciones de carrera).
- Conexiones intermitentes a PostgreSQL.
- Campos vacíos o datos con formatos inválidos.
- Restauración desde backup corrupto.

---

### 1. Rendimiento
- Objetivo: respuestas CRUD simples < 300 ms; generación de reportes < 5 s (datasets pequeños/medios).
- Cómo lograrlo: consultas SQL optimizadas, índices, paginación, caché cuando proceda.
- Verificación: pruebas de carga y mediciones (benchmarks).

### 2. Usabilidad
- Objetivo: interfaz clara, navegación intuitiva y cumplimiento de formatos corporativos.
- Cómo: plantillas HTML/CSS responsivas, guía de estilo, mensajes claros.
- Verificación: pruebas de usabilidad y checklist contra guía de estilo.

### 3. Seguridad
- Objetivo: confidencialidad e integridad de datos, protección contra ataques comunes.
- Cómo: HTTPS/TLS, hashing seguro de contraseñas (bcrypt/argon2), uso de prepared statements/ORM, validación y saneamiento de entradas, gestión de sesiones segura, control de roles.
- Verificación: auditoría de seguridad y pruebas básicas de penetración.

### 4. Integridad y consistencia de datos
- Objetivo: evitar duplicados y mantener integridad referencial.
- Cómo: constraints (UNIQUE, FK), transacciones ACID en operaciones compuestas.
- Verificación: pruebas funcionales y de concurrencia.

### 5. Disponibilidad y fiabilidad
- Objetivo: servicio accesible en horarios operativos y tolerancia a fallos razonable.
- Cómo: backups automáticos, monitoreo y manejo de errores con reintentos limitados.
- Verificación: pruebas de restauración y monitoreo de uptime.

### 6. Mantenibilidad
- Objetivo: código y arquitectura que faciliten cambios.
- Cómo: patrón MVC, documentación, tests automatizados y buenas prácticas de código.
- Verificación: cobertura de pruebas y revisiones de código.

### 7. Escalabilidad y portabilidad
- Objetivo: soportar crecimiento y ser desplegable en variados entornos.
- Cómo: separación de capas, uso de tecnologías portables (Python, PostgreSQL), contenedores opcionales.
- Verificación: pruebas de escalado y despliegue en entorno distinto.

### 8. Recuperación / Backup
- Objetivo: backups cada 7 días y restauración fiable.
- Cómo: scripts/cron para pg_dump, verificación de integridad y retención.
- Verificación: restores periódicos a entorno de prueba.

### 9. Formato corporativo
- Objetivo: mostrar información conforme a la guía de estilos de la organización.
- Cómo: hoja de estilos CSS y templates compartidos.
- Verificación: revisión visual y checklist de cumplimiento.

---

### Calidad: métricas y verificación resumida
- Pruebas de rendimiento: tiempos medios y percentiles para respuestas.
- Pruebas de seguridad: lista de vulnerabilidades básicas rechazadas.
- Pruebas funcionales: cobertura de casos críticos (autenticación, altas, duplicados, reportes, backups).

