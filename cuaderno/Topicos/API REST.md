
No meter el verbo en la URI:
GET /getsongs          X
POST /postsongs      X
GET /songs
POST /songs


/songs                    -->     Coleccion completa
/songs/5                 -->     Elemento especifico dentro de la coleccion
/artists/12/songs   .-->     Buena practica anidamiento (no superar 3 niveles)

Convenciones URI's
* Sustantivo en plural    -->  /songs
* No mayusculas           -->  /songs
* Usar kebab-case        --> /top-tracks
* Sin verbos
* Sin diagonal al final
* Versionado de la API en la URI     -->   api/v1/songs

Query params
- MOdifica como se devuelve una coleccion
Path param
- Idetifica CUAL recurso