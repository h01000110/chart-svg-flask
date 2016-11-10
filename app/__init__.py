from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Mes(db.Model):
    __tablename__ = 'meses'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dado = db.Column(db.String)

    def __init__(self, dado):
        self.dado = dado


db.create_all()
a = 0
for i in range(12):
    db.session.add(Mes(a))
db.session.commit()


@app.route('/')
def index():
    x = Mes.query.all()
    tudo = 0
    for i in x:
        b = x.index(i)
        tudo += int(x[b].dado)
    metade = int(tudo / 2)

    jan = Mes.query.filter_by(id=1).first()
    if int(jan.dado) != 0:
        jan = (int(jan.dado) / tudo) * 100
    else:
        jan = 0

    fev = Mes.query.filter_by(id=2).first()
    if int(fev.dado) != 0:
        fev = (int(fev.dado) / tudo) * 100
    else:
        fev = 0

    mar = Mes.query.filter_by(id=3).first()
    if int(mar.dado) != 0:
        mar = (int(mar.dado) / tudo) * 100
    else:
        mar = 0

    abr = Mes.query.filter_by(id=4).first()
    if int(abr.dado) != 0:
        abr = (int(abr.dado) / tudo) * 100
    else:
        abr = 0

    mai = Mes.query.filter_by(id=5).first()
    if int(mai.dado) != 0:
        mai = (int(mai.dado) / tudo) * 100
    else:
        mai = 0

    jun = Mes.query.filter_by(id=6).first()
    if int(jun.dado) != 0:
        jun = (int(jun.dado) / tudo) * 100
    else:
        jun = 0

    jul = Mes.query.filter_by(id=7).first()
    if int(jul.dado) != 0:
        jul = (int(jul.dado) / tudo) * 100
    else:
        jul = 0

    ago = Mes.query.filter_by(id=8).first()
    if int(ago.dado) != 0:
        ago = (int(ago.dado) / tudo) * 100
    else:
        ago = 0

    set = Mes.query.filter_by(id=9).first()
    if int(set.dado) != 0:
        set = (int(set.dado) / tudo) * 100
    else:
        set = 0

    out = Mes.query.filter_by(id=10).first()
    if int(out.dado) != 0:
        out = (int(out.dado) / tudo) * 100
    else:
        out = 0

    nov = Mes.query.filter_by(id=11).first()
    if int(nov.dado) != 0:
        nov = (int(nov.dado) / tudo) * 100
    else:
        nov = 0

    dez = Mes.query.filter_by(id=12).first()
    if int(dez.dado) != 0:
        dez = (int(dez.dado) / tudo) * 100
    else:
        dez = 0

    return render_template('index.html', jan=jan, fev=fev, mar=mar, abr=abr,
                           mai=mai, jun=jun, jul=jul, ago=ago, set=set,
                           out=out, nov=nov, dez=dez, tudo=tudo, metade=metade)


@app.route('/altera', methods=['POST'])
def altera():
    mes = request.form.get('mes')
    dado = request.form.get('dado')

    p = Mes.query.filter_by(id=mes).first()
    if dado.isdigit():
        p.dado = dado
        db.session.commit()

    return redirect(url_for('index'))


@app.route('/reset', methods=['POST'])
def reset():
    for i in range(1, 13):
        r = Mes.query.filter_by(id=i).first()
        r.dado = 0
    db.session.commit()

    return redirect(url_for('index'))
