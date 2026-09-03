1. GET - Consultar recurso
```bash
curl -i https://jsonplaceholder.typicode.com/posts/1
```

2. GET - Consultar recurso no existente
```bash
curl -i https://jsonplaceholder.typicode.com/posts/9999
```

3. POST - Crear un nuevo recurso
```bash
curl -i -X POST https://jsonplaceholder.typicode.com/posts \
-H "Content-Type: application/json" \
-d '{"title":"Mi primer post","body":"Este es un post creado mediante HTTP","userId":1}'
```

4. PUT - Remplazar recurso completo
```bash
curl -i -X PUT https://jsonplaceholder.typicode.com/posts/1 \
-H "Content-Type: application/json" \
-d '{"id":1,"title":"Post actualizado completamente","body":"Este contenido reemplaza al anterior","userId":1}'
```

5. PATCH - modificar solamente un campo
```bash
curl -i -X PATCH https://jsonplaceholder.typicode.com/posts/1 \
-H "Content-Type: application/json" \
-d '{"title":"Título modificado con PATCH"}'
```

6. DELETE - eliminar 
```bash
curl -i -X DELETE https://jsonplaceholder.typicode.com/posts/1
```