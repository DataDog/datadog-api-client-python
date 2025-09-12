# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RulesetRespDataAttributesRulesItemsQueryAddition(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "key": (str,),
            "value": (str,),
        }

    attribute_map = {
        "key": "key",
        "value": "value",
    }

    def __init__(self_, key: str, value: str, **kwargs):
        """
        The definition of ``RulesetRespDataAttributesRulesItemsQueryAddition`` object.

        :param key: The ``addition`` ``key``.
        :type key: str

        :param value: The ``addition`` ``value``.
        :type value: str
        """
        super().__init__(kwargs)

        self_.key = key
        self_.value = value
