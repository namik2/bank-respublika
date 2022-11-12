from flask import render_template,request
from app import app
from forms import CardExtensionsForm
from models import News,News_detailed,Products,CardExtensions


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/news")
def news():
    news = News.query.all()
    return render_template('xeberler.html',news=news)


@app.route("/news/page-1")
def page1():
    return render_template('page1.html')


@app.route("/news/page-2")
def page2():
    return render_template('page2.html')

@app.route("/cardrenew",methods=['GET','POST'])
def cardrenew():
    post_data= request.form
    print(post_data,'salamsssssss')
    form = CardExtensionsForm()
    if request.method =='POST':
        form= CardExtensionsForm(data=post_data)
        print("hdfkjlajfskfjksdhaffkja")
        # if form.validate_on_submit():
        print("sdadasdassadasdadasdas")
        carextensions = CardExtensions(card_number = form.card_number.data, pasport_select = form.pasport_select.data, pasport_number = form.pasport_number.data, order = form.order.data, number = form.number.data, number_select = form.number_select.data, filial_select = form.filial_select.data)
        print(carextensions,'salaaaaam')
        carextensions.save()
    return render_template('extension.html',form=form)