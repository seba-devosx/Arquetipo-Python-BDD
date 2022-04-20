@haka
Feature:prueba de formulario
    @haka1
    Scenario Outline: ingreso de datos dentro de un formulario
        Given ingreso a la siguiente url "https://www.hakalab.com/"
        When seleccione el apartado de hakatool
        And seleccione formulario
        And ingrese el nombre <nombre> ,<correo> ,<dir1> ,<dir2>
        Examples:
            | nombre | correo        | dir1            | dir2       |
            | axl    | axl@gmail.com | AV siempre viva | Av mexico |