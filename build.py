#!/usr/bin/env python3
"""Genera las 5 invitaciones a partir de las dos plantillas de _templates/.

Cada invitacion usa el mismo diseño que su plantilla y solo cambia el link
del formulario de RSVP. Para modificar el contenido (horarios, direcciones,
textos) hay que editar la plantilla y volver a correr este script:

    python3 build.py
"""

from pathlib import Path

RAIZ = Path(__file__).parent

# carpeta -> (plantilla, formulario de RSVP)
INVITACIONES = {
    "comida-con-pareja":    ("comida", "https://forms.gle/HeUdNsiieHcqByjm6"),
    "comida-sin-pareja":    ("comida", "https://forms.gle/VJx1YPKJxHdeKXPX8"),
    "comida-pareja-fiesta": ("comida", "https://forms.gle/r22XT7neHURakDuq7"),
    "fiesta-con-pareja":    ("fiesta", "https://forms.gle/UDZXr8xiBWirx5Kq7"),
    "fiesta-sin-pareja":    ("fiesta", "https://forms.gle/hq4uX651Cn22gwy86"),
}


def main():
    plantillas = {
        nombre: (RAIZ / "_templates" / f"{nombre}.html").read_text(encoding="utf-8")
        for nombre in {p for p, _ in INVITACIONES.values()}
    }

    for carpeta, (plantilla, rsvp) in INVITACIONES.items():
        html = plantillas[plantilla]
        if html.count("{{RSVP_URL}}") != 1:
            raise SystemExit(f"_templates/{plantilla}.html debe tener exactamente un {{{{RSVP_URL}}}}")

        destino = RAIZ / carpeta
        destino.mkdir(exist_ok=True)
        (destino / "index.html").write_text(html.replace("{{RSVP_URL}}", rsvp), encoding="utf-8")
        print(f"{carpeta}/index.html  <-  {plantilla}  ({rsvp})")


if __name__ == "__main__":
    main()
