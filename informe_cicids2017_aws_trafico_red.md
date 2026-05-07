---
title: "Gestión de anomalías en el tráfico de red aplicado al contexto de Amazon Web Services mediante análisis de datos"
lang: es
geometry: margin=2.5cm
fontsize: 11pt
---

# Carátula

**UNIVERSIDAD [COLOCAR NOMBRE]**  
**FACULTAD DE INGENIERÍA**  
**CURSO:** Análisis de Datos

**Título:**  
**Gestión de anomalías en el tráfico de red aplicado al contexto de Amazon Web Services mediante análisis de datos**

**Trabajo Final**

**Integrantes:**
- [Nombre 1]
- [Nombre 2]
- [Nombre 3]

**Grupo:** [Grupo]  
**Instructor:** [Nombre del docente]  
**Año:** 2026

\newpage

# Índice

1. Introducción
2. Descripción de la empresa
3. Problema de la empresa
4. Objetivos del trabajo
5. Topología de red de la empresa
6. Definición de conceptos clave
7. Metodología de análisis de datos
8. Descripción de los datos
9. Análisis de datos
10. Discusión
11. Conclusiones y recomendaciones
12. Referencias bibliográficas
13. Anexos

\newpage

# 1. Introducción

El análisis de tráfico de red es una actividad esencial para comprender el comportamiento de los sistemas digitales modernos. En entornos empresariales y cloud, millones de solicitudes, paquetes y flujos circulan entre usuarios, aplicaciones, bases de datos, servicios de autenticación, sistemas de almacenamiento y componentes de seguridad. Esta actividad puede ser normal, pero también puede incluir intentos de ataque, exploración de servicios, abuso de recursos o patrones de comunicación anómalos.

La ciberseguridad y la disponibilidad son dimensiones críticas para las plataformas de computación en la nube. En una infraestructura distribuida, un incremento inesperado en paquetes por segundo, bytes por segundo o duración de flujos puede afectar el rendimiento de aplicaciones, elevar la latencia y deteriorar la experiencia del usuario. Por ello, el análisis de datos permite pasar de una revisión reactiva a una evaluación basada en evidencias, visualizaciones y métricas estadísticas.

> **Aclaración obligatoria:** el dataset utilizado no pertenece a AWS ni corresponde a información interna de la empresa. Se utiliza el dataset público CICIDS2017 como base real de tráfico de red para analizar patrones de tráfico normal y anómalo. El caso se aplica al contexto de Amazon Web Services porque AWS administra infraestructura cloud distribuida donde la disponibilidad, la latencia, la seguridad y el rendimiento de red son elementos críticos.

# 2. Descripción de la empresa

Amazon Web Services (AWS) es una empresa perteneciente a Amazon que ofrece servicios de computación en la nube a organizaciones de diferentes tamaños y sectores. Su infraestructura global permite desplegar aplicaciones, almacenar información, ejecutar procesamiento, administrar redes y proteger cargas de trabajo.

Entre sus servicios se encuentran Amazon EC2, Amazon S3, Amazon RDS, Amazon CloudFront, Amazon Route 53, AWS Lambda, Amazon VPC, Elastic Load Balancing y AWS WAF. En este tipo de organización, la seguridad, disponibilidad y rendimiento son aspectos fundamentales porque una interrupción o degradación puede afectar servicios críticos de clientes.

# 3. Problema de la empresa

En una empresa cloud como AWS, el tráfico anómalo puede generar saturación de servicios, alta latencia, pérdida de disponibilidad, riesgos de seguridad, ataques DDoS, escaneos de puertos, intentos de fuerza bruta, ataques web y deterioro de la experiencia del usuario.

El dataset analizado no es interno de AWS, sino un dataset público de tráfico de red utilizado para estudiar estos fenómenos. El problema analítico consiste en identificar patrones de tráfico normal y malicioso a partir de variables como duración de flujo, paquetes, bytes, puertos y velocidad de tráfico.

# 4. Objetivos del trabajo

## 4.1 Objetivo general

Analizar el tráfico de red normal y anómalo del dataset CICIDS2017 mediante técnicas de análisis de datos, aplicando los hallazgos al contexto de una infraestructura cloud como Amazon Web Services, con la finalidad de identificar patrones de duración de flujo, paquetes, bytes, puertos, protocolos y tipos de tráfico malicioso.

## 4.2 Objetivos específicos

1. Identificar la distribución del tráfico benigno y malicioso dentro del dataset.
2. Analizar la duración promedio de los flujos de red.
3. Evaluar el comportamiento de variables como paquetes, bytes, puertos y velocidad de tráfico.
4. Detectar valores atípicos en variables numéricas relevantes.
5. Visualizar patrones de tráfico mediante gráficos estadísticos.
6. Relacionar los resultados con posibles riesgos para una infraestructura cloud como AWS.
7. Proponer recomendaciones para mejorar el monitoreo, seguridad y rendimiento de red.

# 5. Topología de red de la empresa

Usuario final  
↓  
Route 53  
↓  
CloudFront  
↓  
Elastic Load Balancing  
↓  
EC2 / Lambda / API Gateway  
↓  
RDS / S3  
↓  
Monitoreo con CloudWatch y protección con AWS WAF / Shield

[Insertar imagen de topología de red AWS aquí]

# 6. Definición de conceptos clave

- **Tráfico de red:** comunicaciones entre dispositivos, servidores, aplicaciones y usuarios.
- **Flujo de red:** registro agregado de una comunicación entre origen y destino.
- **Dataset CICIDS2017:** conjunto público de evaluación de detección de intrusiones con tráfico benigno y malicioso.
- **Tráfico benigno:** actividad considerada normal.
- **Tráfico malicioso:** actividad asociada a ataques o anomalías.
- **DDoS:** ataque distribuido de denegación de servicio.
- **DoS:** ataque de denegación de servicio.
- **PortScan:** escaneo de puertos abiertos.
- **Botnet:** red de equipos comprometidos.
- **Fuerza bruta:** intentos repetitivos de adivinar credenciales.
- **Ataque web:** explotación o abuso de aplicaciones web.
- **Latencia:** demora en la comunicación.
- **Paquetes:** unidades de datos transmitidas.
- **Bytes:** cantidad de información transferida.
- **Puerto de destino:** identificador lógico del servicio receptor.
- **Análisis de datos:** inspección, limpieza y transformación de datos para obtener conclusiones.
- **Limpieza de datos:** corrección de nulos, duplicados e inconsistencias.
- **Visualización de datos:** representación gráfica de información.
- **Estadística descriptiva:** medidas de tendencia central, dispersión y distribución.
- **Valor atípico:** observación extrema frente al comportamiento general.

# 7. Metodología de análisis de datos

La metodología incluye recolección del dataset, carga en Python/Google Colab, inspección inicial, limpieza de datos, creación de variables derivadas, análisis descriptivo, visualización exploratoria, análisis diagnóstico, exportación para Power BI y elaboración de conclusiones.

# 8. Descripción de los datos

| Elemento | Descripción |
|---|---|
| Nombre | CICIDS2017 – Intrusion Detection Evaluation Dataset |
| Fuente | Canadian Institute for Cybersecurity, University of New Brunswick |
| Formato | CSV |
| Tipo de datos | Flujos de tráfico de red |
| Variable objetivo | `Label` |
| Variables relevantes | `Flow Duration`, `Destination Port`, `Flow Bytes/s`, `Flow Packets/s`, `Total Fwd Packets`, `Total Backward Packets` |
| Contenido | Tráfico benigno y tráfico malicioso |

| Columna | Descripción |
|---|---|
| `Destination Port` | Puerto de destino asociado al servicio receptor. |
| `Flow Duration` | Duración del flujo de red. |
| `Total Fwd Packets` | Total de paquetes hacia adelante. |
| `Total Backward Packets` | Total de paquetes de retorno. |
| `Total Length of Fwd Packets` | Longitud total de paquetes hacia adelante. |
| `Total Length of Bwd Packets` | Longitud total de paquetes de retorno. |
| `Flow Bytes/s` | Velocidad del flujo en bytes por segundo. |
| `Flow Packets/s` | Velocidad del flujo en paquetes por segundo. |
| `Flow IAT Mean` | Promedio del tiempo entre llegadas. |
| `Label` | Etiqueta de tráfico benigno o ataque. |

# 9. Análisis de datos

El notebook `analisis_cicids2017_aws_trafico_red.ipynb` implementa carga, inspección, limpieza, variables derivadas, estadística descriptiva, visualizaciones, outliers y exportación. La limpieza aplica `df.columns = df.columns.str.strip()`, reemplaza infinitos por `NaN`, convierte columnas numéricas, trata nulos, elimina duplicados y exporta `cicids2017_clean.csv`.

## 9.1 Variables derivadas

- `Traffic Type`: `BENIGN` se clasifica como `Benigno`; el resto como `Malicioso`.
- `Attack Category`: agrupa etiquetas en Benigno, DDoS, DoS, Escaneo de puertos, Botnet, Fuerza bruta, Ataque web, Infiltración u Otros.
- `Service Context`: relaciona puertos con HTTP/Web, HTTPS/Web seguro, DNS, SSH/Administración, FTP, SMTP, RDP u Otros servicios.

## 9.2 Gráficos del análisis

![Distribución de etiquetas](figures/01_distribucion_labels.png)

![Tráfico benigno vs malicioso](figures/02_benigno_vs_malicioso.png)

![Categoría de ataque](figures/03_attack_category.png)

![Top destination ports](figures/04_top_destination_ports.png)

![Histograma Flow Duration](figures/05_hist_flow_duration.png)

![Boxplot Flow Duration por ataque](figures/06_boxplot_flow_duration_attack.png)

![Histograma Flow Bytes/s](figures/07_hist_flow_bytes.png)

![Boxplot Flow Packets/s por ataque](figures/08_boxplot_flow_packets_attack.png)

![Service Context](figures/09_service_context.png)

![Heatmap ataque servicio](figures/10_heatmap_attack_service.png)

![Scatter Flow Bytes y Flow Packets](figures/11_scatter_flowbytes_flowpackets.png)

![Promedio duración por ataque](figures/12_promedio_duration_attack.png)

## 9.3 Interpretación aplicada a AWS

Los puertos web pueden relacionarse con CloudFront, Elastic Load Balancing y API Gateway; DNS con Route 53; SSH con administración de EC2; y FTP/SMTP/RDP con servicios expuestos o configuraciones de red que requieren revisión. Picos en `Flow Bytes/s` y `Flow Packets/s` podrían indicar presión sobre recursos, necesidad de mitigación DDoS o reglas de AWS WAF.

# 10. Discusión

## 10.1 Comparación de resultados

El análisis compara tráfico benigno y malicioso usando etiquetas, categorías de ataque, métricas de duración, velocidad y puertos de destino. No todos los ataques se comportan igual: algunos generan gran volumen, otros se concentran en servicios específicos y otros producen valores atípicos.

## 10.2 Implicaciones de los hallazgos

En AWS, los hallazgos pueden orientar reglas de monitoreo con CloudWatch, protección con AWS WAF, mitigación con AWS Shield, revisión de grupos de seguridad, dashboards en Power BI y modelos de detección de anomalías.

## 10.3 Limitaciones del estudio

- El dataset no pertenece a AWS.
- El análisis es aplicado al contexto AWS.
- El dataset representa tráfico capturado en un entorno específico.
- Algunos datos pueden requerir limpieza por valores infinitos o faltantes.
- El análisis descriptivo no reemplaza un sistema real de monitoreo.

# 11. Conclusiones y recomendaciones

## 11.1 Conclusiones

1. El dataset permitió identificar diferencias entre tráfico benigno y malicioso.
2. Las categorías de ataque presentan comportamientos distintos en duración, paquetes y bytes.
3. Los puertos de destino ayudan a relacionar tráfico con servicios expuestos.
4. `Flow Bytes/s` y `Flow Packets/s` ayudan a detectar tráfico de alta intensidad.
5. En AWS, estos patrones serían útiles para monitoreo, seguridad y prevención.

## 11.2 Recomendaciones

1. Implementar monitoreo continuo de tráfico.
2. Configurar alertas para picos de `Flow Packets/s` y `Flow Bytes/s`.
3. Fortalecer mitigación DDoS con AWS Shield.
4. Revisar exposición de puertos críticos.
5. Usar AWS WAF para proteger aplicaciones web.
6. Usar logs y métricas de CloudWatch.
7. Aplicar modelos de detección de anomalías.
8. Capacitar al equipo técnico en interpretación de métricas de red.

# 12. Referencias bibliográficas

Amazon Web Services. (s. f.). *What is AWS?* https://aws.amazon.com/what-is-aws/

Amazon Web Services. (s. f.). *AWS Shield*. https://aws.amazon.com/shield/

Amazon Web Services. (s. f.). *AWS WAF*. https://aws.amazon.com/waf/

Amazon Web Services. (s. f.). *Elastic Load Balancing*. https://aws.amazon.com/elasticloadbalancing/

Amazon Web Services. (s. f.). *Amazon CloudFront*. https://aws.amazon.com/cloudfront/

Canadian Institute for Cybersecurity. (s. f.). *Intrusion Detection Evaluation Dataset (CICIDS2017)*. University of New Brunswick. https://www.unb.ca/cic/datasets/ids-2017.html

McKinney, W. (2010). Data structures for statistical computing in Python. *Proceedings of the 9th Python in Science Conference*, 56–61.

Microsoft. (s. f.). *Power BI documentation*. https://learn.microsoft.com/power-bi/

Sharafaldin, I., Lashkari, A. H., & Ghorbani, A. A. (2018). Toward generating a new intrusion detection dataset and intrusion traffic characterization. *Proceedings of the 4th International Conference on Information Systems Security and Privacy (ICISSP)*, 108–116.

# 13. Anexos

## Anexo A. Archivos generados

- `analisis_cicids2017_aws_trafico_red.ipynb`
- `informe_cicids2017_aws_trafico_red.md`
- `informe_cicids2017_aws_trafico_red.pdf`
- `powerbi_readme.md`
- `powerbi_medidas_dax.txt`
- `README.md`
- `figures/`
- `powerbi/`

## Anexo B. Reproducción

Descargue CICIDS2017, configure `DATA_PATH` en el notebook y ejecute las celdas de carga, limpieza, visualización y exportación.

## Anexo C. Generación local de binarios

Por política del repositorio, los archivos binarios generados no se versionan. El PDF `informe_cicids2017_aws_trafico_red.pdf` y las imágenes `figures/*.png` se recrean localmente ejecutando el notebook con el dataset CICIDS2017 real o, para obtener entregables estructurales antes de cargar los datos, con el comando:

```bash
python scripts/generate_structural_assets.py
```
