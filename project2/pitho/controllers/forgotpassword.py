from pitho.autoload import *
@app.route("/forgotpassword")
def forgotpassword():
	base = configuration('base_theme')
	return render_template(base+"/forgotpassword.html")
@app.route("/forgotpassword_submit",methods= ['GET','POST'])
def forgotpassword_submit():
	if request.method != 'POST':
		return redirect("/")
	data = request.form
	if 'Password' in data.keys():
		user = Users()
		status=user.password_reset(data)
		if status == False:
			flash("Please check your email and otp")
			return redirect(request.referrer)
		flash("successfully update your password")
		return redirect("/")
	user=Users()
	status = user.forgotpassword(data)
	if status == False:
		flash("your email doesnt exist")
		return redirect("forgotpassword")
	else:
		flash("We have sent a reset password link on your email")
		return redirect("/")