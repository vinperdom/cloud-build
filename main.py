import functions_framework


def greet(message):
    print("hello, ", message)


@functions_framework.cloud_event
def my_cloudevent_function(cloud_event):
    greet(cloud_event.data)