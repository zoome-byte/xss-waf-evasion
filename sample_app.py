# sample_app.py
from flask import Flask, request, render_template_string
import re

app = Flask(__name__)

def waf_filter(input_text):
    blocked = ["<script>", "</script>", "onerror", "onload", "iframe", "svg"]
    for word in blocked:
        input_text = re.sub(word, "", input_text, flags=re.IGNORECASE)
    return input_text

@app.route("/", methods=["GET", "POST"])
def home():
    output = ""
    if request.method == "POST":
        user_input = request.form["input"]
        safe_input = waf_filter(user_input)
        output = f"Output: {safe_input}"
    return render_template_string('''
        <form method="post">
            Enter XSS payload: <input name="input">
            <input type="submit">
        </form>
        <p>{{output}}</p>
    ''', output=output)

if __name__ == "__main__":
    app.run(debug=True)
