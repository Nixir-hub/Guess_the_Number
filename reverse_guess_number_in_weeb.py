from flask import Flask, request

app = Flask(__name__)

@app.route("/guess", methods=["GET", "POST"])
def reverse_guess():
    lower = request.form.get("minimal", 0, type=int)
    higher = request.form.get("maximum", 1000, type=int)
    guess = request.form.get("guess", type=int)
    answer = request.form.get("option")

    if guess is not None:
        if answer == "lower":
            lower = guess
        elif answer == "higher":
            higher = guess
        elif answer == "ok":
            return "I Win"
    guess = (higher - lower + 1)//2 + lower

    form = f"""<form method="POST">
            <input Type='hidden' value='{lower}' name="minimal">
            <input Type='hidden' value='{higher}' name="maximal">
            <input Type'text' value='{guess}' name="guess">
                <select name="option">
                    <option value="lower">To small</option>
                    <option value="higher">To big</option>
                    <option value="ok">That right!</option>
                </select>
            <input Type="submit">
     </form>
     """
    return form

if __name__ == '__main__':
    app.run()
