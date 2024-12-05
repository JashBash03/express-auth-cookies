const dotenv = require('dotenv');
dotenv.config();
const SECRET = process.env.SESSION_SECRET;

const express = require('express');
const session = require('express-session');
const app = express();
const port = 3000;


app.use(express.static('public'));

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Configuración de express-session
app.use(session({
    secret: SECRET, // Secreto para firmar la sesión
    resave: false, // No volver a guardar la sesión si no ha cambiado
    saveUninitialized: true, // Guardar sesiones sin inicializar
    cookie: { secure: false } // Cambiar a true si usas HTTPS
}));

app.use((req, res, next) => {
    console.log(req.method, req.path);
    next();
});

const users = require('./routes/users');
app.use("/api/", users);

app.listen(port, () => {
    console.log(`Server is listening at http://localhost:${port}`);
    });