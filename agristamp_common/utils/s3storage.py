import os
import logging
from uuid import uuid4
import boto3
from botocore.exceptions import ClientError
from tempfile import NamedTemporaryFile

AWS_REGION = os.getenv('AWS_DEFAULT_REGION')

s3_client = boto3.client('s3', region_name=AWS_REGION)

def create_presigned_url(bucket_name, object_name, expiration=3600):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a presigned URL for the S3 object

    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response

def upload_file(file_path, folder, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_path: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_path is used
    :return: True if file was uploaded, else False
    """

    _, file_extension = os.path.splitext(file_path)
    
    # format file object name = folder + uuid hash + extension
    if object_name is None:
        object_name = f"{folder}/{str(uuid4())}{file_extension}"

    # Upload the file

    try:
        response = s3_client.upload_file(file_path, 
                                         bucket, 
                                         object_name
                                        )

    except ClientError as e:
        logging.error(e)
        return False

    s3_url = f"s3://{bucket}/{object_name}"
    object_url = f"https://{bucket}.s3-{AWS_REGION}.amazonaws.com/{object_name}"
    presigned_url = create_presigned_url(bucket, object_name)

    return_obj = {
        's3_url': s3_url,
        'object_url': object_url,
        'presigned_url': presigned_url,
    }

    return return_obj


def upload_fastapi_uploadfile(file, folder, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_path: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_path is used
    :return: True if file was uploaded, else False
    """

    # Create Temp File to Upload
    _, file_extension = os.path.splitext(file.filename)

    temp_file = NamedTemporaryFile(suffix=file_extension)
    temp_file.write(file.file.read())
    temp_file.seek(0)

    file_path = temp_file.name

    # format file object name = folder + uuid hash + extension
    if object_name is None:
        object_name = f"{folder}/{str(uuid4())}{file_extension}"

    # Upload the file

    try:
        response = s3_client.upload_file(file_path,
                                         bucket,
                                         object_name
                                        )

    except ClientError as e:
        logging.error(e)
        return False

    s3_url = f"s3://{bucket}/{object_name}"
    object_url = f"https://{bucket}.s3-{AWS_REGION}.amazonaws.com/{object_name}"
    presigned_url = create_presigned_url(bucket, object_name)
    

    return_obj = {
        's3_url': s3_url,
        'object_url': object_url,
        'presigned_url': presigned_url,
    }

    return return_obj
