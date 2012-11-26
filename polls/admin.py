#####################################
#polls/admin.py created by Developer
#####################################
from polls.models import Poll, Choice   # from package import class objects

from django.contrib import admin


class ChoiceInline(admin.TabularInline):
    #Method 4: class ChoiceInline(admin.StackedInline):
    model = Choice
    # specify number of Choices display on screen
    extra = 3


class PollAdmin(admin.ModelAdmin):
    # customize display form
    # Method 1
    #fields = ['pub_date', 'question']

    # Method 2: split the form up into fieldsets
    #fieldsets = [
    #(None, {'fields': ['question']}),
    #('Date information', {'fields': ['pub_date']}),
    #]

    # Method 3: form partly collapsed - for long form use
    fieldsets = [
    (None, {'fields': ['question']}),
    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    #register Choice with the admin
    # Method 4, 5: Display Choice objects
    inlines = [ChoiceInline]

    # Method 6: Display individual field name as columns
    # list_display admin option is a tuple
    list_display = ('question', 'pub_date', 'was_published_recently')

    # Add filter sidebar that allow user to set pub_date filter
    list_filter = ['pub_date']

    # adds a search box at the top of the change list
    search_fields = ['question']

    # Display available year - drill down by month and by day
    date_hierarchy = 'pub_date'

# register Poll with the admin
admin.site.register(Poll, PollAdmin)
