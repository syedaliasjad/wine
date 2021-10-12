from flask import Flask,render_template,request
import pickle
app = Flask(__name__)
@app.route('/' , methods=['GET','POST'])
def home():
    if request.method =='POST':
        model = pickle.load(open("lr_model.pkl","rb"))
        user_input = request.form.get('size')
        user_input1 = float(user_input)
        pred = model.predict([[user_input1]])
        return render_template('index.html', pred=pred)
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)