from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = 'y3DOWd8CpBUOVQIT5h3i0WflWSRROR3AA6mQgck2'


def addOrder(dessert, mitVanillaSauce):
    if not session.has_key('orders'):
        session['orders'] = []

    session['orders'].append({
        'dessert': dessert,
        'mitVanillaSauce': mitVanillaSauce
    })

def getNumOrders():
    orders = session.get('orders', [])
    return len(orders)



@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html', numOrders=getNumOrders())

@app.route('/order', methods=['POST', 'GET'])
def order():
    if request.method == 'POST':
        dessert = request.form['dessert']
        mitVanillaSauce = request.form.has_key('mitVanillaSauce')
        addOrder(dessert, mitVanillaSauce)
        return redirect(url_for('index'))
    else:
        return render_template('order.html')



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')