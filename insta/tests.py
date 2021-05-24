from django.test import TestCase
from .models import Profile, Image, Comment
from django.contrib.auth.models import User

class ImageTestClass(TestCase):
    def setUp(self):
    
        self.user_jk = User(username='josh', email='josh@gmail.com', password='123456')
        self.profile_jk = Profile(profile_photo='/path/image.png', bio='This is my bio', user=self.user_jk)
        self.image_jk = Image(image_name='Football', image_caption='|||||||',image_location='/path/image.png', profile=self.profile_jk)
        
        
    def test_save_image(self):
        self.user_jk.save()
        self.profile_jk.save()
        self.image_jk.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)> 0)
        
    def test_delete_image(self):
        self.user_jk.save()
        self.profile_jk.save()
        self.image_jk.save_image()
        self.image_jk.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)
        
    def test_update_caption(self):
        self.user_jk.save()
        self.profile_jk.save()
        self.image_jk.save_image()
        self.image_jk.get_img_id(self.image_one.id)
        self.image_jk.update_cap('This is sparta')
        self.assertTrue(self.image_jk.image_caption=='This is sparta')
        
class ProfileTestClass(TestCase):
    def setUp(self):
        self.user_jh = User(username='johndoo', email='johndoe@gmail.com', password='abcdef')
        self.profile_too = Profile(profile_photo='/path/imgtwo.png', bio='This is the second bio', user=self.user_john)
        
        
    def test_save_profile(self):
        self.user_jh.save()
        self.profile_too.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    def test_delete_profile(self):
        self.user_jh.save()
        self.profile_too.save_profile()
        self.profile_too.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)== 0)
        
    def test_update_bio(self):
        self.user_jh.save()
        self.profile_too.save_profile()
        self.profile_too.get_prof_id(self.profile_too.id)
        self.profile_too.update_profile('This is the third bio')
        self.assertTrue(self.profile_too.bio=='This is the third bio')
    
    def test_search_by_profile(self):
        self.user_jh.save()
        self.profile_too.save_profile()
        profiles = self.profile_too.search_by_profile('johndoo')
        
        self.assertTrue(len(profiles) > 0)

class CommentTestClass(TestCase):
    def setUp(self):
        self.user_j = User(username='jack', email='jackdoe@gmail.com', password='abcdef')
        self.profile = Profile(profile_photo='/path/imgthree.png', bio='I am Jack', user=self.user_j)
        self.image_three = Image(image_name='Food', image_caption='Juicy steak',image_location='/path/imgfour.png', profile=self.profile)
        self.comment_one = Comment(comment='This food looks delicious', user_id=self.user_j, image_id=self.image_three)
        
        
    
    def test_save_comments(self):
        self.user_j.save()
        self.profile.save_profile()
        self.image_three.save_image()
        self.comment_one.save_comment()
        comments = Comment.objects.all()
        
        self.assertTrue(len(comments)> 0)
        

        