
from django.test import TestCase

from .models import   LikePost, Post
# Create your tests here.


class PostTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.post = Post(caption="travel")
        self.post.save_post()

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_method(self):
        self.post.save_post()
        posts= Post.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_method(self):
        self.post.save_post()
        self.post.delete_post()
        post = Post.objects.all()
        self.assertTrue(len(post) == 0)

    def test_update(self):
        post = Post.get_category_id(self.post.id)
        post.update_post('Travel')
        post = Post.get_post_id(self.post.id)
        self.assertTrue(post.name == 'Travel')

#  #test for Like Model

class LikePostTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.like = LikePost(username="samuels")
        self.like.save_like()


    def test_instance(self):
        self.assertTrue(isinstance(self.like, LikePost))

#     

    def test_save_method(self):
        self.like.save_like()
        likes  = LikePost.objects.all()
        self.assertTrue(len(likes)>0)


# # Create your tests here.

