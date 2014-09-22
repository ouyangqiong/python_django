from django.contrib import admin
from polls.models import Question,Choice
# Register your models here.
#admin.site.register(Question,)
class ChoiceStackInline(admin.StackedInline):
    model=Choice
    extra=3

class ChoiceTabularInline(admin.TabularInline):  
    model=Choice
    extra=3
class QuestionAdmin(admin.ModelAdmin):
    # fields=['pub_date','question_text']
    list_display=('question_text','pub_date','was_published_recently')
    list_filter=['pub_date']
    search_fields=['question_text']
    fieldsets = [
              (None,                {'fields':['question_text']}),
              ('Date Information',  {'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines=[ChoiceTabularInline]
     
admin.site.register(Question,QuestionAdmin) 
   
class ChoiceAdmin(admin.ModelAdmin):
    list_display=('question','choice_text','votes')
    
admin.site.register(Choice,ChoiceAdmin)