# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import synthetics_ssl_certificate_issuer
except ImportError:
    synthetics_ssl_certificate_issuer = sys.modules[
        'datadog_api_client.v1.model.synthetics_ssl_certificate_issuer']
try:
    from datadog_api_client.v1.model import synthetics_ssl_certificate_subject
except ImportError:
    synthetics_ssl_certificate_subject = sys.modules[
        'datadog_api_client.v1.model.synthetics_ssl_certificate_subject']
from datadog_api_client.v1.model.synthetics_ssl_certificate import SyntheticsSSLCertificate


class TestSyntheticsSSLCertificate(unittest.TestCase):
    """SyntheticsSSLCertificate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsSSLCertificate(self):
        """Test SyntheticsSSLCertificate"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsSSLCertificate()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
