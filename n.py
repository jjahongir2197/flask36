from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

books = []

@app.route("/", methods=["GET", "POST"])
def library():

    if request.method == "POST":

        title = request.form["title"]
        author = request.form["author"]

        books.append({
            "title": title,
            "author": author
        })

        return redirect("/")

    return render_template(
        "index.html",
        books=books
    )

@app.route("/delete/<int:id>")
def delete(id):

    books.pop(id)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
