## info de la materia: Tópicos especiales en Telemática st0263 
#
## Estudiante(s): 
- Simon Gomez Arango - sgomez13@eafit.edu.co
- Sara María Castrillón Ríos - smcastril1@eafit.edu.co
- Manuela Tolosa - mtolosag@eafit.edu.co
#
## Profesor: 
Edwin Nelson Montoya Múnera - emontoya@eafit.edu.co
#

# Arquitectura Streaming para big data

## 1. breve descripción de la actividad
Llevamos a cabo la implementación de un escenario práctico que abarque la captura de datos en tiempo real (streaming) desde YouTube como fuente primaria. Estos datos serán adquiridos mediante el servicio canalizador AWS Kinesis. Posteriormente, se dirigirán simultáneamente hacia un Datalake alojado en AWS S3 y hacia un Procesador de Flujos (Apache Flink) encargado de analizar los datos conforme son recibidos. Este análisis se complementará con la visualización gráfica de los datos mediante un graficador.

## ¿Que se logró y que no se logró?
- **Se logró**
  -	Recolectar datos de streming a tiempo real y mandarlos a Kinesis data stream.
  -	Esos datos los mandamos directamente al datalake en S3.
  -	Al mismo tiempo mandamos los datos a Apache Flink para procesarlos.
  -Sacamos diferentes stadisticas en el notebook.

- **No se logró**:
  - Exportar los datos finales despues de procesarlos para que queden de manera persistente.

## 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas:
![image](https://github.com/sgomeza13/YoutubeLiveChatAnalysis/assets/74980999/7b275242-c4e0-4cfb-94fd-8d049517a2d2)
## 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

Lenguaje de programación: Python.

Librerias : pychat, boto3, Flask, pyflink.

## 4. descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
- Estamos usando un .env para cargar las variables de entorno
- IP
  - En la siguiente IP tenemos corriendo un servidor de Flask al que le podemos mandar una petición HTTP para pasarle el ID del directo de YouTube del cual queremos tener los comentarios en tiempo real. ( 52.2.10.125 )
    
 ![image](https://github.com/sgomeza13/YoutubeLiveChatAnalysis/assets/74980999/dab6e42b-8685-41d5-b021-0e5952530a94)
 ![image](https://github.com/sgomeza13/YoutubeLiveChatAnalysis/assets/74980999/a0b4f315-1b53-466a-933b-a8bc6fd2d430)

## video sustentación: https://www.youtube.com/watch?v=yiARRCB0lA4

## 5. referencia :
- Query your data streams in real time with kinesis data analytics studio | Amazon web services. (2021, julio 15). https://www.youtube.com/watch?v=SX_6x_wXIfA&t=1s

