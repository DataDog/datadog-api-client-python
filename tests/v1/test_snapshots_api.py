# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.snapshots_api import SnapshotsApi  # noqa: E501


class TestSnapshotsApi(unittest.TestCase):
    """SnapshotsApi unit test stubs"""

    def setUp(self):
        self.api = SnapshotsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_graph_snapshot(self):
        """Test case for get_graph_snapshot

        Take graph snapshots  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
