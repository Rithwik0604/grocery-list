from flask import Flask, render_template, flash, redirect, request, url_for
import grocery

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.args.get("action") == "got":
        item = request.args.get("item")
        category = request.args.get("category")
        # print('got request')
        grocery.got(item, category)
        # return redirect(url_for("home"))
    reply = grocery.read()
    if reply == 1:
        return render_template("home.html", result=True)
    return render_template("home.html", result=reply)


@app.template_filter()
def getCount(data):
    count = {"total": 0, "got": 0}
    for d in data:
        key = list(d.keys())[0]
        count[key] = len(d[key])
        count["total"] += len(d[key])

        # got items count
        for items in d[key]:
            if items["got"] == True:
                count["got"] += 1

    return count


@app.route("/uncheck/")
def uncheck():
    grocery.uncheckAll()
    return redirect(url_for("home"))


@app.route("/reset/")
def reset():
    grocery.reset()
    return redirect(url_for("home"))


@app.route("/add/", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        data = dict(request.form)
        data["got"] = False
        grocery.add(data)
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit/", methods=["POST", "GET"])
def edit():
    if request.args.get("action") == "edit":
        data = []
        data.append(request.args.get("item"))
        data.append(request.args.get("quantity"))
        data.append(request.args.get("replacement"))
        data.append(request.args.get("category"))
        data.append(request.args.get("got"))
        return render_template("edit.html", result=data)

    if request.method == "POST":
        data = dict(request.form)
        grocery.edit(data=data)
        return redirect(url_for("home"))

    return render_template("edit.html")


@app.route("/delete/")
def delete():
    item = request.args.get("item")
    category = request.args.get("category")
    grocery.delete(item, category)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
