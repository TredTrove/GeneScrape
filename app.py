from flask import Flask, jsonify, request, flash, url_for, redirect, render_template

app = Flask(__name__)
# app.config.from_pyfile('app.cfg')
app.config['DEBUG'] = True

@app.route('/', methods=('GET', 'POST'))
def landing():
#    form = Submit(request.form)
#    if request.method == 'POST':
#        goGo(form.name.data, form.message.data, form.email.data)
#        redirect('success')
    return render_template('index.html')#, form=form)

if __name__ == "__main__":
    app.run()
