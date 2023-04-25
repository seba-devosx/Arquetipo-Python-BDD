# Arquetipo-Python-BDD
Arquetipo para la realización de testing en software

# lista de comandos
Ejecuctar y generar datos para reporte

```
behave -f allure_behave.formatter:AllureFormatter -o allure-2.10.0/results ./features/Flujo1.feature
```
Una vez ejecutado el comando anterior este ejecutara el feature seleccionado deplegando en navegador
en tu pantalla e iniciara el flujo a ejecuctar, el arquetipo esta configurado para que despues de cada
prueba este realizara la captura de cada uno de los pasos que se van ejecutando, para cuando 
termine el proceso de ejecucion deplegue el reporte de allure en tu navegador, en el podras visualizar 
la cantidad de step los cuales hayan pasado de manera satisfactoria la prueba y en cuales han habido fallos