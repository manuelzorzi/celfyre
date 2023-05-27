import logging
from django.core.mail import EmailMultiAlternatives, BadHeaderError
from smtplib import SMTPException

# Create or get the logger
logger = logging.getLogger(__name__)

def send_story_email(goal, habit, story, audio_url, email):
    subject = 'Your motivational story from Celfyre'
    from_email = 'info@celfyre.com'  # Replace with your actual email
    to = [email]
    text_content = f'Here is the story you requested: \n\n{goal}\n\n,\n\n{habit}\n\n,\n\n{story}\n\nListen to the audio version here: {audio_url}'

    # Create the HTML version of your message
    html_content = f"""
    <html>
      <body>
        Here is the story you requested: <br><br>
        {goal} <br><br>
        {habit} <br><br>
        {story} <br><br>
        Listen to the audio version <a href="{audio_url}">here</a>.
      </body>
    </html>
    """

    # If you want to use both text and HTML content, you'll need to create an instance of EmailMultiAlternatives.
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")

    try:
        msg.send()
        logger.info(f"Email sent successfully to {email}")
    except BadHeaderError:
        logger.exception(f"Invalid header found in email to {email}")
    except SMTPException:
        logger.exception(f"SMTP error occurred when sending email to {email}")
    except Exception as e:
        logger.exception(f"An unexpected error occurred when sending email to {email}: {e}")
