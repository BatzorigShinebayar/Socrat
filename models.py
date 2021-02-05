import datetime
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


publish_status = (
    ('0', 'no'),
    ('1', 'yes'),
)


# news_type = (
#     ('slide', 'Слайд зураг'),
#     ('about', 'Бидний тухай'),
# )


now = datetime.datetime.now()


# # # # Portfolio Models # # # #


class Sector(models.Model):
    class Meta:
        verbose_name = 'Portfolio Type'
        verbose_name_plural = 'Portfolio Type'

    title = models.CharField('title', max_length=100, null=True, blank=True)
    description = RichTextUploadingField('Read More')

    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolio'

    # Foreign Key from Sector Model
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Portfolio Type')

    # Condition
    is_published = models.CharField('Is Published', max_length=1, choices=publish_status, null=True)

    title = models.CharField('Title', max_length=100, null=True, blank=True)
    slug = models.TextField("Slug", null=True, blank=True)
    image = models.FileField(upload_to='Image/Portfolio/%Y/%m/%d')
    current_date = models.DateField('Current Date')
    start_date = models.DateField('Started Date')
    end_date = models.DateField('End Date')
    finance = models.CharField('Finance', max_length=100)
    finance_step = models.CharField('Finance Step', max_length=100)
    director = models.CharField('Director', max_length=100)
    contact = models.CharField('Contact', max_length=100)
    address = models.CharField('Address', max_length=100)
    website = models.CharField('Website Link', max_length=100)
    description = RichTextUploadingField('Description', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def progress(self):
        a_date = datetime.datetime.strptime(str(self.start_date), '%Y-%m-%d')
        b_date = datetime.datetime.strptime(str(self.current_date), '%Y-%m-%d')
        c_date = datetime.datetime.strptime(str(self.end_date), '%Y-%m-%d')
        a = datetime.datetime.timestamp(a_date)
        b = datetime.datetime.timestamp(b_date)
        c = datetime.datetime.timestamp(c_date)
        x = c - a
        y = b - a
        p = (y * 100) / x
        return p

    def __str__(self):
        return self.title


class PortfolioTimeline(models.Model):
    class Meta:
        verbose_name = 'Portfolio Timeline'
        verbose_name_plural = 'Portfolio Timeline'

    # Foreign Key from Portfolio
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, null=True, blank=True)

    title = models.CharField('Title', max_length=100)
    date = models.DateField('Date', max_length=20)
    description = RichTextUploadingField('Description', blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PortfolioImages(models.Model):
    class Meta:
        verbose_name = 'Pictures'
        verbose_name_plural = 'Pictures'

    # Foreign Key From Portfolio
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, null=True, blank=True)

    portfolio_images = models.IntegerField('ID', null=True, blank=True)
    image = models.FileField(upload_to='Image/Portfolio/%Y/%m/%d')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PortfolioFAQ(models.Model):
    class Meta:
        verbose_name = 'Portfolio FAQ'
        verbose_name_plural = "Portfolio FAQ"

    # Foreign Key From Portfolio
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, null=True, blank=True)

    question = models.CharField('Question', max_length=300, null=True, blank=True)
    answer = models.CharField('Answer', max_length=300, null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PortfolioBanner(models.Model):
    class Meta:
        verbose_name = 'Portfolio Page Hero Banner'
        verbose_name_plural = 'Portfolio Page Hero Banner'

    title = models.CharField('Title', max_length=200)
    subtitle = models.CharField('Subtitle', max_length=300)
    image = models.FileField('Banner', upload_to='Image/Banner/Portfolio/%Y/%m/%d')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# # # # End Portfolio Models # # # #


# # # # Incubation Models # # # #


class IncubationServiceGeneralInfo(models.Model):
    class Meta:
        verbose_name = "Incubation General Info"
        verbose_name_plural = "Incubation General Info"

    title = models.CharField('Title', max_length=100)
    short_description = models.TextField('Short Description')
    description = RichTextUploadingField('Description')
    link = models.CharField('Link', max_length=300)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class IncubationProgramBenefit(models.Model):
    class Meta:
        verbose_name = "Incubation Program Benefit"
        verbose_name_plural = "Incubation Program Benefit"

    title = models.CharField('Title', max_length=100)
    image = models.FileField('icon', upload_to='Image/Incubation/Icon/%Y/%m/%d')
    is_published = models.CharField('Is Published', max_length=1, choices=publish_status, null=True)
    description = RichTextUploadingField('Description')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class IncubationProgram(models.Model):
    class Meta:
        verbose_name = "Incubation Program"
        verbose_name_plural = "Incubation Program"

    # Foreign Key From Incubation Program benefit
    investment_value = models.ForeignKey(IncubationProgramBenefit, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField('Name', max_length=100)
    title = models.CharField('Title', max_length=100)
    duration = models.CharField('Duration', max_length=200)
    registration_link = models.CharField('Registration Link', max_length=100)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class IncubationTypes(models.Model):
    class Meta:
        verbose_name = "Incubation Type"
        verbose_name_plural = "Incubation Type"

    title = models.CharField('Title', max_length=100)
    description = models.TextField('Short Description')
    link = models.CharField('Link', max_length=300)
    image = models.FileField('icon', upload_to='Image/Incubation/Icon/%Y/%m/%d')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class IncubationServiceStage(models.Model):
    class Meta:
        verbose_name = "Incubation Service Stage"
        verbose_name_plural = "Incubation Service Stage"

    title = models.CharField('Title', max_length=200)
    subtitle = models.CharField('Subtitle', max_length=400)
    image = models.FileField('Banner', upload_to='Image/Incubation/%Y/%m/%d')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class IncubationPageGallery(models.Model):
    class Meta:
        verbose_name = "Incubation Gallery"
        verbose_name_plural = "Incubation Gallery"

    title = models.CharField('Title', max_length=200)
    image = models.FileField('Image', upload_to='Image/Incubation/Gallery/%Y/%m/%d')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class IncubationBanner(models.Model):
    class Meta:
        verbose_name = "Incubation Page Hero Banner"
        verbose_name_plural = "Incubation Page Hero Banner"

    title = models.CharField('Title', max_length=200)
    description = models.CharField('Description', max_length=300)
    link = models.CharField('Link', max_length=300)
    image = models.FileField('Banner', upload_to='Image/Banner/Incubation/%Y/%m/%d')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class IncubationMidBanner(models.Model):
    class Meta:
        verbose_name = "Incubation Page Middle Banner"
        verbose_name_plural = "Incubation Page Middle Banner"

    title = models.CharField('Title', max_length=200)
    image = models.FileField('MidBanner', upload_to='Image/Banner/Incubation/%Y/%m/%d')
    link = models.CharField('Link', max_length=300)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class IncubationBotBanner(models.Model):
    class Meta:
        verbose_name = "Incubation Page Bottom Banner"
        verbose_name_plural = "Incubation Page Bottom Banner"

    title = models.CharField('Title', max_length=200)
    description = models.TextField('Description')
    image = models.FileField('MidBanner', upload_to='Image/Banner/Incubation/%Y/%m/%d')
    link = models.CharField('Link', max_length=300)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

# # # # End Incubation Models # # # #


# # # # Mentor Models # # # #


class TeamType(models.Model):
    class Meta:
        verbose_name = 'Team Type'
        verbose_name_plural = 'Team Type'

    title = models.CharField('Title', max_length=100, null=True, blank=True)
    is_published = models.CharField('Is Published', max_length=1, choices=publish_status, null=True)
    description = RichTextUploadingField('Description')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TeamMembers(models.Model):
    class Meta:
        verbose_name = 'Team Members'
        verbose_name_plural = 'Team Members'

    # Foreign Key From Team Type
    team_type = models.ForeignKey(TeamType, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField('Name', max_length=50, null=True, blank=True)
    career = models.CharField('Career', max_length=100, null=True, blank=True)
    image = models.FileField('Image', upload_to='Image/Team Members/%Y/%m/%d')
    email = models.CharField('Email', max_length=100, null=True, blank=True)
    phone = models.CharField('Phone Number', max_length=100, null=True, blank=True)
    facebook = models.CharField('Facebook Link', max_length=100, null=True, blank=True)
    instagram = models.CharField('Instagram Link', max_length=100, null=True, blank=True)
    linkedin = models.CharField('Linkedin Link', max_length=100, null=True, blank=True)
    github = models.CharField('Github Link', max_length=100, null=True, blank=True)
    twitter = models.CharField('Twitter Link', max_length=100, null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TeamBanner(models.Model):
    class Meta:
        verbose_name = 'Team Page Hero Banner'
        verbose_name_plural = 'Team Page Hero Banner'

    title = models.CharField('Title', max_length=200)
    subtitle = models.CharField('Subtitle', max_length=300)
    image = models.FileField('Banner', upload_to='Image/Banner/Team/%Y/%m/%d')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# # # # End Mentor Models # # # #


# # # # Start News Models # # # #


class NewsBanner(models.Model):
    class Meta:
        verbose_name = 'News Page Hero Banner'
        verbose_name_plural = 'News Page Hero Banner'

    title = models.CharField('Title', max_length=200)
    subtitle = models.CharField('Subtitle', max_length=300)
    image = models.FileField('Banner', upload_to='Image/Banner/News/%Y/%m/%d')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class NewsTag(models.Model):
    class Meta:
        verbose_name = 'News Tag'
        verbose_name_plural = 'News Tag'

    title = models.CharField('title', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class NewsType(models.Model):
    class Meta:
        verbose_name = 'News Type'
        verbose_name_plural = 'News Type'

    title = models.CharField('title', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class News(models.Model):
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    title = models.CharField('Title', max_length=100)
    type = models.ForeignKey(NewsType, on_delete=models.CASCADE, blank=True, verbose_name='Төрөл')
    tag = models.ManyToManyField(NewsTag, blank=True)
    publish = models.CharField('Published', max_length=1, choices=publish_status)
    short_desc = models.CharField('Short Description', max_length=300)
    description = RichTextUploadingField('Description')
    image = models.FileField(upload_to='documents/%Y/%m/%d/')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class NeedFiles(models.Model):
    class Meta:
        verbose_name = 'Useful Files'
        verbose_name_plural = 'Useful Files'

    title = models.CharField('Title', max_length=100, null=True, blank=True)
    file = models.FileField(upload_to='documents/%Y/%m/%d/')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class NeedLinks(models.Model):
    class Meta:
        verbose_name = 'Useful Link'
        verbose_name_plural = 'Useful Link'

    title = models.CharField('Title', max_length=100, null=True, blank=True)
    link = models.CharField('Link', max_length=100, null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# # # # End News Models # # # #


# # # # Start FAQ Models # # # #


class FaqType(models.Model):
    class Meta:
        verbose_name = 'FAQ Type'
        verbose_name_plural = 'FAQ Type'

    title = models.CharField('Title', max_length=100)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Faq(models.Model):
    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'

    faq_type = models.ForeignKey(FaqType, on_delete=models.CASCADE, blank=True)
    question = models.CharField('Question', max_length=400)
    answer = models.TextField('Answer')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class FaqBanner(models.Model):
    class Meta:
        verbose_name = 'FAQ Page Hero Banner'
        verbose_name_plural = 'FAQ Page Hero Banner'

    title = models.CharField('Title', max_length=200)
    subtitle = models.CharField('Subtitle', max_length=300)
    image = models.FileField('Banner', upload_to='Image/Banner/FAQ/%Y/%m/%d')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# # # # End FAQ Models # # # #


class About(models.Model):
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

    title = models.CharField('Title', max_length=200)
    description = models.TextField('Description')
    image = models.FileField('Story Image', upload_to='Image/About/Story/%Y/%m/%d')
    story = models.CharField('Story Title', max_length=200)
    story_desc = models.TextField('Story Description')
    link = models.CharField('Link', max_length=300)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class AboutBanner(models.Model):
    class Meta:
        verbose_name = "About Page Hero Banner"
        verbose_name_plural = "About Page Hero Banner"

    title = models.CharField('Title', max_length=200)
    image = models.FileField('Banner', upload_to='Image/Banner/About/%Y/%m/%d')
    link = models.CharField('Link', max_length=300)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class AboutBotBanner(models.Model):
    class Meta:
        verbose_name = "About Page Bot Banner"
        verbose_name_plural = "About Page Bot Banner"

    title = models.CharField('Title', max_length=200)
    image = models.FileField('Banner', upload_to='Image/Banner/About/%Y/%m/%d')
    link = models.CharField('Link', max_length=300)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# # # # Start Comment Models # # # #


class Comment(models.Model):
    class Meta:
        ordering = ['created_date']
        verbose_name = "Comment"
        verbose_name_plural = "Comment"

    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
