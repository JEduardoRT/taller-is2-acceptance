# everything.feature

Feature: Administrar tareas en la lista to-do

  Scenario: Añadir una tarea a la lista to-do
    Given la lista to-do está vacía
    When el usuario añade una tarea "Comprar dulces"
    Then la lista to-do debería contener "Tarea 'Comprar dulces' añadida con ID 1 y prioridad Baja."

  Scenario: Lista todas las tareas en la lista to-do
    Given La lista to-do contiene las tareas : ID 1: Comprar dulces, ID 2: Pagar facturas
    When el usuario enlista todas las tareas
    Then la salida debería contener: "ID 1: Comprar dulces - Pendiente - Prioridad: Media, ID 2: Pagar facturas - Pendiente - Prioridad: Alta"


  Scenario: Marca una tarea como completada
    Given la lista to-do contiene las tareas: Comprar dulces – Pendiente
    When el usuario complete la tarea "Comprar dulces"
    Then la lista to-do debería mostrar la tarea "Comprar dulces" como completada

  Scenario: Limpia toda la lista to-do
    Given la lista to-do contiene las tareas: Comprar dulces, Pagar facturas
    When el usuario limpia la lista to-do
    Then la lista to-do debería estar vacía

  Scenario: Crear una tarea y asignar prioridad
    Given la lista to-do está vacía
    When el usuario añade una tarea: “Pagar facturas”
    And asigna la prioridad Media
    Then la lista to-do debería contener: “ID 1: Pagar facturas – Pendiente – Prioridad: Media”
