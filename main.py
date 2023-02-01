import functions_framework


def greet(message):
    print("hello, ", message)


@functions_framework.cloud_event
def main(cloud_event):
    greet(cloud_event.data)