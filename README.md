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
Llevar a cabo la implementación de un escenario práctico que abarque la captura de datos en tiempo real (streaming) desde YouTube como fuente primaria. Estos datos serán adquiridos mediante el servicio canalizador AWS Kinesis. Posteriormente, se dirigirán simultáneamente hacia un Datalake alojado en AWS S3 y hacia un Procesador de Flujos (Apache Flink) encargado de analizar los datos conforme son recibidos. Este análisis se complementará con la visualización gráfica de los datos mediante un graficador.

## ¿Que se logró y que no se logró?
- **Se logró**
  -	Recolectar datos de streming a tiempo real y mandarlos a Kinesis data stream.
  -	Esos datos los mandamos directamente al datalake en S3.
  -	Al mismo tiempo mandamos los datos a Apache Flink para procesarlos.


- **No se logró**:
  - 

## 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas:

## 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

Lenguaje de programacion: 

Librerias :

## 4. descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

