def add_task(task_list, task_name, priority):
    """Añade una nueva tarea a la lista con prioridad."""
    if priority not in ['Alta', 'Media', 'Baja']:
        print("Prioridad inválida. Debe ser 'Alta', 'Media' o 'Baja'.")
        return
    
    task_id = len(task_list) + 1
    task_list[task_id] = {
        'name': task_name,
        'completed': False,
        'priority': priority
    }
    print(f"Tarea '{task_name}' añadida con ID {task_id} y prioridad {priority}.")

def list_tasks(task_list):
    """Lista todas las tareas con sus prioridades."""
    if not task_list:
        print("No hay tareas en la lista.")
    else:
        for task_id, task_info in task_list.items():
            status = "Completada" if task_info['completed'] else "Pendiente"
            print(f"ID {task_id}: {task_info['name']} - {status} - Prioridad: {task_info['priority']}")

def clear_tasks(task_list):
    """Limpia todas las tareas."""
    task_list.clear()
    print("Todas las tareas han sido eliminadas.")

def mark_task_completed(task_list, task_id):
    """Marca una tarea como completada."""
    if task_id in task_list:
        task_list[task_id]['completed'] = True
        print(f"Tarea ID {task_id} marcada como completada.")
    else:
        print(f"No se encontró la tarea con ID {task_id}.")

def main():
    """Función principal para ejecutar la aplicación."""
    task_list = {}
    
    while True:
        print("\n--- Administrador de Tareas ---")
        print("1. Añadir nueva tarea")
        print("2. Listar todas las tareas")
        print("3. Limpiar todas las tareas")
        print("4. Marcar tarea como completada")
        print("5. Salir")
        
        choice = input("Selecciona una opción (1-5): ")
        
        if choice == '1':
            task_name = input("Introduce el nombre de la tarea: ")
            priority = input("Introduce la prioridad de la tarea (Alta, Media, Baja): ")
            add_task(task_list, task_name, priority)
        elif choice == '2':
            list_tasks(task_list)
        elif choice == '3':
            clear_tasks(task_list)
        elif choice == '4':
            try:
                task_id = int(input("Introduce el ID de la tarea a marcar como completada: "))
                mark_task_completed(task_list, task_id)
            except ValueError:
                print("ID de tarea inválido.")
        elif choice == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 5.")

if __name__ == "__main__":
    main()
