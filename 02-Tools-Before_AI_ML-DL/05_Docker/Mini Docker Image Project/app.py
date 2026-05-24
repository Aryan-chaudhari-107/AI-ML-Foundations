from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Table Generator</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
            margin-top: 50px;
        }
        input, button {
            padding: 10px;
            font-size: 16px;
        }
        table {
            margin: auto;
            margin-top: 20px;
            border-collapse: collapse;
        }
        td, th {
            border: 1px solid black;
            padding: 10px 20px;
        }
    </style>
</head>
<body>

    <h1>Multiplication Table Generator</h1>

    <form method="POST">
        <input type="number" name="number" placeholder="Enter a number" required>
        <button type="submit">Generate Table</button>
    </form>

    {% if table %}
    <table>
        <tr>
            <th>Expression</th>
            <th>Result</th>
        </tr>

        {% for row in table %}
        <tr>
            <td>{{ row[0] }}</td>
            <td>{{ row[1] }}</td>
        </tr>
        {% endfor %}
    </table>
    {% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    table = []

    if request.method == "POST":
        number = int(request.form["number"])

        for i in range(1, 11):
            table.append((f"{number} x {i}", number * i))

    return render_template_string(HTML_PAGE, table=table)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)