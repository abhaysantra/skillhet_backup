from django.db import models
from tinymce import HTMLField
from django.utils.safestring import mark_safe
from django_resized import ResizedImageField

class Slider(models.Model):
    small_title = models.CharField(max_length=255)
    title_content = HTMLField(default=None)
    title = models.CharField(max_length=255)
    image = ResizedImageField(size=[1600, 900] ,upload_to='slider' , default=None)
    
    # For Image Display In Admin
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 200px; height: 100px;" />' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_slug = models.SlugField(default=None)
    category_image = models.ImageField(upload_to='category' , default=None)
    
    def image_tag(self):
        if self.category_image:
            return mark_safe('<img src="%s" style="width: 64px; height: 64px;" />' % self.category_image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.category_name

class SocialLink(models.Model):
    facebook = models.CharField(max_length=256,default=None)
    twitter = models.CharField(max_length=256,default=None)
    flickr = models.CharField(max_length=256,default=None)
    linkedin = models.CharField(max_length=256,default=None)

    def __str__(self):
        return self.facebook

class SiteAddress(models.Model):
    phone = models.CharField(max_length=256,default=None)
    landline = models.CharField(max_length=256,default=None)
    email = models.CharField(max_length=256,default=None)
    web_link = models.CharField(max_length=256,default=None)
    address = models.TextField(default=None)
    footer_content = models.TextField(default=None)

    def __str__(self):
        return self.email

class CoreValue(models.Model):
    first_title = models.CharField(max_length=255)
    second_title = models.CharField(max_length=255)
    content = models.TextField(default=None)
    small_content1 = models.TextField(default=None)
    small_content2 = models.TextField(default=None)
    small_content3 = models.TextField(default=None)
    image = ResizedImageField(size=[272, 300], upload_to='core_value', blank=True)
    
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 272px; height: 300px;" />' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.first_title

class About(models.Model):
    first_title = models.CharField(max_length=255)
    second_title = models.CharField(max_length=255)
    content = HTMLField(default=None)
    image1 = ResizedImageField(size=[400, 400], upload_to='about', blank=True)
    image2 = ResizedImageField(size=[400, 400], upload_to='about', blank=True)
    signature = models.ImageField(upload_to='about', blank=True)
    
    def image_tag(self):
        if self.image1:
            return mark_safe('<img src="%s" style="width: 200px; height: 200px;" />' % self.image1.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.first_title

class WhyChooseUs(models.Model):
    title = models.CharField(max_length=256,default=None)
    content = models.TextField(default=None)
    image = models.ImageField(upload_to='why_choose_us', default=None)
    
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 64px; height: 64px;" />' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title

class PostDetail(models.Model):
    category = models.ForeignKey('Category',default=None, on_delete=models.CASCADE)
    main_content = HTMLField(default=None)
    slider_image1 = ResizedImageField(size=[1000, 500] ,upload_to='post_details' , default=None)
    slider_image2 = ResizedImageField(size=[1000, 500] ,upload_to='post_details' , default=None)
    slider_image3 = ResizedImageField(size=[1000, 500] ,upload_to='post_details' , default=None)
    
    title1 = models.CharField(max_length=255)
    content1 = HTMLField(default=None)
    image1 = ResizedImageField(size=[456, 286] ,upload_to='post_details' , default=None)

    title2 = models.CharField(max_length=255)
    content2 = HTMLField(default=None)
    image2 = ResizedImageField(size=[456, 303] ,upload_to='post_details' , default=None)
    sub_title1 = models.CharField(max_length=255)
    sub_title2 = models.CharField(max_length=255)
    sub_title3 = models.CharField(max_length=255)

    def image_tag(self):
        if self.slider_image1:
            return mark_safe('<img src="%s" style="width: 200px; height: 100px;" />' % self.slider_image1.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title1

class OurSkill(models.Model):
    heading = models.CharField(max_length=255, default=None)

    title1 = models.CharField(max_length=255, default=None)
    content1 = models.TextField(default=None)

    title2 = models.CharField(max_length=255, default=None)
    content2 = models.TextField(default=None)

    title2 = models.CharField(max_length=255, default=None)
    content2 = models.TextField(default=None)

    title3 = models.CharField(max_length=255, default=None)
    content3 = models.TextField(default=None)
    image = ResizedImageField(size=[750, 750] ,upload_to='our_skill' , default=None)

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 200px; height: 200px;" />' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.heading

class Enquery(models.Model):
    name = models.CharField(max_length=256, blank=True)
    email = models.CharField(max_length=256, blank=True)
    mobile = models.CharField(max_length=256, blank=True)
    subject = models.CharField(max_length=256, blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name