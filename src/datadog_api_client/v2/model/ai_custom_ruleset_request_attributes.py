# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AiCustomRulesetRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "name": (str,),
            "short_description": (str,),
        }

    attribute_map = {
        "description": "description",
        "name": "name",
        "short_description": "short_description",
    }

    def __init__(self_, description: str, name: str, short_description: str, **kwargs):
        """
        Attributes for creating an AI custom ruleset.

        :param description: Base64-encoded full description of the ruleset.
        :type description: str

        :param name: The ruleset name.
        :type name: str

        :param short_description: Base64-encoded short description of the ruleset.
        :type short_description: str
        """
        super().__init__(kwargs)

        self_.description = description
        self_.name = name
        self_.short_description = short_description
