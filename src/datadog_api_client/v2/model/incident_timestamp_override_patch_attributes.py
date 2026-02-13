# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class IncidentTimestampOverridePatchAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "timestamp_value": (datetime,),
        }

    attribute_map = {
        "timestamp_value": "timestamp_value",
    }

    def __init__(self_, timestamp_value: datetime, **kwargs):
        """
        Attributes for patching an incident timestamp override.

        :param timestamp_value: The timestamp value for the override.
        :type timestamp_value: datetime
        """
        super().__init__(kwargs)

        self_.timestamp_value = timestamp_value
