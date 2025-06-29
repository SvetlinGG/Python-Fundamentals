
class User:

    def __init__(self, username):
        self.username = username
        self.friends = []
        self.photos = []
        self.posts = []

    def add_friends(self, friend):
        self.friends.append(friend)
        print(f'{self.username} added {friend.username} as a friend')

    def create_post(self, content):
        post = Post(self, content)
        self.posts.append(post)

    def view_post(self):
        print(f"\n{self.username}'s Post: ")
        for post in self.posts:
            print(f' - {post.content} by {post.author}')


class Post:

    def __init__(self, author, content):
        self.author = author
        self.content = content