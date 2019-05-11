from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#####################################################
#                   ADMIN SIDE                      #
#####################################################


@app.route('/admin')
def admin():
    return render_template('admin/admin_index.html', admin=True)


@app.route('/admin/new')
def nuova_stanza():
    if request.method == 'GET':
        return render_template('admin/new_stanza.html', admin=True)
    else:
        return redirect(url_for('admin'))


@app.route('/admin/edit')
def edit_stanza():
    return redirect(url_for('admin'))


@app.route('/admin/remove')
def remove_stanza():
    return redirect(url_for('admin'))


@app.route('/admin/removeAll')
def remove_all():
    return redirect(url_for('admin'))



if __name__ == '__main__':
    app.run()
