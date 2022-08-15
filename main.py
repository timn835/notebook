from website import create_app

app = create_app()

#we do the following 2 lines so that only when
#we run this file (not if we import) are we going
#to execute app.run . If you were to simply import main.py,
# you do not want to run the webserver.

if __name__ == '__main__':
    app.run(debug=True) 
    
#debug=True means the webserver will be 
#restarted everytime the code is changed.
#we only have this in development, not in production

