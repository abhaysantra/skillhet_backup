from django.contrib import admin
from .models import Slider, Category, SocialLink, SiteAddress, About, WhyChooseUs, Enquery, CoreValue, PostDetail, OurSkill

class SliderAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag') #Display Image & Title
    # def has_add_permission(self, request, obj=None):  #For Stop Add Button
    #     return False

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"category_slug": ("category_name",)}
    list_display = ('category_name', 'image_tag', 'category_slug',)

class SociallinkAdmin(admin.ModelAdmin):
    list_display = ('facebook','twitter','flickr','linkedin')
    def has_add_permission(self, request, obj=None):  
        return False

class SiteAddressAdmin(admin.ModelAdmin):
    list_display = ('phone','landline','email','address')
    def has_add_permission(self, request, obj=None):  
        return False

class AboutAdmin(admin.ModelAdmin):
    list_display = ('first_title','second_title','image_tag')
    def has_add_permission(self, request, obj=None):  
        return False

class WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag','content')
    def has_add_permission(self, request, obj=None):  
        return False

class EnqueryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'subject', 'message')
    def has_add_permission(self, request, obj=None):  
        return False

class CoreValueAdmin(admin.ModelAdmin):
    list_display = ('first_title', 'second_title', 'content', 'image_tag')
    def has_add_permission(self, request, obj=None):  
        return False

class PostDetailAdmin(admin.ModelAdmin):
    list_display = ('main_content', 'title1', 'title2', 'image_tag')
    # def has_add_permission(self, request, obj=None):  
    #     return False

class OurSkillAdmin(admin.ModelAdmin):
    list_display = ('heading', 'title1', 'content1', 'image_tag')
    def has_add_permission(self, request, obj=None):  
        return False
   

admin.site.register(Slider, SliderAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SocialLink, SociallinkAdmin)
admin.site.register(SiteAddress, SiteAddressAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(WhyChooseUs, WhyChooseUsAdmin)
admin.site.register(Enquery, EnqueryAdmin)
admin.site.register(CoreValue, CoreValueAdmin)
admin.site.register(PostDetail, PostDetailAdmin)
admin.site.register(OurSkill, OurSkillAdmin)
