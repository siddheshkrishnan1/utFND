# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for
import sys


# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/') # First page 
def form():
    return render_template('form_submit.html')

@app.route('/userClaimsInput/', methods=['POST'])
def userClaimsInput():
    QS=request.form['claim']
    print ("Query string is")
    print QS
    return render_template('form_action.html', QueryString=QS)

# Second Page code down below 
#Error needs to be fixed using OOP



@app.route('/userClaimsOpinion/', methods=['POST'])
def userClaimsOpinion():
    EM = "The numbers should add up to 100!"
    truePercentage=request.form['trueInput']
    falsePercentage=request.form['falseInput']
    uncertainPercentage=request.form['unsureInput']
    total = int(truePercentage) + int(falsePercentage) + int(uncertainPercentage)
    if total != 100:
     return render_template('form_action.html', ErrorMessage=EM)   
    else:
        return render_template('form_action.html')



    # sum =int(QS) + int(QS2)

    # if sum >100 or sum<100:
    #     return render_template (userClaimsInput page , errormessage="The numbers should add up to 100")

    #In string QS, replace every string with a + and then pass it as a parameter to the API (An) 
    # QSNEW= "http://www.cs.utexas.edu/~atn/cgi-bin/api.cgi?claim="+ourstring
    
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80)