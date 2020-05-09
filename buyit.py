from flask import Flask, render_template, request
import json
import service

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/main', methods=['GET'])
def render_main_page():
    return render_template('main.html', the_title='Выберите действие')


@app.route('/item', methods=['GET'])
def render_item_page():
    return render_template('item.html',
                           the_title='Создание Заказа',
                           the_order_length=len(service.get_order()))


@app.route('/item', methods=['POST'])
def update_item():
    item = request.form['item']
    comment = request.form['comment']
    is_checked = request.form['is_checked']
    if item:
        service.update_item(item, comment, is_checked)
    return json.dumps({'success': True, 'order_length': len(service.get_order())}), 200, {
        'ContentType': 'application/json'}


@app.route('/item', methods=['DELETE'])
def remove_item():
    item = request.form['item']
    if item:
        service.remove_item(item)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/items', methods=['DELETE'])
def remove_items():
    items_str = request.form['items']
    if items_str:
        items = json.loads(items_str)
        for i in items:
            service.remove_item(i)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/order', methods=['GET'])
def render_order_page():
    order = service.get_order()
    return render_template('order.html',
                           the_title='Выполнение Заказа',
                           the_order=order)


@app.route('/about', methods=['GET'])
def render_about_page():
    return render_template('about.html',
                           the_title='О Программе',
                           the_app_name='Покупашка',
                           the_app_version='0.2.2',
                           the_authors='Артём Галовач, Дима Галовач')


@app.route('/release_notes', methods=['GET'])
def render_release_notes():
    return render_template('release.html', the_title='Информация о релизах')


@app.route('/order', methods=['DELETE'])
def remove_order():
    service.remove_order()
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


if __name__ == '__main__':
    app.run(debug=True, port=8888)
