# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IntakeAPIKeyAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "api_key": (str,),
            "org_id": (int,),
        }

    attribute_map = {
        "api_key": "api_key",
        "org_id": "org_id",
    }

    def __init__(self_, api_key: str, org_id: int, **kwargs):
        """
        Attributes of an intake API key returned after successful authentication.

        :param api_key: The Datadog API key the workload can use to send telemetry.
        :type api_key: str

        :param org_id: The numeric ID of the Datadog organization the API key belongs to.
        :type org_id: int
        """
        super().__init__(kwargs)

        self_.api_key = api_key
        self_.org_id = org_id
