from flask import Flask, request

app = Flask(__name__)

@app.route("/guess", methods=["GET", "POST"])
def reverse_guess():
    minimal = request.form.get("minimal", 0)
    maximum = request.form.get("maximum", 1000)
    guess = request.form.get("guess")


    guess = (maximum - minimal)/2 + minimal
    form = f"""<form method="POST>
            <input Type='hidden' value='{minimal}' name="minimal">
            <input Type='hidden' value='{maximum}' name="maximum">
            <input Type'text' value='{guess}' name="guess">
                <select name"options">
                    <oprions value="maximum">To big</option>
                    <oprions value="minimal">To small</option>
                    <oprions value="ok">That right!</option>
                </select>
            <input Type="submit>
     </form>
     """
    return form

if __name__ == '__main__':
    app.run()