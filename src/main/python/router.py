
#!/usr/bin/python

# Copyright KOLIBERO under one or more contributor license agreements.  
# KOLIBERO licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask, jsonify, request, Response, abort
from functools import wraps

import json
import time
import requests
import os
from snowplow_tracker import Subject, Emitter, Tracker, SelfDescribingJson

app = Flask(__name__)

# snowplow
@app.route('/api/v1.0/snowplow', methods=['POST'])
def snowplow():
    indata = request.json

    e = Emitter(os.environ["SP_COLLECTOR_URI"],protocol=os.environ["SP_COLLECTOR_PROTOCOL"],port=os.environ["SP_COLLECTOR_PORT"],method=os.environ["SP_COLLECTOR_METHOD"])
    t = Tracker(emitters=e,namespace="cf",app_id=str(indata["i_app_id"]),encode_base64=True)
   
    s1 = Subject()
    s1.set_platform("web")
    s1.set_user_id(str(indata.get("i_user_id")))
    s1.set_lang(str(indata.get("i_language")))
    s1.set_ip_address(str(indata.get("i_ip")))
    s1.set_useragent(str(indata.get("i_user_agent")))

    t.set_subject(s1)

    t.track_self_describing_event(SelfDescribingJson("iglu:com.snowplowanalytics.snowplow/unstruct_event/jsonschema/1-0-0",{
      "data":{
        "data": indata
      },
      "schema": "iglu:com.rbox24/"+str(indata["i_app_id"])+"/jsonschema/1-0-0"
    }))

    t.flush()   

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
