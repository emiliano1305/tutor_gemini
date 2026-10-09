from __future__ import annotations

import re
import unicodedata


LESSONS = [
    {
        "title": "1. ¿Qué es Python?",
        "keywords": ["python", "lenguaje", "programar", "programacion", "programa", "codigo"],
        "objective": "Entender qué es Python y ejecutar una primera instrucción.",
        "explanation": "Python es un lenguaje de programación: permite escribir instrucciones para que la computadora realice tareas. Se usa, entre otras cosas, para automatizar tareas, trabajar con datos y crear aplicaciones.",
        "code": 'print("Hola, mundo")',
        "walkthrough": "`print` le indica a Python que muestre algo en pantalla. El texto está entre comillas.",
        "exercise": "Cambiá el texto para que el programa salude a alguien por su nombre.",
    },
    {
        "title": "2. Variables y tipos de datos",
        "keywords": ["variable", "variables", "tipo", "datos", "entero", "decimal", "texto", "booleano", "str", "int", "float", "bool"],
        "objective": "Guardar y reconocer valores en un programa.",
        "explanation": "Una variable es un nombre asociado a un valor. Python reconoce distintos tipos: números enteros (`int`), decimales (`float`), textos (`str`) y valores de verdadero/falso (`bool`).",
        "code": 'nombre = "Ana"\nedad = 12\naltura = 1.55\nestudia_python = True\nprint(nombre, edad)',
        "walkthrough": "`nombre` guarda texto, `edad` un entero, `altura` un decimal y `estudia_python` un valor booleano. El signo `=` asigna el valor a la variable.",
        "exercise": "Creá una variable `ciudad` con el nombre de tu ciudad y mostrá su contenido con `print`.",
    },
    {
        "title": "3. Entrada de datos",
        "keywords": ["input", "entrada", "usuario", "teclado", "convertir", "conversion"],
        "objective": "Pedir un dato al usuario y convertirlo cuando sea necesario.",
        "explanation": "`input()` pausa el programa y espera que la persona escriba algo. El resultado de `input()` es texto; para hacer cálculos con un número, convertimos ese texto, por ejemplo con `int()`.",
        "code": 'nombre = input("¿Cómo te llamás? ")\nedad = int(input("¿Cuántos años tenés? "))\nprint("Hola", nombre)\nprint("El año que viene tendrás", edad + 1)',
        "walkthrough": "La primera línea guarda el texto escrito. La segunda convierte la respuesta a un entero para poder sumarle 1.",
        "exercise": "Pedí un número con `input`, convertílo a entero y mostrale al usuario el doble.",
    },
    {
        "title": "4. Operaciones y expresiones",
        "keywords": ["operador", "operadores", "suma", "sumar", "sumo", "resta", "multiplicar", "division", "expresion", "calculo", "aritmetica"],
        "objective": "Hacer cálculos usando los operadores básicos.",
        "explanation": "Python puede calcular con `+` (suma), `-` (resta), `*` (multiplicación) y `/` (división). Una expresión combina valores y operadores para producir un resultado.",
        "code": 'a = 8\nb = 2\nprint(a + b)  # 10\nprint(a * b)  # 16\nprint(a / b)  # 4.0',
        "walkthrough": "Python evalúa cada expresión y `print` muestra el resultado. La división `/` produce un número decimal.",
        "exercise": "Guardá dos números en variables y calculá la suma y la diferencia.",
    },
    {
        "title": "5. Decisiones: if y else",
        "keywords": ["if", "else", "elif", "condicion", "condiciones", "condicional", "decision", "comparar"],
        "objective": "Hacer que el programa elija qué instrucciones ejecutar.",
        "explanation": "Una condición permite ejecutar instrucciones según si una expresión es verdadera o falsa. Python usa `if`, `elif` y `else`. La indentación indica qué instrucciones pertenecen a cada bloque.",
        "code": 'nota = 7\nif nota >= 6:\n    print("Aprobado")\nelse:\n    print("Hay que seguir practicando")',
        "walkthrough": "Python comprueba `nota >= 6`. Si es verdadero, ejecuta el bloque indentado bajo `if`; si no, ejecuta el bloque bajo `else`.",
        "exercise": "Pedí una edad y usá `if` para indicar si es mayor o igual a 18.",
    },
    {
        "title": "6. Repeticiones: bucles for y while",
        "keywords": ["bucle", "bucles", "for", "while", "iteracion", "iterar", "repetir", "range"],
        "objective": "Repetir instrucciones sin copiarlas muchas veces.",
        "explanation": "Un bucle repite un bloque de instrucciones. `for` se usa habitualmente para recorrer elementos o una secuencia; `while` repite mientras una condición siga siendo verdadera.",
        "code": 'for numero in range(1, 4):\n    print(numero)',
        "walkthrough": "`range(1, 4)` produce 1, 2 y 3. En cada vuelta, el valor actual queda guardado en `numero`.",
        "exercise": "Usá un bucle para mostrar los números del 1 al 5.",
    },
    {
        "title": "7. Listas",
        "keywords": ["lista", "listas", "list", "indice", "elemento", "append", "secuencia"],
        "objective": "Guardar y recorrer varios valores en una colección ordenada.",
        "explanation": "Una lista guarda varios elementos en orden. Se escribe entre corchetes. Los índices empiezan en 0, y `append()` agrega un elemento al final.",
        "code": 'frutas = ["manzana", "pera"]\nfrutas.append("banana")\nprint(frutas[0])  # manzana\nfor fruta in frutas:\n    print(fruta)',
        "walkthrough": "`frutas[0]` obtiene el primer elemento. El bucle recorre cada elemento de la lista.",
        "exercise": "Creá una lista con tres colores y usá un bucle para mostrar cada uno.",
    },
    {
        "title": "8. Funciones",
        "keywords": ["funcion", "funciones", "def", "return", "parametro", "argumento"],
        "objective": "Agrupar instrucciones y reutilizarlas con distintos valores.",
        "explanation": "Una función es un bloque reutilizable. `def` la define, los parámetros reciben datos y `return` devuelve un resultado.",
        "code": 'def sumar(a, b):\n    return a + b\n\nresultado = sumar(3, 4)\nprint(resultado)  # 7',
        "walkthrough": "`sumar` recibe `a` y `b`, calcula su suma y la devuelve. Luego se llama con 3 y 4.",
        "exercise": "Escribí una función que reciba un número y devuelva su doble.",
    },
    {
        "title": "9. Diccionarios",
        "keywords": ["diccionario", "diccionarios", "dict", "clave", "valor", "key"],
        "objective": "Guardar datos asociados a una clave.",
        "explanation": "Un diccionario relaciona claves con valores. Se escribe entre llaves como pares `clave: valor`; se consulta usando la clave.",
        "code": 'alumno = {"nombre": "Ana", "nota": 8}\nprint(alumno["nombre"])\nalumno["nota"] = 9',
        "walkthrough": "`alumno` tiene las claves `nombre` y `nota`. La asignación final actualiza el valor asociado a `nota`.",
        "exercise": "Armá un diccionario con las claves `nombre` y `curso`, y mostrá el curso.",
    },
    {
        "title": "10. Errores y excepciones",
        "keywords": ["error", "errores", "excepcion", "excepciones", "try", "except", "debug", "depurar"],
        "objective": "Entender un error común y responder a él sin que el programa termine abruptamente.",
        "explanation": "Los errores son parte del aprendizaje. `try` permite ejecutar instrucciones que podrían fallar y `except` define qué hacer si ocurre una excepción. Conviene capturar el tipo de error esperado.",
        "code": 'try:\n    edad = int(input("Edad: "))\n    print(edad)\nexcept ValueError:\n    print("Ingresá la edad con números")',
        "walkthrough": "Si la persona escribe algo que no puede convertirse a entero, ocurre `ValueError` y se ejecuta el bloque `except`.",
        "exercise": "¿Qué error puede aparecer si intentás convertir el texto `hola` a entero con `int()`?",
    },
    {
        "title": "11. Archivos",
        "keywords": ["archivo", "archivos", "leer", "escribir", "open", "fichero"],
        "objective": "Abrir un archivo de texto y leer o guardar información.",
        "explanation": "Python puede trabajar con archivos. `open()` abre un archivo y el modo `"r"` se usa para lectura. El bloque `with` ayuda a cerrar el archivo cuando termina el trabajo.",
        "code": 'with open("notas.txt", "r", encoding="utf-8") as archivo:\n    contenido = archivo.read()\n    print(contenido)',
        "walkthrough": "`with` abre el archivo y lo cierra al salir del bloque. `read()` obtiene su contenido como texto.",
        "exercise": "¿Qué modo de `open()` se usa habitualmente para leer un archivo?",
    },
    {
        "title": "12. Clases y objetos: primera mirada",
        "keywords": ["clase", "clases", "objeto", "objetos", "class", "instancia", "poo"],
        "objective": "Reconocer la idea básica de una clase y un objeto.",
        "explanation": "Una clase define una estructura y comportamientos; un objeto es un ejemplar creado a partir de esa clase. Es un tema para después de practicar variables, funciones y colecciones.",
        "code": 'class Mascota:\n    def __init__(self, nombre):\n        self.nombre = nombre\n\nmi_mascota = Mascota("Luna")\nprint(mi_mascota.nombre)',
        "walkthrough": "`class` define `Mascota`. `__init__` inicializa cada objeto y `self.nombre` guarda el nombre de esa instancia.",
        "exercise": "Identificá el nombre de la clase y el nombre de la instancia en el ejemplo.",
    },
]


RECIPES = {
    "Mostrar un mensaje": {
        "filename": "mensaje.py",
        "code": 'print("Hola, mundo")',
        "explanation": "`print()` muestra texto en la pantalla.",
    },
    "Sumar dos números": {
        "filename": "sumar_dos_numeros.py",
        "code": 'numero1 = float(input("Primer número: "))\nnumero2 = float(input("Segundo número: "))\nresultado = numero1 + numero2\nprint("La suma es:", resultado)',
        "explanation": "El programa pide dos datos, los convierte a números decimales con `float()`, los suma y muestra el resultado.",
    },
    "Decidir si una nota aprueba": {
        "filename": "nota.py",
        "code": 'nota = float(input("Ingresá la nota: "))\nif nota >= 6:\n    print("Aprobado")\nelse:\n    print("A seguir practicando")',
        "explanation": "`if` compara la nota con 6; el programa muestra un mensaje según el resultado.",
    },
    "Repetir números con un bucle": {
        "filename": "bucle.py",
        "code": 'for numero in range(1, 6):\n    print(numero)',
        "explanation": "`range(1, 6)` genera 1, 2, 3, 4 y 5. El bucle muestra cada valor.",
    },
    "Crear una función": {
        "filename": "funcion_doble.py",
        "code": 'def doble(numero):\n    return numero * 2\n\nprint(doble(5))  # 10',
        "explanation": "La función recibe un número y devuelve el doble. Después se llama con el valor 5.",
    },
}

QUIZZES = [
    {
        "question": "¿Qué función muestra información en pantalla?",
        "options": ["input()", "print()", "range()"],
        "answer": "print()",
        "explanation": "`print()` muestra valores en pantalla; `input()` pide un dato.",
    },
    {
        "question": "¿Qué índice corresponde al primer elemento de una lista?",
        "options": ["0", "1", "-1"],
        "answer": "0",
        "explanation": "En Python, el índice del primer elemento es 0.",
    },
    {
        "question": "¿Qué palabra se usa para definir una función?",
        "options": ["func", "def", "return"],
        "answer": "def",
        "explanation": "`def` inicia la definición de una función; `return` devuelve un resultado.",
    },
    {
        "question": "¿Qué tipo de dato devuelve directamente input()?",
        "options": ["Texto (str)", "Entero (int)", "Verdadero/falso (bool)"],
        "answer": "Texto (str)",
        "explanation": "`input()` devuelve texto; hay que convertirlo si se necesita un número.",
    },
]


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", text.casefold())
    text = "".join(char for char in text if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9_]+", " ", text).strip()


def find_lesson(query: str) -> dict | None:
    normalized_query = normalize(query)
    if not normalized_query:
        return None
    query_words = set(normalized_query.split())
    scored: list[tuple[int, dict]] = []
    generic_keywords = {"python", "lenguaje", "programar", "programacion", "programa", "codigo"}
    for lesson in LESSONS:
        score = 0
        for keyword in lesson["keywords"]:
            normalized_keyword = normalize(keyword)
            if " " in normalized_keyword:
                if normalized_keyword in normalized_query:
                    score += 1 if normalized_keyword in generic_keywords else 3
            elif normalized_keyword in query_words:
                score += 1 if normalized_keyword in generic_keywords else (3 if len(normalized_keyword) > 3 else 1)
        if score:
            scored.append((score, lesson))
    if not scored:
        return None
    scored.sort(key=lambda item: item[0], reverse=True)
    return scored[0][1]
