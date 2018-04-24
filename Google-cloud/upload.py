import os

import google.cloud.storage

# Create a storage client.
storage_client = google.cloud.storage.Client()

# TODO (Developer): Replace this with your Cloud Storage bucket name.
bucket_name = 'high-frequency-data'
bucket = storage_client.get_bucket(bucket_name)

# TODO (Developer): Replace this with the name of the local file to upload.
source_file_name = 'high_low_freq_peakedspectrum_table_cleaned'
blob = bucket.blob(os.path.basename(source_file_name))

# Upload the local file to Cloud Storage.
blob.upload_from_filename(source_file_name)

print('File {} uploaded to {}.'.format(source_file_name, bucket))
