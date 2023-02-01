import functions_framework


def say(message):
    print(message)


@functions_framework.cloud_event
def my_cloudevent_function(cloud_event):
    say("hello!")
