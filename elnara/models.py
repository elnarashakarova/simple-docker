from django.db import models

# HOME SECTION

class Home(models.Model):
    name = models.CharField(max_length=20)
    greetings_1 = models.CharField(max_length=200)
    greetings_2 = models.CharField(max_length=200, blank=True, null=True)
    #picture = models.ImageField(upload_to='picture/')
    # save time when modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ABOUT SECTION

class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/',blank=True, null=True)
    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career


class Profile(models.Model):
    about = models.ForeignKey(About,
                                on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)



# SKILLS SECTION

class Category(models.Model):
    name = models.CharField(max_length=20)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category,
                                on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)

    

# # PORTFOLIO SECTION

# class Portfolio(models.Model):
#     image = models.ImageField(upload_to='portfolio/')
#     link = models.URLField(max_length=200)

#     def __str__(self):
#         return f'Portfolio {self.id}'
    
# PPOJECTS SECTION  ######

# class Projects(models.Model):
#     image = models.ImageField(upload_to='projects/', blank=True, null=True)
#     video = models.FileField(upload_to = 'projects/', default='default_video.mp4', blank=True, null=True)    
#     #link = models.URLField(max_length=200)

#     def __str__(self):
#         return f'Projects {self.id}'


# PROJECTS SECTION
class Projects(models.Model):
    #image = models.ImageField(upload_to='projects/', blank=True, null=True)
    video = models.TextField(blank=True, null=True, help_text="Add the embed link of the video")
    link = models.URLField(max_length=200, default='http://example.com')  # Set a default value here

    def __str__(self):
        return f'Projects {self.id}'

    
    
# Certificate SECTION   ######

class Certificates(models.Model):
    image = models.ImageField(upload_to='certificates/')
    link = models.URLField(max_length=200)
    title = models.TextField(max_length=250, default='title name')

    def __str__(self):
        return f'Certificates {self.id}'


