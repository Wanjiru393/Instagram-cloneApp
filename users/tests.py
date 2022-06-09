class FollowersCountTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.fol = FollowersCount(user="test1")
        self.fol.save_followers()

        
    def test_instance(self):
        self.assertTrue(isinstance(self.user, FollowersCount))

