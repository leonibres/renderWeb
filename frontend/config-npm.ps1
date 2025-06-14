# Habilitar la ejecución de scripts para la sesión actual
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# Verificar que Node.js esté instalado
$nodeVersion = node --version
if ($?) {
    Write-Host "[OK] Node.js versión $nodeVersion detectada"
} else {
    Write-Host "[ERROR] Node.js no está instalado"
    Write-Host "Por favor, instala Node.js desde https://nodejs.org/"
    exit 1
}

# Verificar npm
$npmVersion = npm --version
if ($?) {
    Write-Host "[OK] npm versión $npmVersion detectada"
} else {
    Write-Host "[ERROR] npm no está instalado correctamente"
    exit 1
}

Write-Host "Configuración completada. Ahora puedes ejecutar:"
Write-Host "npm install"
Write-Host "npm run serve"
