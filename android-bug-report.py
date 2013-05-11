#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.appengine.ext import db, webapp
from google.appengine.api import mail

import webapp2

class BugData(db.Model):
    device = db.StringProperty()#device name
    model = db.StringProperty()#model name
    sdk = db.StringProperty()#sdk name
    version = db.StringProperty()#version number
    bug = db.TextProperty()#stacktrace
    create = db.DateTimeProperty(auto_now_add=True)

class BugReportHandler(webapp2.RequestHandler):

    def get(self):
        self.get_or_post()

    def post(self):
        self.get_or_post()

    def get_or_post(self):
        dev = self.request.get("dev")
        mod = self.request.get("mod")
        sdk = self.request.get("sdk")
        ver = self.request.get("ver")
        bug = self.request.get("bug")
        
        dev = dev.replace(' ', '       ')

        #insert new element
        db = BugData(device=dev, model=mod, sdk=sdk, version=ver, bug=bug)
        db.put()

        #report with email
        mail.send_mail(sender="itbookman@163.com", to="viennakanon@gmail.com", subject="Bug Report", body=bug)

        self.response.out.write('Success!')

app = webapp2.WSGIApplication([('/android-bug-report', BugReportHandler)],debug=True)
