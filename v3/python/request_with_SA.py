
import argparse
from googleDeploymentAPI import GoogleAPIService

# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument('package_name',
                       help='The package name. Example: com.android.sample')
argparser.add_argument('apk_file',
                       nargs='?',
                       default='test.apk',
                       help='The path to the APK file to upload.')


SERVICE_ACCOUNT_EMAIL = ('ENTER_YOUR_SERVICE_ACCOUNT_EMAIL_HERE@developer.gserviceaccount.com')
PACKAGE_NAME = ('The package name. Example: com.android.sample')
KEY_PATH = ('Load the key in PKCS 12 format that you downloaded from the Google APIs Console when you created your Service account.')
TRACK = 'alpha'  # Can be 'alpha', beta', 'production' or 'rollout'


def main(argv):
  a=GoogleAPIService(SERVICE_ACCOUNT_EMAIL, KEY_PATH, PACKAGE_NAME)
  a.getListings()
  a.uploadAPK(self, apk_file, track, track_name)
  a.commitEdit()

if __name__ == '__main__':
  main()
