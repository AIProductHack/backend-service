from minio import Minio


class MinioHelper:
    def __init__(self, host: str, access_key: str, secret_key: str) -> None:
        self.client = Minio(host, access_key, secret_key)

    def upload(self, bucket_name: str, obj_name: str, content: bytes) -> None:
        if not self.client.bucket_exists(bucket_name):
            self.client.make_bucket(bucket_name)
        self.client.put_object(bucket_name, obj_name, content)

    def download(self, bucket_name: str, obj_name: str) -> bytes | None:
        if not self.client.bucket_exists(bucket_name):
            return
        response = self.client.get_object(bucket_name, obj_name)
        if response.status == 200:
            return response.data
