# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityAgentInvestigationCount(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "count": (int,),
            "value": (str,),
        }

    attribute_map = {
        "count": "count",
        "value": "value",
    }

    def __init__(self_, count: int, value: str, **kwargs):
        """
        One value of the counted field and how many completed investigations have it.

        :param count: Number of completed investigations with this value.
        :type count: int

        :param value: A value of the counted field.
        :type value: str
        """
        super().__init__(kwargs)

        self_.count = count
        self_.value = value
