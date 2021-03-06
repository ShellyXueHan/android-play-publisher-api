#!/usr/bin/env python
import argparse
import sys
import traceback
import json
from apiclient.discovery import build
import httplib2
from oauth2client import client
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.errors import HttpError

sys.tracebacklimit = 0

"""
1. Lists all the apks for a given app -> getListings()
2. Uploads an apk to the alpha track -> 
  (need incremental version code from gradle https://medium.com/@prathanbomb/tips-auto-increment-versioncode-of-android-using-gradle-dba0425af97c)
3. Update app listings -> 
"""

__version__ = '0.0.1'

class GoogleAPIService(object):
  def __init__(self, email, key, package_name):
    # setup Google API Service mandatory parameters:
    self.package_name = package_name

    # compose credential, (scopes always the same):
    credentials = ServiceAccountCredentials.from_p12_keyfile(
      email,
      key,
      scopes='https://www.googleapis.com/auth/androidpublisher')
    try:
      # build service connection:
      http = httplib2.Http()
      http = credentials.authorize(http)
      self.service = build('androidpublisher', 'v3', http=http)

      # setup Edit request, use ID for the Edit in actions:
      edit_request_result = self.service.edits().insert(
          body={},
          packageName=package_name).execute()
      self.edit_id = edit_request_result['id']

    except Exception as e:
      ErrorHandler(e)



# ------------------API Methods: ------------------ 
  def getListings(self):
    apks_result = self.service.edits().apks().list(
        editId=self.edit_id,
        packageName=self.package_name).execute()

    for apk in apks_result['apks']:
      print 'versionCode: %s, binary.sha1: %s' % (apk['versionCode'], apk['binary']['sha1'])

  def uploadAPK(self, apk_file, track, track_name):
    apk_response = self.service.edits().apks().upload(
        editId=self.edit_id,
        packageName=self.package_name,
        media_body=apk_file).execute()

    print 'Version code %d has been uploaded' % apk_response['versionCode']

    track_response = self.service.edits().tracks().update(
        editId=self.edit_id,
        track=track,
        packageName=self.package_name,
        body={u'releases': [{
            u'name': track_name,
            u'versionCodes': [apk_response['versionCode']],
            u'status': u'completed',
        }]}).execute()

    print 'Track %s is set with releases: %s' % (track_response['track'], str(track_response['releases']))


  def commitEdit(self):
    commit_request = self.service.edits().commit(
        editId=self.edit_id,
        packageName=self.package_name).execute()

    print 'Edit "%s" has been committed' % (commit_request['id'])

# ------------------General Methods: ------------------ 
def ErrorHandler(err):
  if isinstance(err, client.HttpAccessTokenRefreshError):
    print('\n*-------------Http Access Token Refresh Error:-------------')
    print ('The credentials have been revoked or expired, please re-run the '
           'application to re-authorize')
  
  elif isinstance(err, HttpError):
    errormsg = str(err.content)
    err_json = json.loads(errormsg)
    err = err_json['error']['message']
    print('\n*-------------HTTP Error:----------------------------------')
  
  else:
    err=str(err)
  
  raise Exception(err)
