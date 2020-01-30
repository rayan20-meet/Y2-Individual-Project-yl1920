from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from database import *
from urllib2 import Request, urlopen
import requests, json


app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


##### Code here ######
@app.route('/')
def home():
	return render_template("index.html", animals= query_all())

@app.route('/contact')
def contact():
	return render_template("contact.html")


@app.route('/donar')
def donar():
	return render_template("donar.html")

@app.route('/about')
def about():
	return render_template("about.html")


@app.route('/add-to-donations/<int:animalID>')
def add_to_donations(animalID):
	# Add_To_Donations(take from form)
	print("added to Donations")
	

# @app.route('/endangered', methods = ['GET'])
# def endangered():
# 	request = Request('https://swe-endangered-animals.appspot.com/single_animal_data/')
# 	response_body = urlopen(request).read()
# 	print response_body
# @app.route('/study_image', methods = ['POST'])
# def study_image():

# 	image_url = request.form['url-input']
#     # At this point you have the image_url value from the front end
#     # Your job now is to send this information to the Clarifai API
#     # and read the result, make sure that you read and understand the
#     # example we covered in the slides! 

#     # YOUR CODE HERE!
# 	headers = {'Authorization':'Key <47021855903742ea870c9bdec8df83de>'}
# 	api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"
# 	data ={"inputs": [
# 			{
# 			"data": {
# 				"image": {
# 					"url":image_url
# 			}
# 				}
# 					}
# 		]}

# 	response = requests.post(api_url, headers=headers, data=json.dumps(data))
# 	request_dict = json.loads(response.content)

# 	isItAnAnimal = False 

# 	for concept in (request_dict["outputs"][0]["data"]["concepts"]):
# 			if concept["name"]=="animal" or concept["name"]=="animals":
# 				isItAnAnimal=True
# 				print("it's an endangered animal")




# 	return render_template('about.html', animals= query_all(), result= isItAnAnimal)


#####################


if __name__ == '__main__':
    app.run(debug=True)