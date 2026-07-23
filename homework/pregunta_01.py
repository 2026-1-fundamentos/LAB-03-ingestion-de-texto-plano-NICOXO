"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


import pandas as pd


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.
    """
    path = "files/input/clusters_report.txt"

    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()


    columns = [
        "cluster",
        "cantidad_de_palabras_clave",
        "porcentaje_de_palabras_clave",
        "principales_palabras_clave",
    ]

    data = []
    current_row = None

    
    for line in lines[4:]:
        # Si la línea está vacía o solo contiene espacios/separadores, continuamos
        line_str = line.strip()
        if not line_str or line_str.startswith("-"):
            continue

       
        parts = line.split()
        if parts[0].isdigit():
            
            if current_row is not None:
                data.append(current_row)

            
            cluster = int(parts[0])
            cantidad = int(parts[1])
            
            
            porcentaje = float(parts[2].replace(",", ".").replace("%", ""))

            
            idx_percent = line.find("%")
            if idx_percent != -1:
                keywords_start = line[idx_percent + 1:].strip()
            else:
                keywords_start = " ".join(parts[3:])

            current_row = [cluster, cantidad, porcentaje, keywords_start]
        else:
           
            if current_row is not None:
                current_row[3] += " " + line_str

    
    if current_row is not None:
        data.append(current_row)

    
    df = pd.DataFrame(data, columns=columns)

    
    def clean_keywords(text):
        
        text = " ".join(text.split())
        # Si termina en punto, se elimina
        if text.endswith("."):
            text = text[:-1]
       
        words = [w.strip() for w in text.split(",")]
        return ", ".join(words)

    df["principales_palabras_clave"] = df["principales_palabras_clave"].apply(clean_keywords)

    return df