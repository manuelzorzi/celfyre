import dramatiq
import os
import django
from .gtp3 import generate_story
from .email import send_story_email
from .audiostack import generate_audio

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celfyre.settings')
django.setup()


@dramatiq.actor
def generate_and_send_story(goal, habit, email):
    story = generate_story(habit, goal)
    audio_url = generate_audio(story)
    send_story_email(goal, habit, story, audio_url, email)
