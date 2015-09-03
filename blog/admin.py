from django.contrib import admin
from blog.models import Post
import time
import urllib
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
  list_display = ('title','pub_date', 'visible', 'get_twitter_post')
  fields = (('title','pub_date','visible'),('reality','reality_image'),('story','story_image'))
  def get_twitter_post(self, instance):
    tweet = "Neuer Blogeintrag #RealityCheck:\n"+instance.title+"\n\nhttp://realitycheck.pl/post/{}/".format(int(time.mktime(instance.pub_date.timetuple())))+"\n\n({} / {})".format(instance.reality_wordcount, instance.story_wordcount)
    return "<a href='https://twitter.com/intent/tweet?text={}'>Tweet this</a>".format(urllib.quote(tweet.encode("utf-8")))
  get_twitter_post.allow_tags = True
  pass

admin.site.register(Post,BlogAdmin)
