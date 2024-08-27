# Import libraries
from flask import Flask, redirect, request, render_template, url_for

# Instantiate Flask functionality
app = Flask("My custom app")

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route("/", methods=["GET"])
def get_transactions():
    return render_template("transactions.html", transactions=transactions)

# Create operation
@app.route("/add", methods=["POST", "GET"])
def add_transaction():
    if request.method == "GET":
        return render_template("form.html")
    if request.method == "POST":
        transaction = {
              'id': len(transactions)+1, 
              'date': request.form['date'], 
              'amount': float(request.form['amount'])
             }
        transactions.append(transaction)
        return redirect(url_for("get_transactions")) ## Means to call the get_transaction() here - to add new transanctions to the transcactions.html

# Update operation
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method == "GET":
        for transaction in transactions:
            if transaction["id"] == transaction_id:
                return render_template("edit.html", transaction=transaction)
            
    if request.method == "POST":
        date = request.form['date']           # Get the 'date' field value from the form
        amount = float(request.form['amount'])# Get the 'amount' field value from the form and convert it to a float

        # Find the transaction with the matching ID and update its values
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date       # Update the 'date' field of the transaction
                transaction['amount'] = amount   # Update the 'amount' field of the transaction
                break
        return redirect(url_for("get_transactions")) 
    
# Delete operation
@app.route("/delete/<int:transaction_id>") ## http://127.0.0.1:5000/delete/2 
def delete_transaction(transaction_id):
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break
    return redirect(url_for("get_transactions"))

# search in range of min_amount and max_amount
@app.route("/search", methods=["POST", "GET"]) ## so go for http://127.0.0.1:5000/search 
def search_transactions():
    if request.method == "POST":
        min_val = request.form["min_amount"]
        max_val = request.form["max_amount"]
        filtered_transactions = list()
        for transaction in transactions:
            if float(transaction["amount"]) > float(min_val) and float(transaction["amount"]) < float(max_val):
                filtered_transactions.append(transaction)
        return render_template("transactions.html", transactions=filtered_transactions)
    
    if request.method == "GET":
        return render_template("search.html")


@app.route("/balance", methods=["GET", "POST"]) # http://127.0.0.1:5000/balance to see results
def total_balance():
    if request.method == "GET":
        amount_list = [transaction["amount"] for transaction in transactions]
        balance = sum(amount_list)
        return render_template("transactions.html", total_balance=balance)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
    