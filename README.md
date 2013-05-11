A bug report system with Google App Engine
================

This project works on Google App Engine, with Python 2.7 apis.
The android project contained works with android api version 1.6 or above.

1. What is this?
A cloud bug report system, works for android currently.
Idea and android project come from this [blog](http://www.adamrocker.com/blog/288)

2. How does it work? 

i.   Android project is under folder AndroidBugReport.
ii.  This android app will generate an uncaught exception, then save stack infomation into a local file.
iii. When the app run again, it will ask user to upload the local file to Google App Engine.

Developed By
================
Zhenghong Wang - <viennakanon@gmail.com>

License
================
    Copyright 2013 Zhenghong Wang

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
