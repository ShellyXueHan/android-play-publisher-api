
# WIP - Working on the python part to turn scripting into simple cli tool

## Google Play Developer Publishing API samples

A collection of command-line samples for the Play Developer Publishing API.

## Installation

1. Download Google APIs Client Library for Python (google-api-python-client):
  https://code.google.com/p/google-api-python-client/

  or use pip:

  ```bash
  $ pip install google-api-python-client
  ```

2. Make sure you can import the client library:

  ```bash
  $ python
  >>> import apiclient
  >>>
  ```

3. Install the project as a library:

  ```bash
  $ python setup.py install --user
  ```

4. Fill in deployment information of the app in the `request_with_SA.py` file:

  4.1 API authentication - as specified in OAth2 section below
  4.2 Application package information and release information
  4.3 Deployment store listing information

5. Call the API functions in main()


## To make API request using OAuth2 - Service accounts:

1. In Google Play Console, create a Service Account with P12 key

2. Grant access to the service account, download the key file and save as `key.p12`.

3. Go to the `request_with_SA.py` file and enter the account related information

4. Try to get listings of an application from Play Store (Please note that you will not be able to manage an application via scripting if it does not exist in Play Store yet!)


## Making API request:

All the modification to the app is contained in an Edit
( https://developers.google.com/android-publisher/api-ref/edits )


Create an Edit and then make changes, then commit the Edit.