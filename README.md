# Permiso Temporal Paseo de Mascotas
Automatización de la obtención del permiso temporal para pasear mascotas durante la Cuarentena en Chile por #Covid19.

# Aclaración
No es bajo ninguna circunstancia mi interés generar una herramienta que permita de manera alguna, la evasión de
responsabilidades de cuidarnos y cuidar a nuestros seres queridos. Esta pequeña y rudimentaria pieza de automatización
apunta a ser, por un lado, una mejora en la que interactuamos con los servicios del Estado, asi como también una crítica
al Gobierno en cómo ha manejado esta crisis, no actuando de forma audaz y temprana, más aún, confundiendo a la población.

Dicho esto, pienso que hacer la vida más sencilla a quienes lo estan pasando mal en este momento, y a quienes que por
diversas razones no pueden ingresar a Comisaría Virtual, me parece un deber. Espero que alguien continue
esto y podamos generar mejores interfaces entre el Estado y la Ciudadaniía.

# Instalación
- clonar repo: ```git clone https://github.com/crishernandezmaps/permiso_temporal_paseo_mascotas.git```
- cd en el repo: ```cd permiso_temporal_paseo_mascotas```
- instalar liberías: ```pip install -r requirements.txt```
- descargar webdriver (Chrome): ```https://chromedriver.chromium.org/downloads```
- agregar tus datos en ```your_data.py```

```
'name': 'Juan Juan Perez Perez',
'rut': 'xxxxxxxxx',
'serie_carnet': 'xxx.xxx.xxx',
'region': 'Metropolitana de Santiago',
'comuna': 'Providencia',
'direccion': 'Av El Pizzas 1312, Depto 014'
```

- comment: ```# from my_data import personal_data```
- uncomment: ```from your_data import personal_data```
- run: ```python permisos.py```

> Los datos anteriores como ejemplo

## Listado Comunas RM [Person el centralismo]
- Alhué
- Buin
- Calera de Tango
- Cerrillos
- Cerro Navia
- Colina
- Conchalí
- Curacaví
- El Bosque
- El Monte
- Estación Central
- Huechuraba
- Independencia
- Isla de Maipo
- La Cisterna
- La Florida
- La Granja
- La Pintana
- La Reina
- Lampa
- Las Condes
- Lo Barnechea
- Lo Espejo
- Lo Prado
- Macul
- Maipú
- María Pinto
- Melipilla
- Ñuñoa
- Padre Hurtado
- Paine
- Pedro Aguirre Cerda
- Peñaflor
- Peñalolén
- Pirque
- Providencia
- Pudahuel
- Puente Alto
- Quilicura
- Quinta Normal
- Recoleta
- Renca
- San Bernardo
- San Joaquín
- San José de Maipo
- San Miguel
- San Pedro
- San Ramón
- Santiago Centro
- Talagante
- Tiltil
- Vitacura

> Finalmente busca tu permiso en Downloads/Descargas
