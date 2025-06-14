const express = require("express");
const path = require("path");
const fs = require("fs");

const app = express();
const port = process.env.PORT || 8080;

// Logs de diagnóstico
console.log("Iniciando servidor Express...");
console.log(`Directorio actual: ${__dirname}`);
console.log(`Puerto configurado: ${port}`);

// Verifica si el directorio dist existe
const distPath = path.join(__dirname, "dist");
if (fs.existsSync(distPath)) {
  console.log(`Directorio dist encontrado en: ${distPath}`);
  
  // Lista los archivos en el directorio dist
  const files = fs.readdirSync(distPath);
  console.log(`Archivos en dist: ${files.join(', ')}`);
} else {
  console.error(`Error: Directorio dist no encontrado en ${distPath}`);
}

// Sirve los archivos estáticos desde el directorio "dist"
app.use(express.static(distPath));

// Middleware para registrar peticiones
app.use((req, res, next) => {
  console.log(`${new Date().toISOString()} - ${req.method} ${req.url}`);
  next();
});

// Redirige todas las rutas al archivo "index.html"
app.get("*", (req, res) => {
  const indexPath = path.join(distPath, "index.html");
  
  if (fs.existsSync(indexPath)) {
    console.log(`Redirigiendo ${req.path} a index.html`);
    res.sendFile(indexPath);
  } else {
    console.error(`Error: index.html no encontrado en ${indexPath}`);
    res.status(404).send('Archivo index.html no encontrado');
  }
});

// Manejador de errores
app.use((err, req, res, next) => {
  console.error(`Error: ${err.message}`);
  res.status(500).send('Ha ocurrido un error en el servidor');
});

// Inicia el servidor
const server = app.listen(port, () => {
  console.log(`Servidor iniciado en el puerto ${port}`);
});

// Manejo de errores del servidor
server.on('error', (error) => {
  console.error(`Error en el servidor: ${error.message}`);
  // Si el puerto está en uso, intentar con otro puerto
  if (error.code === 'EADDRINUSE') {
    console.log(`Puerto ${port} en uso, intentando con puerto ${port + 1}`);
    server.listen(port + 1);
  }
});

// Manejo de señales de terminación
process.on('SIGTERM', () => {
  console.log('Señal SIGTERM recibida, cerrando servidor...');
  server.close(() => {
    console.log('Servidor cerrado');
    process.exit(0);
  });
});
