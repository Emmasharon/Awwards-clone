class ProjectTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Moringa = Project(
            name='Moringa', link='#')
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Moringa, Project))
        # Testing Save Method
    def test_save_method(self):
        self.Moringa.project_save()
        Projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)
    def test_save_method(self):
        self.Moringa.project_delete()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.emmasharon19@gmail.com = Profile(name='', Bio='', Contact='emmasharon19@gmail.com')
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.emmasharon19@gmail.com, Profile))
        # Testing Save Method
    def test_save_method(self):
        self.emmasharon19@gmail.com.profile_save()
        profiles = profiles.objects.all()
        self.assertTrue(len(profiles) > 0)
    def test_save_method(self):
        self.emmasharon19@gmail.com.profile_delete()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)