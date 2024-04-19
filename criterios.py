import subprocess


for i in range(1, 9):
    print(f"Criterios de la tarea {i}")
    print("(en caso de que se despliegue una imagen,",
          "cerrala para continuar con la revisión de criterios)")
    subprocess.run(f'python3 PEC4/Tarea{i}.py', shell=True)
    print("\n")
