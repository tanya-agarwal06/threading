#ques 1:

print("The Access Token is a credential that can be used by an application to access an API.\n"
      "1. Go to https://dev.twitter.com/apps/new and log in, if necessary\n"
      "2.Enter your Application Name, Description and your website address. You can leave the callback URL empty.\n"
      "3.Accept the TOS, and solve the CAPTCHA.\n"
      "4.Submit the form by clicking the Create your Twitter Application"
      "5.Copy the consumer key (API key) and consumer secret from the screen into your application."
        )

#ques 2:        #code:
import socket
a=socket.gethostname("google.com")
b=socket.gethostbyname("facebook.com")
print("ip of google",a)
print("ip of facebook",b)

#theory

print("\n")
print("1. You type wwww.google.com into the address bar of your browser.\n"
      "2.The browser checks the cache for a DNS record to find the corresponding IP address of www.google.com.\n"
      "3. If the requested URL is not in the cache, ISP’s DNS server initiates a DNS query to find the IP address of the server that hosts maps.google.com.\n"
      "4. Browser initiates a TCP connection with the server.\n"
      "5. The browser sends an HTTP request to the web server.\n"
      "6. The server handles the request and sends back a response.\n"
      "7. The server sends out an HTTP response.\n"
      "8.the browser displays the html content")



#ques 3:
print("\n")
from keys import access_Token,access_Token_secret ,consumer_key,consumer_secret
import tweepy

oauth = tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_Token,access_Token_secret)
api = tweepy.API(oauth)
print(api.search("#sanju"))

#ques 4:
print("\n")
print("library:- A library is a collection of functions / objects that serves one particular purpose. you could use a library in a variety of projects.\n")
print("An API is an interface for other programs to interact with your program without having direct access. \n")
print("for example: in pythoon math is a library which have many functions like factorial,gcd etc.library is present offline so all the functions are there offline\n")
print("and api for example twiter,gmail api,facebook api all these are used for interaction and also these are not present offline as the code is taken from the servers of the company whose api it is")

#ques 5:

print("\n")
user = api.get_user('abhayjindal5')
timelin=api.user_timeline(screen_name='abhayjindal5',count=200,tweet_mode="extended")
print(user.screen_name)
print(user.followers_count)
print(timelin)