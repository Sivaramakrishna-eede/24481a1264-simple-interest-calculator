from flask import  Flask, redirect,render_template
app= Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to Flaskapp<=>routing"

@app.route('/greet/<username>')
def greet(username):
    return f"good mrng, {username} "
'''
@app.route('/delete/<int: roll>')
def delete_user(roll):
    return  redirect(url_for(greet))
'''
@app.route('/calculator',methods=['GET','POST'])
def si():
    if request.method == 'POST':
        P= float(request.form['p'])
        T= float(request.form['t'])
        R= float(request.form['r'])
        result = (p*t*r)/100
        total = P + result
        return render_tamplate('index.html',result=result,total=total,p=P,t=T,r=R)
    
 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=3500)