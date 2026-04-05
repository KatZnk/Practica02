
import numbers

def limpieza(students):
    procesados = {}

    for s in students:
        name = s.get("name")
        grade_raw = s.get("grade")

        if name is None or str(name).strip() == "":
            continue
        name_norm = name.strip().title()

        if grade_raw is None:
            continue
            
        grade_str = str(grade_raw).strip()
        
        if grade_str == "" or not grade_str.replace(".", "", 1).isdigit():
            continue
            
        grade = float(grade_str)
        status_norm = s.get("status").strip().title()

        if name_norm in procesados:
            if grade > procesados[name_norm]["grade"]:
                procesados[name_norm]["grade"] = grade
        else:
            procesados[name_norm] = {
                "name": name_norm, 
                "grade": grade, 
                "status": status_norm
            }

    lista_final = sorted(procesados.values(), key=lambda x: x["name"])
    
    print("Registros limpios de alumnos:")
    print(f"{'Nombre':<20} {'Nota':<6} {'Estado'}")
    print("-" * 42)
    
    for alu in lista_final:
        print(f"{alu['name']:<20} {alu['grade']:<6} {alu['status']}")
    
    print("-" * 42)
    print(f"Total de alumnos válidos: {len(lista_final)}")