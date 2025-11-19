from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from accounts.models import User, Profile
from blog.models import Post, Category

class Command(BaseCommand):
    help = "This is a command that generates a dummy data and saves it in the data base for debug"
    fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(email=self.fake.email(), password=self.fake.password(length=12))
        profile = Profile.objects.get(user=user)
        profile.image = self.fake.image_url()
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.description = self.fake.paragraph(nb_sentences=20)
        profile.save()
        print('successfully generate the profile and user tables')
        category = Category.objects.create(name=self.fake.name())
        for _ in range(10):
            post = Post.objects.create(
                image = self.fake.image_url(),
                author = profile,
                title = self.fake.paragraph(nb_sentences=5),
                content = self.fake.paragraph(nb_sentences=40),
                status = True,
                category = category,
                published_date = timezone.now(), 
            )
        print("successfully created 10 the category and user tables to")

    