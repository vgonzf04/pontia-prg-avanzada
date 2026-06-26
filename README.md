## Endpoints de la API

La API está disponible en la siguiente URL base:

```text
http://127.0.0.1:8000
```

---

## `GET /`

Comprueba que la API está funcionando correctamente.

### URL

```text
http://127.0.0.1:8000/
```

### Parámetros

No recibe parámetros.

### Respuesta correcta

**Código:** `200 OK`

```json
{
  "msg": "API working correctly."
}
```

---

## `GET /tasks`

Devuelve todas las tareas almacenadas en la base de datos.

### URL

```text
http://127.0.0.1:8000/tasks
```

### Parámetros

No recibe parámetros.

### Respuesta correcta

**Código:** `200 OK`

Devuelve una lista con las tareas existentes.

### Errores posibles

**Código:** `404 Not Found`

Se produce cuando no existe ninguna tarea almacenada.

```json
{
  "detail": "No task has been found"
}
```

---

## `POST /tasks`

Crea una nueva tarea.

### URL

```text
http://127.0.0.1:8000/tasks
```

### Parámetros

Recibe un objeto JSON en el cuerpo de la petición con los datos de la tarea.

| Campo         | Tipo      | Obligatorio | Descripción                                                                 |
| ------------- | --------- | ----------- | --------------------------------------------------------------------------- |
| `title`       | `string`  | Sí          | Título de la tarea. Máximo 30 caracteres.                                   |
| `description` | `string`  | No          | Descripción de la tarea. Máximo 50 caracteres.                              |
| `deadline`    | `date`    | Sí          | Fecha límite de la tarea en formato `YYYY-MM-DD`.                           |
| `completed`   | `boolean` | No          | Indica si la tarea está completada. Si no se envía, por defecto es `False`. |

### Ejemplo de petición

```json
{
  "title": "Sin completed",
  "description": "comprueba default False",
  "deadline": "2027-12-12"
}
```

### Respuesta correcta

**Código:** `201 Created`

Devuelve la tarea creada.

### Errores posibles

**Código:** `400 Bad Request`

Se produce cuando ya existe una tarea con el mismo título.

```json
{
  "detail": "Task already created"
}
```

**Código:** `422 Unprocessable Entity`

Se produce cuando los datos enviados no cumplen con el modelo esperado, por ejemplo si falta un campo obligatorio, si el tipo de dato no es correcto o si la fecha no tiene un formato válido.

---

## `GET /tasks/expired`

Devuelve las tareas cuya fecha límite ya ha pasado.

### URL

```text
http://127.0.0.1:8000/tasks/expired
```

### Parámetros

No recibe parámetros.

### Respuesta correcta

**Código:** `200 OK`

Devuelve una lista con las tareas caducadas.

### Errores posibles

**Código:** `404 Not Found`

Se produce cuando no existe ninguna tarea caducada.

```json
{
  "detail": "No expired tasks were found"
}
```

---

## `GET /tasks/{id}`

Devuelve una tarea concreta según su identificador.

### URL

```text
http://127.0.0.1:8000/tasks/{id}
```

Ejemplo:

```text
http://127.0.0.1:8000/tasks/2
```

### Parámetros

| Parámetro | Tipo      | Obligatorio | Descripción                                        |
| --------- | --------- | ----------- | -------------------------------------------------- |
| `id`      | `integer` | Sí          | Identificador de la tarea que se quiere consultar. |

### Respuesta correcta

**Código:** `200 OK`

Devuelve la tarea correspondiente al `id` indicado.

### Errores posibles

**Código:** `404 Not Found`

Se produce cuando no existe una tarea con el identificador indicado.

```json
{
  "detail": "Task with id:{id} doesn't exist"
}
```

**Código:** `422 Unprocessable Entity`

Se produce cuando el parámetro `id` no es un número entero válido.

---

## `PUT /tasks/{id}`

Marca una tarea como completada.

### URL

```text
http://127.0.0.1:8000/tasks/{id}
```

Ejemplo:

```text
http://127.0.0.1:8000/tasks/2
```

### Parámetros

| Parámetro | Tipo      | Obligatorio | Descripción                                                     |
| --------- | --------- | ----------- | --------------------------------------------------------------- |
| `id`      | `integer` | Sí          | Identificador de la tarea que se quiere marcar como completada. |

### Respuesta correcta

**Código:** `200 OK`

Marca la tarea indicada como completada.

### Errores posibles

**Código:** `400 Bad Request`

Se produce cuando la tarea ya estaba marcada como completada.

```json
{
  "detail": "Task with id:{id} already finished"
}
```

**Código:** `422 Unprocessable Entity`

Se produce cuando el parámetro `id` no es un número entero válido.

---

## `DELETE /tasks/{id}`

Elimina una tarea según su identificador.

### URL

```text
http://127.0.0.1:8000/tasks/{id}
```

Ejemplo:

```text
http://127.0.0.1:8000/tasks/2
```

### Parámetros

| Parámetro | Tipo      | Obligatorio | Descripción                                       |
| --------- | --------- | ----------- | ------------------------------------------------- |
| `id`      | `integer` | Sí          | Identificador de la tarea que se quiere eliminar. |

### Respuesta correcta

**Código:** `200 OK`

Elimina la tarea correspondiente al `id` indicado.

### Errores posibles

**Código:** `404 Not Found`

Se produce cuando no existe una tarea con el identificador indicado.

```json
{
  "detail": "Task with id:{id} not found"
}
```

**Código:** `422 Unprocessable Entity`

Se produce cuando el parámetro `id` no es un número entero válido.
