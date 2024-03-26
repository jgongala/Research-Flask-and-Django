from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

        # Create some test posts
        self.post1 = Post.objects.create(author=self.user, title='Test Post 1', description='This is test post 1')
        self.post2 = Post.objects.create(author=self.user, title='Test Post 2', description='This is test post 2')

    def test_home_view(self):
        # Log in as the test user
        self.client.login(username='testuser', password='testpassword')

        # Test if home page returns a 200 status code
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        
    def test_create_post_view(self):
        # Log in as the test user
        self.client.login(username='testuser', password='testpassword')

        # Test if create post page returns a 200 status code
        response = self.client.get(reverse('createPost'))
        self.assertEqual(response.status_code, 200)

        # Test creating a new post
        response = self.client.post(reverse('createPost'), {'title': 'New Test Post', 'description': 'This is a new test post'})
        self.assertEqual(response.status_code, 302)  # 302 is the status code for redirect, as we're redirecting after successful post creation

        # Check if the post was created
        new_post = Post.objects.get(title='New Test Post')
        self.assertEqual(new_post.author, self.user)

    def test_delete_post_view(self):
        # Log in as the test user
        self.client.login(username='testuser', password='testpassword')

        # Test deleting a post
        response = self.client.post(reverse('delete', args=[self.post1.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after successful delete

        # Check if the post was deleted
        with self.assertRaises(Post.DoesNotExist):
            Post.objects.get(id=self.post1.id)

    def test_edit_post_view(self):
        # Log in as the test user
        self.client.login(username='testuser', password='testpassword')

        # Test editing a post
        response = self.client.post(reverse('edit', args=[self.post2.id]), {'title': 'Edited Test Post', 'description': 'This is an edited test post'})
        self.assertEqual(response.status_code, 302)  # Redirect after successful edit

        # Check if the post was edited
        edited_post = Post.objects.get(id=self.post2.id)
        self.assertEqual(edited_post.title, 'Edited Test Post')
