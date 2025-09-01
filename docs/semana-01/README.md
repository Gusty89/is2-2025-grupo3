# Semana 01 – Setup y Análisis Inicial

## Objetivos de la Semana
- Configurar el entorno de desarrollo y el repositorio.
- Analizar el problema y definir los requerimientos iniciales.
- Establecer la estructura del proyecto backend y frontend.
- Crear las primeras entidades del dominio (`Producto` y `Deposito`).

---

## Entregables
- Configuración inicial del repositorio:
  - Carpetas: `backend/`, `docs/`, `test/`.
  - Entorno virtual (`venv/`) y archivo `requirements.txt`.
- Modelos iniciales del dominio:
  - `Producto` (`app/domain/models/producto.py`)
  - `Deposito` (`app/domain/models/deposito.py`)
- Diagramas de análisis y flujo de datos.

---

## Estructura de Carpetas
docs/semana-01/
├── diagramas/ # Diagramas UML, ER, flujo, etc.
│ ├── modelo_dominio.png
│ └── flujo_backend.drawio
├── especificaciones/ # Documentos de análisis y decisiones
│ ├── requerimientos.md
│ └── decisiones.md
├── reportes/ # Resultados de pruebas o ejemplos
│ └── prueba_inicial.txt
└── README.md # Este archivo

---

## Avances Realizados
1. **Repositorio y entorno**  
   - Creación de la estructura inicial de carpetas.
   - Configuración de entorno virtual y dependencias básicas.
2. **Modelo de dominio**  
   - Clase `Producto` en `app/domain/models/producto.py`.
   - Clase `Deposito` en `app/domain/models/deposito.py`.
3. **Primeros scripts de prueba**  
   - Scripts de inserción de datos en la base de datos (`seed_data.py`).
4. **Documentación inicial**  
   - Diagramas UML y notas de análisis en `diagramas/` y `especificaciones/`.

---

## Próximos Pasos
- Implementar CRUD de productos y depósitos (Semana 03).
- Añadir validaciones y reglas de negocio.
- Preparar pruebas unitarias iniciales.

---

## Notas
- Toda la documentación se actualizará semana a semana.
- Este README sirve como referencia del historial de entregables y avances.
