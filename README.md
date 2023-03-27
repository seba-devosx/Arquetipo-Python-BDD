# Arquetipo-Python-BDD
Arquetipo para la realización de testing en software

# lista de comandos
Ejecuctar y generar datos para reporte

```
behave -f allure_behave.formatter:AllureFormatter -o allure-2.10.0/results ./features/Flujo1.feature
```
Generar reporte
La carpeta result se encargara de almacenar los resultados obtenidos en el flujo en formato json
por ende sera necesario ejecutar el siguiente comando el cual levanta un servidor local para visualizar los 
resultados obtenido
```
sh allure-2.10.0/bin/allure serve --clean ../re      allure-2.10.0/results
```