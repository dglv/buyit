from flask import Flask, render_template, request
import uuid
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
                           the_title='Товары для Тележки ' + order_id,
                           the_order_id=order_id,
                           the_order_length=len(service.get_order(order_id)))


@app.route('/order', methods=['GET'])
def render_order_page():
    order_id = request.args.get('order_id')
    order = service.get_order(order_id)
    return render_template('order.html',
                           the_order_id=order_id,
                           the_title='Тележка ' + order_id,
                           the_order=order)


@app.route('/item', methods=['POST'])
def update_item():
    order_id = request.form['order_id']
    if 'item_id' in request.form:
        item_id = request.form['item_id']
    else:
        item_id = str(uuid.uuid4())
    name = request.form['name']
    comment = request.form['comment']
    is_checked = request.form['is_checked']

    item = {
        'id': item_id,
        'name': name,
        'comment': comment,
        'is_checked': is_checked
    }
    service.update_item(order_id, item)
    return json.dumps({'success': True, 'order_length': len(service.get_order(order_id))}), 200, {
        'ContentType': 'application/json'}


@app.route('/item_position', methods=['POST'])
def change_item_position():
    order_id = request.form['order_id']
    item_id = request.form['item_id']
    position = request.form['position']
    if item_id and position:
        service.change_item_position(order_id, item_id, position)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/item', methods=['DELETE'])
def remove_item():
    order_id = request.form['order_id']
    item_id = request.form['item_id']
    if item_id:
        service.remove_item(order_id, item_id)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/items', methods=['DELETE'])
def remove_items():
    order_id = request.form['order_id']
    item_ids_str = request.form['item_ids']
    if item_ids_str:
        item_ids = json.loads(item_ids_str)
        for item_id in item_ids:
            service.remove_item(order_id, item_id)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/about', methods=['GET'])
def render_about_page():
    return render_template('about.html',
                           the_title='О Программе',
                           the_app_name='Покупашка',
                           the_app_version='0.2.4',
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
