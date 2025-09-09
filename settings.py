STATIC_URL = '/static/'

# For development only
STATICFILES_DIRS = [BASE_DIR / "static"]

TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'tryon/templates'],  # your template folder
        ...
    }
]
