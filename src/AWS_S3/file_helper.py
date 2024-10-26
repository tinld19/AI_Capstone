import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from io import BytesIO
from PIL import Image

class S3Helper:

   def upload_image_to_s3(self, img: Image.Image, bucket_name: str, s3_file_name: str, content_type: str = 'image/jpeg'):
         """
         Upload an image to an S3 bucket with the specified content type.
         
         :param img: PIL Image object to upload
         :param bucket_name: The name of the S3 bucket
         :param s3_file_name: The S3 object name (the name under which to store the image)
         :param content_type: The MIME type of the file
         :return: None
         """
         s3_client = boto3.client('s3')

         try:
               # Use BytesIO to save the image in memory
               img_buffer = BytesIO()
               img.save(img_buffer, format=content_type.split('/')[1].upper())  # Save image to buffer in the correct format
               img_buffer.seek(0)  # Move to the start of the BytesIO object
               
               # Upload the image from the buffer
               s3_client.upload_fileobj(
                  img_buffer,
                  bucket_name,
                  s3_file_name,
                  ExtraArgs={'ContentType': content_type}
               )
               print(f"Upload Successful: Image has been uploaded to {bucket_name}/{s3_file_name}")
               return True
         except NoCredentialsError:
               print("Credentials not available.")
               return False
         except Exception as e:
               print(f"An error occurred: {e}")
               return False


   def read_image_from_s3(self, bucket_name, s3_file_name):
      """
      Read an image from an S3 bucket and return it as a PIL Image object.
      
      :param bucket_name: The name of the S3 bucket
      :param s3_file_name: The S3 object name (the name of the file in S3)
      :return: PIL Image object
      """
      s3_client = boto3.client('s3')

      try:
         # Use BytesIO to create a file-like object in memory
         img_data = BytesIO()
         s3_client.download_fileobj(bucket_name, s3_file_name, img_data)
         img_data.seek(0)  # Move to the start of the BytesIO object
         img = Image.open(img_data)  # Read the image
         return img
      except NoCredentialsError:
         print("Credentials not available.")
      except ClientError as e:
         print(f"Failed to read image from S3: {e}")
      except Exception as e:
         print(f"An error occurred: {e}")
         
         
   def download_pdf_from_s3(self, bucket_name: str, s3_file_name: str, local_path: str):
      """
      Download a PDF file from an S3 bucket and save it to a specified local path.
      
      :param bucket_name: The name of the S3 bucket
      :param s3_file_name: The S3 object name (the name of the PDF file in S3)
      :param local_path: Local path where the PDF file will be saved
      :return: The path of the downloaded PDF file
      """
      s3_client = boto3.client('s3')

      try:
         s3_client.download_file(bucket_name, s3_file_name, local_path)
         print(f"Downloaded: {s3_file_name} from bucket: {bucket_name} to {local_path}")
         return local_path
      except NoCredentialsError:
         print("Credentials not available.")
      except ClientError as e:
         print(f"Failed to download PDF from S3: {e}")
      except Exception as e:
         print(f"An error occurred: {e}")