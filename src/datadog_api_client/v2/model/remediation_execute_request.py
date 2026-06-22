# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RemediationExecuteRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "connection_id": (str,),
            "investigation_id": (str,),
        }

    attribute_map = {
        "connection_id": "connection_id",
        "investigation_id": "investigation_id",
    }

    def __init__(self_, connection_id: str, investigation_id: str, **kwargs):
        """
        Request payload for executing a remediation.

        :param connection_id: The Action Platform AWS connection ID to execute through. Must carry the integration_aws connection prefix.
        :type connection_id: str

        :param investigation_id: The ID of the investigation to remediate.
        :type investigation_id: str
        """
        super().__init__(kwargs)

        self_.connection_id = connection_id
        self_.investigation_id = investigation_id
