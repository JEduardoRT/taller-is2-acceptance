# steps.py
import io
import contextlib
from behave import given, when, then
from todo import add_task, list_tasks, clear_tasks, mark_task_completed

# Diccionario global para simular la lista de tareas en memoria
task_list = {}

@given('la lista to-do está vacía')
def step_given_list_is_empty(context):
    global task_list
    task_list = {}

@when('el usuario añade una tarea "{task_name}"')
def step_when_user_adds_task(context, task_name):
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        add_task(task_list, task_name, 'Baja')
    context.output = f.getvalue().strip()

@then('la lista to-do debería contener "{expected_task}"')
def step_then_list_should_contain(context, expected_task):
    assert context.output == expected_task

@given('La lista to-do contiene las tareas : ID 1: Comprar dulces, ID 2: Pagar facturas')
def step_given_list_with_tasks(context):
    global task_list
    task_list = {
        1: {'name': 'Comprar dulces', 'completed': False, 'priority': 'Media'},
        2: {'name': 'Pagar facturas', 'completed': False, 'priority': 'Alta'}
    }

@when('el usuario enlista todas las tareas')
def step_when_user_lists_tasks(context):
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        list_tasks(task_list)
    context.output = f.getvalue().strip()

@then('la salida debería contener: "{expected_tasks}"')
def step_then_output_should_contain(context, expected_tasks):
    expected_tasks = expected_tasks.replace(',', '\n')  # Ensure consistent character encoding
    assert context.output == expected_tasks

@given('la lista to-do contiene las tareas: Comprar dulces – Pendiente')
def step_given_list_with_one_task(context):
    global task_list
    task_list = {
        1: {'name': 'Comprar dulces', 'completed': False, 'priority': 'Baja'}
    }

@when('el usuario complete la tarea "{task_name}"')
def step_when_user_completes_task(context, task_name):
    task_id = next(id for id, task in task_list.items() if task['name'] == task_name)
    mark_task_completed(task_list, task_id)

@then('la lista to-do debería mostrar la tarea "{task_name}" como completada')
def step_then_task_should_be_completed(context, task_name):
    task_id = next(id for id, task in task_list.items() if task['name'] == task_name)
    assert task_list[task_id]['completed'] is True

@given('la lista to-do contiene las tareas: Comprar dulces, Pagar facturas')
def step_given_list_to_clean(context):
    global task_list
    task_list = {
        1: {'name': 'Comprar dulces', 'completed': False, 'priority': 'Media'},
        2: {'name': 'Pagar facturas', 'completed': False, 'priority': 'Alta'}
    }

@when('el usuario limpia la lista to-do')
def step_when_user_clears_list(context):
    clear_tasks(task_list)

@then('la lista to-do debería estar vacía')
def step_then_list_should_be_empty(context):
    assert not task_list

@given('la lista to-do está vacía 2')
def step_given_empty_list_priority(context):
    global task_list
    task_list = {}

@when('el usuario añade una tarea: "{task_name}" y asigna la prioridad {priority}')
def step_when_user_adds_task_with_priority(context, task_name, priority):
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        add_task(task_list, task_name, priority)
    context.output = f.getvalue().strip()

@then('la lista to-do debería contener: "{expected_task}"')
def step_then_list_should_contain_with_priority(context, expected_task):
    assert context.output == expected_task
