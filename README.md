# Traductor de lenguaje de manos

## Desarrollador
Rene Alejandro Rengel Arevalo  
Código de estudiante: 49962

## Descripción del Proyecto
El "Traductor de lenguaje de manos" es un proyecto que utiliza las bibliotecas Mediapipe y FastAPI para crear una aplicación que abre la cámara de la computadora, reconoce la mano del usuario y, al hacer signos correspondientes al alfabeto en lenguaje de señas, muestra en pantalla la letra correspondiente.

## Version de Python
Debido a problemas de compatibilidad con algunas librerias, se utilizo python 3.8.0.

## Instrucciones de Uso
1. Instale las dependencias especificadas en el archivo `requirements.txt`.
2. Cambie al directorio "app".
3. Ejecute el siguiente comando para iniciar el servidor en el puerto 8000 de su localhost:
   uvicorn main:app --reload
4. Ejecute la aplicacion con el boton Run en Visual Studio Code

### Al momento el proyecto logra reconocer las letras:
"A"
"E"
"I"
"O"
"U"
"B"
"D"
"K"
"L"
"W"
"N"
"Y"
"F"
"P"

