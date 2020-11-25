from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

from followers.models import Follow


def send_ideas_to_followers(user, idea):
    followers = Follow.objects.filter(followed=user)
    for follower in followers:
        send_email_to_follower(follower, idea)


def send_email_to_follower(follower, idea):
    subject = "New publication from " + follower
    message = "The user " + follower + " has published this idea " + idea
    from_email = "admin@example.com"
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, follower.email)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')
