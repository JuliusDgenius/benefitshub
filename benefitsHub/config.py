"""Configuration module for the application"""
import os
import json


class Config:
    """Configuration class for the application"""
    # Secret key for Flask sessions and security  
    # Load configuration from JSON file
    try:
        with open('/etc/benefitshub_config.json') as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        config = {}

    SECRET_KEY = config.get('SECRET_KEY') or os.getenv('SECRET_KEY', 'dev_secret_key')
    
    # Database URI for SQLAlchemy
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI') or os.getenv('DATABASE_URL')
    
    # Email configuration
    # SMTP server settings for Gmail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465  # Port for SSL
    MAIL_USE_SSL = True  # Use SSL for secure connection
    
    # Email credentials from config file
    MAIL_USERNAME = config.get('EMAIL_USER') or os.getenv('EMAIL_USER')
    MAIL_PASSWORD = config.get('EMAIL_PASS') or os.getenv('EMAIL_PASS')
