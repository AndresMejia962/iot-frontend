# Frontend - Sistema IoT Distribuido

Frontend desarrollado con React + TypeScript + Vite + Tailwind CSS para el sistema IoT distribuido con Apache Cassandra.

## 🚀 Características

- ✅ Formulario para crear nuevas lecturas de sensores
- ✅ Panel de filtros para buscar lecturas por sede y tipo de sensor
- ✅ Tabla de resultados con todas las lecturas
- ✅ Interfaz moderna y responsive con Tailwind CSS
- ✅ Manejo de errores y estados de carga

## 📦 Instalación

```bash
npm install
```

## 🏃 Ejecutar en desarrollo

```bash
npm run dev
```

La aplicación estará disponible en `http://localhost:5173`

## 🏗️ Build para producción

```bash
npm run build
```

Los archivos optimizados se generarán en la carpeta `dist/`

## 🌐 API

El frontend está configurado por defecto para conectarse a la API desplegada en:
`https://iot-db-distribuida-252092889958.us-central1.run.app`

### Cambiar entre API Local y Producción

Si necesitas apuntar a otra API (por ejemplo, otra instancia en Cloud Run), crea un archivo `.env.local`:

```env
# frontend/.env.local
VITE_API_URL=https://iot-db-distribuida-252092889958.us-central1.run.app
```

> Si no defines la variable, se usará automáticamente la API pública en Cloud Run.

## 📁 Estructura del Proyecto

```
frontend/
├── src/
│   ├── components/
│   │   ├── ReadingForm.tsx      # Formulario para crear lecturas
│   │   ├── ReadingList.tsx      # Tabla de lecturas
│   │   └── FilterPanel.tsx      # Panel de filtros
│   ├── App.tsx                  # Componente principal
│   ├── main.tsx                 # Punto de entrada
│   └── style.css                # Estilos de Tailwind
├── index.html
├── package.json
└── tailwind.config.js
```

## 🎨 Tecnologías

- **React 18** - Biblioteca de UI
- **TypeScript** - Tipado estático
- **Vite** - Build tool y dev server
- **Tailwind CSS** - Framework de CSS utility-first
- **Axios** - Cliente HTTP

