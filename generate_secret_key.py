"""
Generate a secure Django SECRET_KEY
Run this script to generate a random secret key for production
"""

from django.core.management.utils import get_random_secret_key

print("=" * 50)
print("DJANGO SECRET KEY GENERATOR")
print("=" * 50)
print("\nYour new SECRET_KEY:")
print("-" * 50)
print(get_random_secret_key())
print("-" * 50)
print("\n⚠️  IMPORTANT:")
print("1. Copy this key to your .env file")
print("2. Add it to Render environment variables")
print("3. Never commit this key to Git!")
print("4. Keep it secret and secure")
print("=" * 50)
