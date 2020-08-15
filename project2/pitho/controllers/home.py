from pitho.autoload import *
@app.route("/")
def home():
	if session.get("logged_in") is not None:
		return redirect("/myaccount")
	base=configuration('base_theme')
	return render_template(base+"/home.html")
@app.route("/login_submit",methods=['GET','POST'])
def login_submit():
	data = request.form
	user = Users()
	status=user.login(data)
	if status == False:
		flash("Invalid username and password")
		return redirect("/")
	else:
		session['logged_in'] = status
		return redirect("/myaccount")
	return "yes"
	#when we use the data from form then we use request an when we use the data through API then we use requests

