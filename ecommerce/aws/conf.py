import datetime

AWS_GROUP_NAME = "mhs_eCommerce_Group"
AWS_USERNAME = "mhs-ecommerce-user"

AWS_ACCESS_KEY_ID = "AKIAU6GDZ7WU4JRN6EV7"
AWS_SECRET_ACCESS_KEY = "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"
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

DEFAULT_FILE_STORAGE = 'ecommerce.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'ecommerce.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'mhs-ecommerce'
S3DIRECT_REGION = 'ap-south-1'
AWS_S3_SIGNATURE_VERSION = "s3v4" #Prachiadded
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = { 
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}
