from flask import Flask, request

app = Flask(__name__)

@app.route("/guess", methods=["GET", "POST"])
def reverse_guess():
    lower = request.form.get("minimal", 0, type=int)
    higher = request.form.get("maximum", 1000, type=int)
    guess = request.form.get("guess")
    answer = request.form.get("option", type=int)

    if guess is not None:
        if answer == "minimal":
            minimal = guess
        elif answer == "maximum":
            maximum = guess
    guess = (higher - lower)//2 + lower

    form = f"""<form method="POST">
            <input Type='hidden' value='{lower}' name="minimal">
            <input Type='hidden' value='{higher}' name="maximal">
            <input Type'text' value='{guess}' name="guess">
                <select name="options">
                    <option value="maximum">To big</option>
                    <option value="minimal">To small</option>
                    <option value="ok">That right!</option>
                </select>
            <input Type="submit">
     </form>
     """
    return form

if __name__ == '__main__':
    app.run()
