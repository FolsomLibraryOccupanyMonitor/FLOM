# my_project/settings.py
TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        LOGIN_REDIRECT_URL = '/'
    },
]