# 📦 Sistema de Inventario - IS2 Grupo 3 (2025)

Este proyecto forma parte del trabajo práctico grupal de la materia **Ingeniería de Software II** de la Universidad Nacional de José C. Paz. El objetivo es desarrollar un sistema de gestión de inventario utilizando Python, siguiendo un enfoque iterativo de 12 semanas.

## 👥 Integrantes del grupo

- Gustavo Paniagua [@gusty89]
- Alejo Escurra [@codex-00]
- Gonzalo Rosa [@gonzarosa]
- Anabel Cano [@]
- Nahuel Lemos [@]

## 🚀 Tecnologías utilizadas

- Python 3.11+
- FastAPI
- SQLAlchemy
- SQLite (modo local)
- Jinja2 (para vistas web)
- Docker (semana 10)
- GitHub Actions (CI/CD simulado)
- Pytest (para pruebas)

## 📁 Estructura del proyecto (tentativa)

inventario/
├── main.py  
├── models/  
│   ├── producto.py  
│   ├── deposito.py  
│   └── movimiento.py  
├── routers/  
│   └── api.py  
├── templates/  
│   └── base.html  
├── static/  
│   └── styles.css  
├── tests/  
│   └── test_modelos.py  
├── docs/  
│   └── modelo_dominio.png  
├── requirements.txt  
└── README.md


## 🗓️ Plan de trabajo (12 semanas)

| Semana | Enfoque principal |
|--------|-------------------|
| 1      | Setup del entorno, Git y análisis inicial |
| 2      | Diseño del modelo de dominio |
| 3      | CRUD de productos y depósitos |
| 4      | Gestión de movimientos |
| 5      | Autenticación y roles |
| 6      | Pruebas + Swagger |
| 7      | Vistas web con Jinja2 |
| 8      | Formularios y validaciones |
| 9      | Reportes y alertas |
| 10     | Docker + CI/CD |
| 11     | Refactor + mejora visual |
| 12     | Demo final + presentación |

## 📐 Modelo de Dominio

El sistema se basa en tres entidades principales:

- **Producto**: nombre, código, unidad, stock
- **Depósito**: nombre, ubicación, capacidad
- **Movimiento**: tipo (entrada/salida), fecha, cantidad, producto, depósito

## 🧪 Pruebas

Las pruebas unitarias se desarrollan con `pytest` y se ubican en la carpeta `/tests`.

## 📦 Docker y CI/CD

A partir de la semana 10 se incluirá un entorno dockerizado y flujos automatizados con GitHub Actions.

## 📄 Licencia

Uso académico exclusivo. No distribuir sin autorización del equipo.



