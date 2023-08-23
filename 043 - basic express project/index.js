const express = require('express');
const sqlite3 = require('sqlite3').verbose();

const repository = (function() {
    const data = [];
    const base = new sqlite3.Database('base.db');
    base.serialize(() => {
        base.run('CREATE TABLE IF NOT EXISTS todos (id, task)');
        base.each('SELECT id, task FROM todos', (_, row) => {
            data.push({id: row.id, task: row.task});
        });
    });

    function list() {
        return data;
    }

    function create(task) {
        const newTask = {id: _nextId(), task};
        data.push(newTask);
        base.prepare("INSERT INTO todos (id, task) VALUES (?, ?)")
            .run(newTask.id, newTask.task)
            .finalize();
    }

    function _nextId() {
        let max = 0;
        data.forEach(el => { 
            if (el.id > max) {
                max = el.id
            }
        });
        return max + 1;
    }

    function remove(id) {
        for (let index = 0; index < data.length; index++) {
            if (data[index].id === id) {
                data.splice(index, 1);
                break;
            }
        }
        base.prepare("DELETE FROM todos WHERE id = ?")
            .run(id)
            .finalize();
    }

    return { list, create, remove }
})();

const server = express();
const port = 3000;

server.use(express.json());
server.use(express.urlencoded({extended: true}));
server.set("view engine", "ejs");
server.set('views', __dirname);

server.get("/", (req, res) => {
    res.render("index", { data: repository.list() });
});

server.post("/create", (req, res) => {
    repository.create(req.body.task);
    res.redirect('/');
});

server.get("/done/:id", (req, res) => {
    repository.remove(parseInt(req.params.id));
    res.redirect('/');
});

server.listen(port, () => {
    console.log(`Listening on port ${port}`);
});
