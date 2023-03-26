from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def page1():
    page_title = 'Page 1'
    return render_template('page1.html', page_title=page_title)

@app.route('/page2/')
def page2():
    page_title = 'Page 2'
    return render_template('page2.html', page_title=page_title)

@app.route('/page3/')
def page3():
    page_title = 'Page 3'
    return render_template('page3.html', page_title=page_title)

@app.route('/page4/')
def page4():
    page_title = 'Page 4'
    return render_template('page4.html', page_title=page_title)

@app.route('/page5/')
def page5():
    page_title = 'Page 5'
    return render_template('page5.html', page_title=page_title)

@app.route('/page6/')
def page6():
    page_title = 'Page 6'
    return render_template('page6.html', page_title=page_title)

@app.route('/page7/')
def page7():
    page_title = 'Page 7'
    return render_template('page7.html', page_title=page_title)

@app.route('/page8/')
def page8():
    page_title = 'Page 8'
    return render_template('page8.html', page_title=page_title)

@app.route('/page9/')
def page9():
    page_title = 'Page 9'
    return render_template('page9.html', page_title=page_title)


@app.route('/page10/')
def page10():
    page_title = 'Page 10'
    return render_template('page10.html', page_title=page_title)

@app.route('/page11/')
def page11():
    page_title = 'Page 11'
    return render_template('page11.html', page_title=page_title)

@app.route('/page12/')
def page12():
    page_title = 'Page 12'
    return render_template('page12.html', page_title=page_title)

if __name__ == '__main__':
    app.run(debug=True)
