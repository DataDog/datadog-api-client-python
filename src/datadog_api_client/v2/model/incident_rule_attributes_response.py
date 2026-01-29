# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class IncidentRuleAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "modified_at": (datetime,),
            "name": (str,),
        }

    attribute_map = {
        "created_at": "createdAt",
        "modified_at": "modifiedAt",
        "name": "name",
    }

    def __init__(self_, created_at: datetime, modified_at: datetime, name: str, **kwargs):
        """


        :param created_at: When the rule was created.
        :type created_at: datetime

        :param modified_at: When the rule was last modified.
        :type modified_at: datetime

        :param name: The name of the rule.
        :type name: str
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.modified_at = modified_at
        self_.name = name
