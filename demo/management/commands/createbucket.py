from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from minio import Minio
from minio.error import BucketAlreadyOwnedByYou

from urllib.parse import urlparse


class Command(BaseCommand):
    help = 'Creates configured bucket for minio servers'

    def handle(self, *args, **options):
        if not settings.AWS_S3_ENDPOINT_URL:
            raise CommandError('This is meant for minio servers')

        url = urlparse(settings.AWS_S3_ENDPOINT_URL)
        minio_host = url.netloc
        secure = url.scheme.endswith('s')

        bucket_name = settings.AWS_STORAGE_BUCKET_NAME

        client = Minio(minio_host,
                       access_key=settings.AWS_ACCESS_KEY_ID,
                       secret_key=settings.AWS_SECRET_ACCESS_KEY,
                       secure=secure)

        try:
            client.make_bucket(bucket_name)
        except BucketAlreadyOwnedByYou:
            pass

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created bucket "{bucket_name}".'
            )
        )
