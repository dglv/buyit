from flask import Flask, render_template, request
import json
import service

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/main', methods=['GET'])
def render_main_page():
    orders_lengths = service.get_orders_lengths()
    return render_template('main.html',
                           the_title='Покупашка',
                           the_orders_lengths=orders_lengths)


@app.route('/item', methods=['GET'])
def render_item_page():
    order_id = request.args.get('order_id')
    return render_template('item.html',
                           the_title='Товары для Корзины ' + order_id,
                           the_order_id=order_id,
                           the_order_length=len(service.get_order(order_id)))


@app.route('/order', methods=['GET'])
def render_order_page():
    order_id = request.args.get('order_id')
    order = service.get_order(order_id)
    return render_template('order.html',
                           the_order_id=order_id,
                           the_title='Корзина ' + order_id,
                           the_order=order)


@app.route('/item', methods=['POST'])
def update_item():
    order_id = request.form['order_id']
    item = request.form['item']
    comment = request.form['comment']
    is_checked = request.form['is_checked']
    if item:
        service.update_item(order_id, item, comment, is_checked)
    return json.dumps({'success': True, 'order_length': len(service.get_order(order_id))}), 200, {
        'ContentType': 'application/json'}


@app.route('/item_position', methods=['POST'])
def change_item_position():
    order_id = request.form['order_id']
    item = request.form['item']
    position = request.form['position']
    if item and position:
        service.change_item_position(order_id, item, position)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/item', methods=['DELETE'])
def remove_item():
    order_id = request.form['order_id']
    item = request.form['item']
    if item:
        service.remove_item(order_id, item)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/items', methods=['DELETE'])
def remove_items():
    order_id = request.form['order_id']
    items_str = request.form['items']
    if items_str:
        items = json.loads(items_str)
        for i in items:
            service.remove_item(order_id, i)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/about', methods=['GET'])
def render_about_page():
    return render_template('about.html',
                           the_title='О Программе',
                           the_app_name='Покупашка',
                           the_app_version='0.2.3',
                           the_authors='Артём Галовач, Дима Галовач')


@app.route('/release_notes', methods=['GET'])
def render_release_notes():
    return render_template('release.html', the_title='Информация о релизах')


@app.route('/order', methods=['DELETE'])
def remove_order():
    order_id = request.form['order_id']
    service.remove_order(order_id)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


if __name__ == '__main__':
    app.run(debug=True, port=8888)
