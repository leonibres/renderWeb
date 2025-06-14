const express = require("express");
const path = require("path");

const app = express();
const port = process.env.PORT || 8080;

// Sirve los archivos estáticos desde el directorio "dist"
app.use(express.static(path.join(__dirname, "dist")));

// Redirige todas las rutas al archivo "index.html"
app.get("*", (req, res) => {
  res.sendFile(path.join(__dirname, "dist", "index.html"));
});

app.listen(port, () => {
  console.log(`Servidor iniciado en el puerto ${port}`);
});
