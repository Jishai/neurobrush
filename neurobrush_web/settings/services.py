from os import environ


#S3
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#TODO: env vars
AWS_ACCESS_KEY_ID ='AKIAJB7WPKNNL2AMBH5A' # os.environ.get('AWS_ACCESS_KEY_ID') #
AWS_SECRET_ACCESS_KEY =  'Y8wglUGUJNeEfkZNYZDNMpFKlzAmmsA9LnBq1Dx' #os.environ.get('AWS_SECRET_ACCESS_KEY') #
AWS_STORAGE_BUCKET_NAME = 'neurobrush'
#AWS_CALLING_FORMAT = ''
#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_QUERYSTRING_AUTH = False
AWS_PRELOAD_METADATA = True
AWS_IS_GZIPPED = True
AWS_S3_SECURE_URLS = False
AWS_HEADERS = {
    'Cache-Control': 'public, max-age=86400',
}
