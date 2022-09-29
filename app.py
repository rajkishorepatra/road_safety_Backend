from flask import Flask,request
from flask_cors import CORS
from certificate import generate_cert



app = Flask(__name__)
CORS(app)

@app.route('/api/v1/accept-data', methods=['POST'])
def acceptData():
    name = request.json['name']
    email = request.json['email']
    
    if not name or not email:
        return {"status": "VALIDATION ERROR"}, 400
    
    print ("name: "+name + " email: "+email)
    generate_cert(name,email)
       
    return {"status": "OK"}, 200





if __name__ == "__main__":
    app.run(debug=True)