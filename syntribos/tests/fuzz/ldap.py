"""
Copyright 2015 Rackspace

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from syntribos.tests.fuzz import base_fuzz


class LDAPInjectionBody(base_fuzz.BaseFuzzTestCase):
    test_name = "LDAP_INJECTION_BODY"
    test_type = "data"
    data_key = "ldap.txt"


class LDAPInjectionParams(LDAPInjectionBody):
    test_name = "LDAP_INJECTION_PARAMS"
    test_type = "params"


class LDAPInjectionHeaders(LDAPInjectionBody):
    test_name = "LDAP_INJECTION_HEADERS"
    test_type = "headers"


class LDAPInjectionURL(LDAPInjectionBody):
    test_name = "LDAP_INJECTION_URL"
    test_type = "url"
    url_var = "FUZZ"
