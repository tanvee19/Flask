from pitho.autoload import *
@app.route("/signup")
def signup():
	base = configuration('base_theme')
	return render_template(base+"/signup.html")
@app.route("/signup-submit",methods = ['GET','POST'])
def signup_submit():
	if request.method != 'POST':
		return redirect("/")
	data=request.form
	user = Users()
	status = user.signup(data)
	if status == False:
		flash("Your email already exist")
		return redirect("/signup")
	else:
		flash("successfully created your account")
		return redirect("/")
	return "yes"