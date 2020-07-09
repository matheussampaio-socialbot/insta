from instapy import InstaPy

session = InstaPy(username="", password="")
session.login()
session.like_by_tags(["python code", "pentest", "hacking"], amount=5)
session.set_dont_like(["lammer", "coding"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!!", "Sweet!", "Beautiful :heart_eyes:"])
session.end()
