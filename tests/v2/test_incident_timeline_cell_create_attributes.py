# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.incident_timeline_cell_markdown_content_type import (
    IncidentTimelineCellMarkdownContentType,
)
from datadog_api_client.v2.model.incident_timeline_cell_markdown_create_attributes import (
    IncidentTimelineCellMarkdownCreateAttributes,
)
from datadog_api_client.v2.model.incident_timeline_cell_markdown_create_attributes_content import (
    IncidentTimelineCellMarkdownCreateAttributesContent,
)

globals()["IncidentTimelineCellMarkdownContentType"] = IncidentTimelineCellMarkdownContentType
globals()["IncidentTimelineCellMarkdownCreateAttributes"] = IncidentTimelineCellMarkdownCreateAttributes
globals()["IncidentTimelineCellMarkdownCreateAttributesContent"] = IncidentTimelineCellMarkdownCreateAttributesContent
from datadog_api_client.v2.model.incident_timeline_cell_create_attributes import IncidentTimelineCellCreateAttributes


class TestIncidentTimelineCellCreateAttributes(unittest.TestCase):
    """IncidentTimelineCellCreateAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentTimelineCellCreateAttributes(self):
        """Test IncidentTimelineCellCreateAttributes"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentTimelineCellCreateAttributes()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
