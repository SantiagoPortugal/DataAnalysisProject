# Guía para construir el dashboard en Power BI

Este documento explica cómo construir un dashboard de análisis de anomalías de tráfico de red con los CSV exportados por el notebook `analisis_cicids2017_aws_trafico_red.ipynb`.

> Los archivos de `powerbi/` deben regenerarse ejecutando el notebook con el dataset público CICIDS2017. No se incluyen datos falsos ni datos internos de AWS.

## Archivos a importar

- `powerbi/cicids2017_clean.csv`
- `powerbi/summary_by_label.csv`
- `powerbi/summary_by_attack_category.csv`
- `powerbi/summary_by_service_context.csv`
- `powerbi/summary_by_traffic_type.csv`
- `powerbi/resumen_estadistico.csv`

## Power Query

1. Verifique que `Flow Duration`, `Flow Bytes/s`, `Flow Packets/s`, `Total Fwd Packets`, `Total Backward Packets` y `Destination Port` sean numéricos.
2. Verifique que `Label`, `Traffic Type`, `Attack Category` y `Service Context` sean texto.
3. Mantenga `cicids2017_clean` como tabla principal.

## Página 1: Resumen General

- Tarjeta: total de registros.
- Tarjeta: porcentaje de tráfico malicioso.
- Tarjeta: total de ataques.
- Tarjeta: promedio de Flow Duration.
- Gráfico de barras: Traffic Type.
- Gráfico de barras: Attack Category.
- Segmentadores: Label, Attack Category, Service Context.

## Página 2: Análisis de Ataques

- Barras: registros por Label.
- Barras: registros por Attack Category.
- Matriz: Attack Category vs Service Context.
- Barras: promedio de Flow Duration por Attack Category.
- Barras: promedio de Flow Bytes/s por Attack Category.

## Página 3: Puertos y servicios

- Top 10 Destination Port.
- Barras por Service Context.
- Matriz: Service Context vs Traffic Type.
- Barras: Flow Packets/s promedio por Service Context.

## Página 4: Rendimiento de red

- Scatter: Flow Bytes/s vs Flow Packets/s.
- Histograma: Flow Duration.
- Barras: promedio de Total Fwd Packets por Attack Category.
- Barras: promedio de Total Backward Packets por Attack Category.

## Página 5: Eventos críticos

- Tabla filtrada de registros maliciosos.
- Tabla de Top ataques por Flow Bytes/s.
- Tabla de Top ataques por Flow Packets/s.
- Segmentadores por Attack Category y Service Context.

## Estilo

Use diseño sobrio, títulos claros y notas que indiquen que CICIDS2017 no es un dataset interno de AWS.
