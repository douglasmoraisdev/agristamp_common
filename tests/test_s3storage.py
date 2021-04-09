from agristamp_common.utils.s3storage import upload_file, upload_bytes

class TestS3Storage():

   def test_upload_file(self):

      return_obj = upload_file(file_path='/tmp/arquivo_teste.txt', folder='mapas', bucket='base-service')

      assert return_obj

   def test_upload_bytes(self):

      return_obj = upload_bytes(file_bytes=b'algum arquivo em bytes', file_extension='.txt', folder='mapas', bucket='base-service')

      assert return_obj
