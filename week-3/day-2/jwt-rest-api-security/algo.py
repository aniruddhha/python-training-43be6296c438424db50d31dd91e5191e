'''
Algorithm for securing REST Api using JWT Tokens

1. Client will retrive the jwt token from flask app
2. Client will pass JWT token in request header; for each request
3. Flask will retrive JWT token from request headers
4. Flask will verify the signature each time and check token validity
5. If token is valid then and only then requested operation will be performed
6. Else Unauthorized 401 error will be sent 
'''

import jwt
from jwt.exceptions import InvalidAlgorithmError, InvalidSignatureError

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.S2ZL7D-D3VeduQ44Cy2qLRFxHV43gRGSZtlfJ2MJ57g'

try:
    dt = jwt.decode(token, "123456789", algorithms=["HS256"])
    print(dt)
except InvalidSignatureError:
    print('Signature Did not Match')
except InvalidAlgorithmError:
    print('Algorithm Did not Match')
