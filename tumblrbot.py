#pytumblr test
# for info about the API go to 
# https://www.tumblr.com/docs/en/api/v2

# for info and documentation for pytumblr go to 
# https://pypi.org/project/PyTumblr/

import pytumblr

print("success")


client = pytumblr.TumblrRestClient(
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
)

# # grab stuff from my account
def getMyInfo():
	myinfo = client.info() # Grabs the current user information
	print(myinfo)

# #grab stuff from another blog
def getBlogInfo():
	y2kbloginfo = client.blog_info("y2k-aesthetic")
	print(y2kbloginfo)

# #grab blogposts from another blog
def getBlogPosts():
	y2kblogposts = client.posts("y2k-aesthetic")
	print(y2kblogposts)

#Creating a text post
def publishTextPost():
	client.create_text("pfbot", state="published", slug="testing-text-posts", title="Testing", body="testing1 2 3 4")
	print("success publishing post")


# call function
publishTextPost()