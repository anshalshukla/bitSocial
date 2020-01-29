SECRET_KEY = "l!%9humy547#m49&(x&m48w5o&bzb=ggbv=t1nl3ff_9uv&a1="

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = (
    "640757555562-e79eq6482g5okcmvgbg0cd38gmdbeng8.apps.googleusercontent.com"
)
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "zx_0OpegIfgXOwjTf2Bt33_o"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_HOST_USER = "apikey"
EMAIL_HOST_PASSWORD = (
    "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"
)
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = "shukla.anshal85@gmail.com"
ACCOUNT_EMAIL_SUBJECT_PREFIX = "This is a automatically generated email."
DB_NAME = "blog_data"
DB_USER = "root"
DB_PASSWORD = "Anshal@2000"
