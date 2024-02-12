from socket import *
import json
from instagram import find_profile

serverPort = 8080

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    username = connectionSocket.recv(1024).decode()
    if username == 'exit':
        break
    try:
        # Try to find the profile
        profile = find_profile(username)

        # If the profile is found, create a success response
        list_of_content = {
            'status': {
                'code': 200,
                'phrase': 'OK',
                'message': 'Profile found successfully.'
            },
            'data': {
                'username': profile.username,
                'userid': profile.userid,
                'mediacount': profile.mediacount,
                'followers': profile.followers,
                'followees': profile.followees,
                'biography': profile.biography
            }
        }
        data = json.dumps(list_of_content, indent=2)
    except Exception as e:
        data_error = {
            'status': {
                'code': 404,
                'phrase': 'Not Found Profile',
                'message': str(e)
            },
            'data': None
        } 
        data = json.dumps(data_error, indent=2)
    connectionSocket.send(data.encode())
    connectionSocket.close()
serverSocket.close()