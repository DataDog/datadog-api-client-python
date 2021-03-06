# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.logs_attribute_remapper_type import LogsAttributeRemapperType
from datadog_api_client.v1.model.target_format_type import TargetFormatType

globals()["LogsAttributeRemapperType"] = LogsAttributeRemapperType
globals()["TargetFormatType"] = TargetFormatType
from datadog_api_client.v1.model.logs_attribute_remapper import LogsAttributeRemapper


class TestLogsAttributeRemapper(unittest.TestCase):
    """LogsAttributeRemapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsAttributeRemapper(self):
        """Test LogsAttributeRemapper"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsAttributeRemapper()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
