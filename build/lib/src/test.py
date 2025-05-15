

from google.cloud import storage
from config.paths_config import *
GOOGLE_AUTH = "consummate-gift-458313-s6-d0f3981b8d85.json"
print(GOOGLE_AUTH)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] =  GOOGLE_AUTH
client = storage.Client()
bucket = client.bucket("my_bucket1999")
blob = bucket.blob("Hotel_Reservations.csv")
blob.download_to_filename(RAW_FILE_PATH)
