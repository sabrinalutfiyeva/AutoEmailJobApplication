  import smtplib 
   
    my_email=’jess_xxx@gmail.com’
    password_key=’xxxxx’
    
    # SMTP Server and port no for GMAIL.com
    gmail_server= "smtp.gmail.com"
    gmail_port= 587


    # Starting connection
    my_server = smtplib.SMTP(gmail_server, gmail_port)
    my_server.ehlo()
    my_server.starttls()
      
    # Login with your email and password
    my_server.login(my_email, password_key)