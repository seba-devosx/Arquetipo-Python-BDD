@busqueda_autos
Feature:prueba de formulario web
    @testf1
    Scenario Outline: ingreso de datos a formulario
        Given ingreso a la url "https://computer-database.gatling.io/computers"
        When seleccione el filtro
        And ingrese el nombre de la marca <nombre> 
        Examples:
            | nombre |
            | Apple  |