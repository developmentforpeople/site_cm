## Site ComoMejorar

Site ComoMejorar.info

# Primeros pasos

## Settings

- http://comomejorar.localhost:8001/app/system-settings/System%20Settings
- Definir parámetros del sitio: idioma principal, formatos, domingo-lunes, etc.
- Habilitar site tracking

## Idiomas

- Deshabilitar los no necesarios: http://comomejorar.localhost:8001/app/language
- Vaciar caché
- Jerarquía de asignación en **translate.py**: __def get_language(__
- Deshabilitar los que no se necesitan. Añadiendo "**?_lang=es**" se forzará el idioma "es".

## Deshabilitar webforms no necesarios

- http://comomejorar.localhost:8001/app/web-form

## Revisar los files en /frappe/www/ & /erpnext/www/ para copiarlos o redireccionarlos
- search.html
- sitemap.xml
- third_party_apps
- contact
- complete_signup
- about
- ...

## comprobar sitemap.xml

## Workspace

- Añadir workspace y asignarlo al módulo del site

## Traducciones

- Añadir "Translations" a fixtures

## Home page / en el Rol "Portal User"

## Index search

- bench build-search-index
- Sólo se indexa el contenido que esté dentro de la clase "page_content"

## Otro search method para usuarios del ERP
- Hacer comprobaciones pero yo lo caparía
- Usa frappe/frappe/www/search.py
- Se guarda en la tabla "__global_search" y se busca así (publicado=1):

```sql
SELECT `doctype`, `name`, `content`, `title`, `route`
FROM `__global_search`
WHERE `published` = 1 AND  MATCH(`content`) AGAINST ('+ejemplo*' IN BOOLEAN MODE)
LIMIT 1 OFFSET 21;
```

#### License

agpl-3.0
