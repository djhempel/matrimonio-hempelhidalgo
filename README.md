# Matrimonio Diego & Josefina · 30·10·2026

Invitación web. Cinco versiones que comparten diseño, imágenes y estilos;
lo único que cambia entre ellas es el formulario de confirmación.

## Qué link mandarle a cada invitado

| Invitado | URL | Diseño | Formulario |
|---|---|---|---|
| Comida, con pareja | https://djhempel.github.io/matrimonio-hempelhidalgo/comida-con-pareja/ | comida | `HeUdNsiieHcqByjm6` |
| Comida, sin pareja | https://djhempel.github.io/matrimonio-hempelhidalgo/comida-sin-pareja/ | comida | `VJx1YPKJxHdeKXPX8` |
| Comida, y su pareja a la fiesta | https://djhempel.github.io/matrimonio-hempelhidalgo/comida-pareja-fiesta/ | comida | `r22XT7neHURakDuq7` |
| Fiesta, con pareja | https://djhempel.github.io/matrimonio-hempelhidalgo/fiesta-con-pareja/ | fiesta | `UDZXr8xiBWirx5Kq7` |
| Fiesta, sin pareja | https://djhempel.github.io/matrimonio-hempelhidalgo/fiesta-sin-pareja/ | fiesta | `hq4uX651Cn22gwy86` |

En el caso de "comida y pareja a la fiesta" se usa el diseño de comida;
que la pareja llega a partir de las 22:00 se aclara dentro del formulario.

## Los dos diseños

- **comida** — Ceremonia (17:15) + Recepción en Arboleda de Chicureo.
- **fiesta** — Ceremonia (17:15) + Fiesta (22:00), con la ilustración de
  la pista de baile y su propio `.ics`.

## Cómo editar

Las carpetas de invitación **se generan, no se editan a mano**. Para cambiar
un horario, una dirección o un texto:

1. Editá la plantilla correspondiente en `_templates/comida.html` o
   `_templates/fiesta.html`
2. Corré `python3 build.py`
3. Commit y push

Para cambiar el diseño de las dos versiones a la vez, editá `styles.css`.
Para agregar o cambiar un formulario, editá el diccionario `INVITACIONES`
en `build.py` y volvé a correrlo.

## Estructura

```
_templates/       plantillas (una por diseño), con {{RSVP_URL}}
build.py          genera las 5 carpetas desde las plantillas
styles.css        estilos compartidos por todas las versiones
assets/           ilustraciones
wedding.ics       evento para las versiones de comida
wedding-fiesta.ics  evento para las versiones de fiesta
```
