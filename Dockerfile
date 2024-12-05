# Usa una imagen base oficial de Node.js
FROM node:18

# Crea un directorio de trabajo
WORKDIR /usr/src/app

# Copi el archivp package.json
COPY package.json ./

# Instalar las dependencias
RUN npm install

# Copia el resto del código de la aplicación
COPY . . 

# Expone el puerto en el que la aplicación se ejecutará
EXPOSE 3000

# Define el comando para ejecutar la aplicación
CMD [ "node", "server.js" ]

# Crear la imagen
# docker build -t node-app.

# Consultar images
# docker images

# Ejecutar la imagen
# docker run -p 3000:3000 node-app

# Leer contenedores en funcionamiento
# docker ps
# Leer los contenedores en funcionamiento y parados
# docker ps -a

# Ver IP-Adress y mas cosas
# docker inspect container-ID

# Parar servidor
# docker stop container-ID

# Borrar servidor
# docker rm container-ID