from mongoengine import Document ,fields,connect
connect('mongotask')
import datetime

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Blog(Document):
    title = fields.StringField(max_length=50)
    image = fields.ImageField(thumbnail_size = (150,150,False))
    content = fields.StringField(max_length=None)
    author = fields.StringField()
    ddate_modified= fields.DateTimeField(default=datetime.datetime.utcnow)
    status = fields.IntField(choices=STATUS, default=1)

    # meta = {'allow_inheritance': True}
    class Meta:
        ordering = ['-created_on']

