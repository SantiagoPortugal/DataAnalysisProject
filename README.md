# Proyecto de Análisis de Datos: CICIDS2017 aplicado al contexto de AWS

Este repositorio contiene un proyecto académico universitario sobre **gestión de anomalías en el tráfico de red aplicado al contexto de Amazon Web Services mediante análisis de datos**.

## Aclaración importante

El dataset utilizado no pertenece a AWS ni corresponde a información interna de la empresa. Se utiliza el dataset público **CICIDS2017 – Intrusion Detection Evaluation Dataset** como base real de tráfico de red para analizar patrones de tráfico normal y anómalo. El caso se aplica al contexto de Amazon Web Services porque AWS administra infraestructura cloud distribuida donde la disponibilidad, la latencia, la seguridad y el rendimiento de red son elementos críticos.

## Dataset

- **Nombre:** CICIDS2017 – Intrusion Detection Evaluation Dataset.
- **Fuente oficial:** Canadian Institute for Cybersecurity, University of New Brunswick.
- **Página oficial:** https://www.unb.ca/cic/datasets/ids-2017.html
- **Alternativa Kaggle:** https://www.kaggle.com/datasets/chethuhn/network-intrusion-dataset

No se descarga automáticamente el dataset porque la versión de Kaggle puede requerir credenciales. Descargue el dataset manualmente y configure la ruta `DATA_PATH` en el notebook.

## Estructura del proyecto

```text
project/
├── analisis_cicids2017_aws_trafico_red.ipynb
├── informe_cicids2017_aws_trafico_red.md
├── informe_cicids2017_aws_trafico_red.pdf
├── powerbi_readme.md
├── powerbi_medidas_dax.txt
├── README.md
├── figures/
└── powerbi/
```

## Cómo ejecutar el análisis

1. Descargue CICIDS2017 desde la fuente oficial o desde Kaggle.
2. Suba el archivo CSV a Google Colab, móntelo desde Google Drive o colóquelo en una carpeta local.
3. Abra `analisis_cicids2017_aws_trafico_red.ipynb`.
4. Configure `DATA_PATH` con la ruta del archivo CSV o de la carpeta con varios CSV.
5. Ejecute las celdas del notebook en orden.
6. Verifique que se generen los gráficos en `figures/` y los CSV en `powerbi/`.
7. Use `powerbi_readme.md` y `powerbi_medidas_dax.txt` para construir el dashboard en Power BI.

## Variables derivadas

- `Traffic Type`: Benigno o Malicioso.
- `Attack Category`: Benigno, DDoS, DoS, Escaneo de puertos, Botnet, Fuerza bruta, Ataque web, Infiltración u Otros.
- `Service Context`: HTTP/Web, HTTPS/Web seguro, DNS, SSH/Administración, FTP, SMTP, RDP u Otros servicios.

## Nota sobre archivos generados sin dataset local

Para no crear datos artificiales, los CSV incluidos en `powerbi/` son plantillas estructurales con encabezados cuando el dataset real no está disponible en el repositorio. Al ejecutar el notebook con CICIDS2017, estos archivos serán reemplazados por datos reales procesados desde el dataset público.

## Política de archivos binarios

Este repositorio no versiona archivos binarios generados, como `figures/*.png` o `informe_cicids2017_aws_trafico_red.pdf`. Esto evita rechazos en plataformas que no admiten binarios o repositorios con límites estrictos de tamaño.

Para recrear localmente los marcadores estructurales de figuras y el PDF del informe antes de ejecutar el dataset real, use:

```bash
python scripts/generate_structural_assets.py
```

Cuando ejecute el notebook con CICIDS2017, los gráficos reales se generarán nuevamente en `figures/` y los CSV reales se exportarán en `powerbi/`.
