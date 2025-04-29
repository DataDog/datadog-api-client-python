# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ObservabilityPipelineSumoLogicDestinationHeaderCustomFieldsItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "value": (str,),
        }

    attribute_map = {
        "name": "name",
        "value": "value",
    }

    def __init__(self_, name: str, value: str, **kwargs):
        """
        Single key-value pair used as a custom log header for Sumo Logic.

        :param name: The header field name.
        :type name: str

        :param value: The header field value.
        :type value: str
        """
        super().__init__(kwargs)

        self_.name = name
        self_.value = value
