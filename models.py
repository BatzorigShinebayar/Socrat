import datetime
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


publish_status = (
    ('0', 'no'),
    ('1', 'yes'),
)


# news_type = (
#     ('slide', 'Слайд зураг'),
#     ('about', 'Бидний тухай'),
#     ('songon', 'Сонгон шалгарулах'),
#     ('bsbb', 'Бизнесийн систем бий болгох'),
#     ('tsene', 'Үнэ цэнэ бүтээх'),
#     ('business', 'Хүний хэрэгцээг хангах Бизнес санаа'),
#     ('shiidel', 'Мэдлэгт суурилсан Шийдэл-Инноваци'),
#     ('zorilgotoi', 'Бизнесийн нэгдмэл Зорилготой баг'),
#     ('bodlogo', 'Бодлого'),
#     ('investor', 'Хөрөнгө оруулагч'),
#     ('boijigch', 'Бойжигч'),
#     ('zuvluguu', 'Хүсэлтийн зөвлөгөө'),
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
    photos = ImageSpecField(source='image', processors=[ResizeToFill(500, 500)],
                            format='JPEG', options={'quality': 100})

    current_date = models.DateField('Current Date', max_length=30)
    # # current date converting to epoch format
    # str
    # a = datetime.datetime.strptime(current_date, '%Y-%m-%d')

    start_date = models.DateField('Started Date', max_length=30)
    # # start_date converting to epoch format
    # str(start_date)
    # b = datetime.datetime.strptime(start_date, '%Y-%m-%d')

    end_date = models.DateField('End Date', max_length=30)
    # # end_date converting to epoch format
    # str(end_date)
    # c = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    #
    # # calculating ongoing progress
    # x = b - a
    # y = c - a
    # p = (y * 100) / x


    finance = models.CharField('Finance', max_length=100)
    finance_step = models.CharField('Finance Step', max_length=100)
    director = models.CharField('Director', max_length=100)
    contact = models.CharField('Contact', max_length=100)
    address = models.CharField('Address', max_length=100)
    website = models.CharField('Website Link', max_length=100)
    description = RichTextUploadingField('Description', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


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


class PortfolioImages(models.Model):
    class Meta:
        verbose_name = 'Pictures'
        verbose_name_plural = 'Pictures'

    # Foreign Key From Portfolio
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, null=True, blank=True)

    portfolio_images = models.IntegerField('ID', null=True, blank=True)
    image = models.FileField(upload_to='Image/Portfolio/%Y/%m/%d')
    photos = ImageSpecField(source='image', processors=[ResizeToFill(800, 800)],
                            format='JPEG', options={'quality': 100})

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


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


class IncubationProgramBenefit(models.Model):
    class Meta:
        verbose_name = "Incubation Program Benefit"
        verbose_name_plural = "Incubation Program Benefit"

    title = models.CharField('Title', max_length=100)
    image = models.FileField('icon', upload_to='Image/Icon/%Y/%m/%d')
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


class IncubationBanner(models.Model):
    class Meta:
        verbose_name = "Incubation Page Hero Banner"
        verbose_name_plural = "Incubation Page Hero Banner"

    title = models.CharField('Title', max_length=200)
    subtitle = models.CharField('Subtitle', max_length=300)
    image = models.FileField('Banner', upload_to='Image/Banner/Incubation/%Y/%m/%d')

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
