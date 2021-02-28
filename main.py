from flask import Flask, render_template, request, redirect, url_for, flash
from config import app
from models import Todos, get_all
import uuid
import sqlite3


@app.route("/", methods=["GET", "POST"])
@app.route("/todo.html/", methods=["GET", "POST"])
def all_tasks():
    if request.method == "POST":
        with sqlite3.connect("todo.db") as conn:
            task_id = uuid.uuid4()
            task_id = str(task_id)
            title = request.form["title"]
            description = request.form["description"]
            c = conn.cursor()
            c.execute("INSERT INTO todo VALUES (?, ?, ?)", (task_id, title, description))
            conn.commit()

            return redirect("/")
    else:
        with sqlite3.connect("todo.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM todo")
            tasks = c.fetchall()
            return render_template("todo.html", tasks=tasks)


@app.route("/delete/<string:task_id>", methods=["GET"])
def delete_task(task_id):
    with sqlite3.connect("todo.db") as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM todo")
        tasks = c.fetchall()
        c.execute(
            "DELETE from todo WHERE task_id = :task_id",
            {"task_id": task_id},
        )
        conn.commit()
        return redirect("/")


@app.route("/update/<task_id>/", methods=["GET", "POST"])
def update_task(task_id):
    print("def task_id ===>", task_id)
    if request.method == "POST":
        with sqlite3.connect("todo.db") as conn:
            title = request.form["title"]
            description = request.form["description"]
            c = conn.cursor()
            print("with task_id ====>", task_id)
            print("with title ====>", title)
            print("with description ====>", description)
            try:
                c.execute(
                    """UPDATE todo SET title = :title, description = :description
                        WHERE task_id = :task_id""",
                    {"title": title, "description": description, "task_id": task_id},
                )
                conn.commit()
                return redirect("/")
            except Exception as e:
                print(f"Exception raised: {e}")

    else:
        with sqlite3.connect("todo.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM todo")
            tasks = c.fetchall()
        return render_template("todo_id.html/", tasks=tasks, task_id=task_id)


if __name__ == "__main__":
    app.run(debug=True)