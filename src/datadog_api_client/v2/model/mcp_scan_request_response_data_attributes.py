# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class McpScanRequestResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "job_id": (str,),
        }

    attribute_map = {
        "job_id": "job_id",
    }

    def __init__(self_, job_id: str, **kwargs):
        """
        The attributes returned when a scan request has been accepted, containing the job identifier used to poll for results.

        :param job_id: The job identifier assigned to the scan, used to retrieve the scan result.
        :type job_id: str
        """
        super().__init__(kwargs)

        self_.job_id = job_id
