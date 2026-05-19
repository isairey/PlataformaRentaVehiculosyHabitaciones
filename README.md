<div align="center">

<img width="220" src="https://cdn-icons-png.flaticon.com/512/2972/2972185.png" />

# 🏡 FAER – Rental & Accommodation Platform

### Plataforma inteligente de renta de habitaciones y vehículos 🚀

<p align="center">
  <b>FAER</b> es una plataforma moderna enfocada en la administración y alquiler de habitaciones, departamentos y vehículos, diseñada para ofrecer una experiencia rápida, segura y escalable.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Rental-System-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Property-Management-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Vehicle-Rental-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/OpenSource-Academic-purple?style=for-the-badge">
</p>

<p align="center">
  <a href="#-acerca-del-proyecto">Acerca</a> •
  <a href="#-módulos-del-sistema">Módulos</a> •
  <a href="#-características">Características</a> •
  <a href="#-tecnologías-utilizadas">Tecnologías</a> •
  <a href="#-estructura-del-proyecto">Estructura</a>
</p>

</div>

---

# 🌌 Acerca del proyecto

**FAER** es un sistema web orientado a la gestión de propiedades y vehículos en renta, permitiendo administrar alojamientos, automóviles y reservas desde una sola plataforma centralizada.

La plataforma fue diseñada para:

- 🏠 Gestionar habitaciones y departamentos
- 🚗 Administrar vehículos en renta
- 👥 Gestionar usuarios y clientes
- 📅 Controlar reservas
- 📍 Mostrar ubicaciones geográficas
- 🖼️ Administrar galerías de imágenes
- 🔐 Gestionar accesos y autenticación
- 📊 Centralizar información de alquileres

---

# ✨ Características

## 🏡 Gestión de propiedades

- 🏠 Registro de habitaciones y departamentos
- 🛏️ Configuración de tipos de habitación
- 📍 Ubicación geográfica
- 🖼️ Subida de imágenes
- 💰 Configuración de precios
- 🛁 Gestión de baños y habitaciones
- 🌐 Servicios incluidos
- 🏢 Gestión de pisos y ocupación

---

## 🚗 Gestión de vehículos

- 🚘 Registro de automóviles y motocicletas
- 📋 Gestión de placas y modelos
- 🏷️ Clasificación por tipo
- 💰 Administración de precios
- 👥 Control de capacidad
- 🖼️ Galería de imágenes
- 📊 Información detallada

---

## 👥 Gestión de usuarios

- 👤 Registro de clientes
- 🔐 Inicio de sesión
- 📄 Gestión de perfiles
- 📅 Historial de reservas
- ⚡ Administración centralizada

---

## 📅 Sistema de reservas

- 📆 Reservas de habitaciones
- 🚗 Reservas de vehículos
- ⏳ Control de disponibilidad
- 💳 Gestión de pagos
- 📊 Historial de alquileres
- 🔔 Notificaciones automáticas

---

# 👨‍💼 Módulos del sistema

## 🏠 Room Module

Módulo dedicado a la administración de habitaciones y alojamientos.

### Funcionalidades:

- ➕ Registro de propiedades
- 🛏️ Configuración de habitaciones
- 📍 Gestión de direcciones
- 🖼️ Subida de imágenes
- 💰 Gestión de precios
- 🌐 Configuración de servicios
- 📅 Disponibilidad y reservas

---

## 🚗 Vehicle Module

Módulo orientado al alquiler y administración de vehículos.

### Funcionalidades:

- 🚘 Registro de vehículos
- 📋 Gestión de modelos y marcas
- 🏷️ Clasificación por tipo
- 💰 Configuración de precios
- 👥 Gestión de capacidad
- 🖼️ Administración de imágenes
- 📅 Control de disponibilidad

---

## 👤 User Module

Módulo de gestión de usuarios y clientes.

### Funcionalidades:

- 🔐 Autenticación
- 👥 Gestión de clientes
- 📄 Administración de perfiles
- 📅 Historial de reservas
- ⚡ Gestión de permisos

---

# 🛠️ Tecnologías utilizadas

## 🎨 Frontend

<p>
  <img src="https://skillicons.dev/icons?i=html,css,js,bootstrap" />
</p>

- HTML5
- CSS3
- JavaScript
- Bootstrap

---

## ⚙️ Backend

<p>
  <img src="https://skillicons.dev/icons?i=python,django" />
</p>

- Python
- Django
- Sistema CRUD
- Arquitectura MVC

---

## 🗄️ Base de datos

<p>
  <img src="https://skillicons.dev/icons?i=postgres,mysql" />
</p>

- PostgreSQL / MySQL
- Persistencia de datos
- Relaciones SQL
- Gestión de reservas

---

## 🧰 Herramientas

<p>
  <img src="https://skillicons.dev/icons?i=git,github,vscode" />
</p>

- Git
- GitHub
- Visual Studio Code
- Postman

---

# 📂 Estructura del proyecto

```bash
FAER/
│
├── rooms/                     # Gestión de habitaciones
├── vehicles/                  # Gestión de vehículos
├── users/                     # Usuarios y autenticación
├── bookings/                  # Sistema de reservas
├── media/                     # Imágenes y archivos
├── templates/                 # Plantillas HTML
├── static/                    # Archivos CSS y JS
├── database/                  # Configuración de BD
├── manage.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🏡 Modelo Room

## 📋 Atributos principales

- 🏠 Tipo de alojamiento
- 🛏️ Tipo de habitación
- 👥 Ocupación total
- 🛁 Cantidad de baños
- 🌐 Servicios incluidos
- 📍 Ubicación geográfica
- 🖼️ Galería de imágenes
- 💰 Precio de renta

---

# 🚗 Modelo Vehicle

## 📋 Atributos principales

- 🚘 Nombre del vehículo
- 🏷️ Tipo de vehículo
- 🏭 Marca y modelo
- 📋 Número de placa
- 👥 Capacidad
- 💰 Precio de renta
- 🖼️ Imágenes del vehículo

---

# ⚡ Instalación

## 📋 Requisitos

- Python 3.10+
- Django
- PostgreSQL / MySQL
- Git
- Navegador moderno

---

# 🚀 Configuración del proyecto

## 1️⃣ Clonar repositorio

```bash
git clone https://github.com/isairey/FAER.git
```

---

## 2️⃣ Entrar al proyecto

```bash
cd FAER
```

---

## 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Ejecutar migraciones

```bash
python manage.py migrate
```

---

## 5️⃣ Ejecutar servidor

```bash
python manage.py runserver
```

---

## 6️⃣ Abrir aplicación

```bash
http://127.0.0.1:8000
```

---

# 📊 Funcionalidades principales

## 🏠 Gestión de propiedades

- Registro de habitaciones
- Gestión de departamentos
- Servicios incluidos
- Control de ocupación

---

## 🚗 Gestión vehicular

- Administración de vehículos
- Clasificación por tipo
- Gestión de disponibilidad
- Control de reservas

---

## 📅 Sistema de reservas

- Reservas online
- Historial de alquileres
- Gestión de disponibilidad
- Confirmaciones automáticas

---

# 📸 Vista previa

## 🖥️ Interfaces del sistema

<div align="center">

### 🏠 Página principal
![Home](https://images.unsplash.com/photo-1560518883-ce09059eeffa?q=80&w=1200)

### 🛏️ Gestión de habitaciones
![Rooms](https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?q=80&w=1200)

### 🚗 Gestión de vehículos
![Vehicles](https://images.unsplash.com/photo-1494976388531-d1058494cdd8?q=80&w=1200)

### 📅 Sistema de reservas
![Booking](https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?q=80&w=1200)

</div>

---

# 🧠 Objetivos del proyecto

## 🎯 Aprendizaje y administración

- Desarrollo web full stack
- Gestión de propiedades
- Administración vehicular
- Arquitectura MVC
- Sistemas de reservas
- Bases de datos relacionales
- CRUD avanzados

---

# 🚧 Roadmap

## 🔮 Próximas mejoras

- 📱 Aplicación móvil
- 💳 Integración de pagos
- ☁️ Infraestructura cloud
- 🤖 Recomendaciones inteligentes
- 📊 Dashboard avanzado
- 🌐 API REST
- 🔔 Notificaciones en tiempo real

---

# 🤝 Contribuciones

Las contribuciones son bienvenidas ❤️

## Cómo contribuir

1. Fork del proyecto

```bash
git checkout -b feature/nueva-funcionalidad
```

2. Commit

```bash
git commit -m "✨ Nueva funcionalidad"
```

3. Push

```bash
git push origin feature/nueva-funcionalidad
```

4. Pull Request 🚀

---

# 👨‍💻 Desarrollador

<div align="center">

## Isai Reyes — Full Stack Developer

Desarrollador apasionado por plataformas de renta, sistemas administrativos y soluciones web modernas 🚀

</div>

---

# 🌟 Apoya el proyecto

⭐ Dale una estrella  
🍴 Haz fork  
📢 Comparte el proyecto

---

# 📜 Licencia

Proyecto open source bajo licencia MIT orientado al aprendizaje y desarrollo de plataformas de renta modernas.

---

<div align="center">

### 🏡 FAER — gestión inteligente de propiedades y vehículos 🚀

</div>
