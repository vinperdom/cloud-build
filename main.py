import functions_framework


def greet(name):
    print("hello, ", name)


@functions_framework.cloud_event
def main(cloud_event):
    greet(cloud_event.data['name'])
