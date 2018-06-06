
from googleDeploymentAPI import GoogleAPIService

SERVICE_ACCOUNT_EMAIL = ('ENTER_YOUR_SERVICE_ACCOUNT_EMAIL_HERE@developer.gserviceaccount.com')
PACKAGE_NAME = ('The package name. Example: com.android.sample')
KEY_PATH = ('Load the key in PKCS 12 format that you downloaded from the Google APIs Console when you created your Service account.')

def main():
  a=GoogleAPIService(SERVICE_ACCOUNT_EMAIL, KEY_PATH, PACKAGE_NAME)
  a.getListings()

if __name__ == '__main__':
  main()
