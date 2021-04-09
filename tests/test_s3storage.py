from agristamp_common.utils.s3storage import upload_file

class TestS3Storage():

   def test_upload_file(self):

      return_obj = upload_file(file_path='/tmp/arquivo_teste.txt', folder='mapas', bucket='base-service')

      assert return_obj