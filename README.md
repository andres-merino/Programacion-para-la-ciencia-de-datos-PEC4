<!-- PROJECT SHIELDS -->
[![Colaboradores][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Estrellas][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Programacion para la ciencia de datos PEC 4</h3>
  <p align="center">
    Solución de la PEC4 de la asignatura Programación para la ciencia de datos de la UOC.  
    <br />
    <a href="https://github.com/andres-merino/Programacion-para-la-ciencia-de-datos-PEC4/issues">Reportar un Problema</a>
  </p>
</div>

## Descripción

Este paquete fue creado para implementar las tareas solicitadas en la PEC4 (ver enunciado [aquí](/ES-PEC4-enun.pdf)) de la asignatura Programación para la ciencia de datos de la Universidad Oberta de Catalunya.

El objetivo es realizar la lectura de datos asociados a información de canciones, álbumes y artistas, los prepare para el análisis, calcule algunas estadísticas básicas y finalmente, cree visualizaciones para comparar diferentes artistas.

Este paquete fue elaborado por Andrés Esteban Merino Toapanta, alumno del programa de Máster universitario en Ciencias de Datos y entregado el 10 de enero de 2022.

### Construido con

![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge) 


## Instalación

Para su instalación, desde la ventana de comandos ubicada en la carpeta donde se encuentra este archivo, se debe colocar el comando:

```
pip install .
```

Los requisitos del paquete se instalan automáticamente y se los puede ver en [requirements.txt](/requirements.txt). En caso de tener problemas con la visualización de las imágenes, se debe instalar la aplicación `tinker` con el siguiente comando.

```
sudo apt-get install python3-tk
```

## Implementación

Para solventar cada una de las 7 tareas (más la octava opcional) solicitadas en la PEC, se generó un módulo por tarea (cuyo nombre coincide con el número de tarea), el cual cuenta con las funciones necesarias para solventar la tarea requerida, es decir, se tienen los módulos: 
- [Tarea1.py](/PEC4/Tarea1.py)
- [Tarea2.py](/PEC4/Tarea2.py)
- [Tarea3.py](/PEC4/Tarea3.py)
- [Tarea4.py](/PEC4/Tarea4.py)
- [Tarea5.py](/PEC4/Tarea5.py)
- [Tarea6.py](/PEC4/Tarea6.py)
- [Tarea7.py](/PEC4/Tarea7.py)
- [Tarea8.py](/PEC4/Tarea8.py)

Además, se implementó el código para que, al compilar el módulo directamente, este devuelva los criterios de aceptación solicitados.


## Uso

Para utilizar cada módulo del paquete, se lo puede importar en un archivo .py o en un notebook de Jyputer con:
```
import from PEC4.Tarea1 import *
```

Por otro lado, se pueden revisar los criterios de cada tareas, ingresando a la carpeta `PEC4` y ejecutando:
```
python3 Tarea1.py
```
con lo cual se despliega los comentarios o gráficos que constatan el cumplimiento del criterio.

Para automatizar la labor del _sufrido revisor_, se generó el archivo [criterios.py](/criterios.py) en el directorio raíz, con lo cual, al ejecutar en la línea de comandos:
```
python3 criterios.py
```
se despliega las evidencias del cumplimiento de los criterios de todas las 8 tareas. Cabe indicar que, para ejecutar este script, es necesario el paquete `subprocess` (el cual no fue incluido en `requirements.txt` ya que, en sí, no es necesario para el funcionamiento del paquete).

## Pruebas

Se generó el archivo [test/test.py](/test/test.py), en el cual se implementaron pruebas utilizando la librería `unittest` (también son necesarias las librerías `math` y `os` que tampoco son colocadas en `requirements.txt` pues no son necesarias para el paquete). Además, se utilizó la herramienta `covarange.py` para medir la calidad de las pruebas, el resultado puede ser visto en [test/htmlcov/index.html](/test/htmlcov/index.html).

## Comentarios sobre la Tarea 8 (opcional)

La implementación es eficiente dado que utiliza hilos para descargar de una manera már rápida la información necesaria, sin embargo, dadas las limitaciones de la API, al hacer tantas solicitudes en un tiempo tan corto, en ocasiones, no se completa la descarga de datos. En caso de escalar el proyecto, sería necesario comprar la llave de API privada y el código reaccionaría de manera correcta. Por otro lado, para evitar esto último, se podría implementar pausas en el código para no sobrepasar las limitaciones de llamadas de la API. Finalmente, si el objetivo es solo descargar los datos (y no tenerlos en un DataFrame en python), se podría mejorar el código para que se escriba la información directamente en el archivo csv.

## Documentación

La documentación se generó de manera automática utilizando `pdoc`.

## Créditos

Andrés Merino (aemerinot@gmail.com)
- Docente-Investigador en Pontificia Universidad Católica del Ecuador
- Fundador del [Proyecto Alephsub0](https://www.alephsub0.org/about/)

[![LinkedIn][linkedin-shield]][linkedin-url-aemt]

## Licencia

Distribuido bajo la licencia MIT. 

[![MIT License][license-shield]][license-url]


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/andres-merino/Programacion-para-la-ciencia-de-datos-PEC4.svg?style=for-the-badge
[contributors-url]: https://github.com/andres-merino/Programacion-para-la-ciencia-de-datos-PEC4/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/andres-merino/Programacion-para-la-ciencia-de-datos-PEC4.svg?style=for-the-badge
[forks-url]: https://github.com/andres-merino/Programacion-para-la-ciencia-de-datos-PEC4/forks
[stars-shield]: https://img.shields.io/github/stars/andres-merino/Programacion-para-la-ciencia-de-datos-PEC4?style=for-the-badge
[stars-url]: https://github.com/andres-merino/Programacion-para-la-ciencia-de-datos-PEC4/stargazers
[issues-shield]: https://img.shields.io/github/issues/andres-merino/Programacion-para-la-ciencia-de-datos-PEC4.svg?style=for-the-badge
[issues-url]: https://github.com/andres-merino/Programacion-para-la-ciencia-de-datos-PEC4/issues
[license-shield]: https://img.shields.io/github/license/andres-merino/Programacion-para-la-ciencia-de-datos-PEC4.svg?style=for-the-badge
[license-url]: https://es.wikipedia.org/wiki/Licencia_MIT
[linkedin-shield]: https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url-aemt]: https://www.linkedin.com/in/andrés-merino-010a9b12b/
