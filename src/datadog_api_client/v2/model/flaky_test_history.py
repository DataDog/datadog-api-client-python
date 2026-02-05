# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class FlakyTestHistory(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "commit_sha": (str,),
            "status": (str,),
            "timestamp": (int,),
        }

    attribute_map = {
        "commit_sha": "commit_sha",
        "status": "status",
        "timestamp": "timestamp",
    }

    def __init__(self_, commit_sha: str, status: str, timestamp: int, **kwargs):
        """
        A single history entry representing a status change for a flaky test.

        :param commit_sha: The commit SHA associated with this status change. Will be an empty string if the commit SHA is not available.
        :type commit_sha: str

        :param status: The test status at this point in history.
        :type status: str

        :param timestamp: Unix timestamp in milliseconds when this status change occurred.
        :type timestamp: int
        """
        super().__init__(kwargs)

        self_.commit_sha = commit_sha
        self_.status = status
        self_.timestamp = timestamp
