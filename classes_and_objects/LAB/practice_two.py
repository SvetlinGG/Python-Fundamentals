
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
            print(f' - {post.content} by ({post.author.username})')


class Post:

    def __init__(self, author, content):
        self.author = author
        self.content = content

def important(func):
    def wrapper(*args, **kwargs):
        content = func(*args, **kwargs)
        return '[IMPORTANT] ' + content
    return wrapper

class AdminUser(User):

    @important
    def prepare_important_content(self, content):
        return content
    def create_important_content(self, content):
        important_content = self.prepare_important_content(content)
        post = Post(self, important_content)
        self.posts.append(post)
        print(f'{self.username} ;posted in IMPORTANT message: {important_content}')

svetlin = User('Svetlin')
mario = AdminUser('Mario')

svetlin.add_friends(mario)
mario.create_post('Hello tonight')
mario.create_important_content('Hello to you tonight')
svetlin.create_post('Hello SoftUni!')

svetlin.view_post()
mario.view_post()

