from storages.backends.s3boto import S3BotoStorage

StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static')
MediaRootS3BotoStorage  = lambda: S3BotoStorage(location='media')


def jwt_response_payload_handler(token, user=None, *args, **kwargs):
    return {
        "token": token,
        "user": str(user.username),
    }
# 만약에 결제 모듈을 붙인다면, 여기다가 token을 처음로그인 할 때 받아내야 한다.