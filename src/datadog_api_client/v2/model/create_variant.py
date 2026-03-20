# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CreateVariant(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "key": (str,),
            "name": (str,),
            "value": (str,),
        }

    attribute_map = {
        "key": "key",
        "name": "name",
        "value": "value",
    }

    def __init__(self_, key: str, name: str, value: str, **kwargs):
        """
        Request to create a variant.

        :param key: The unique key of the variant.
        :type key: str

        :param name: The name of the variant.
        :type name: str

        :param value: The value of the variant as a string.
        :type value: str
        """
        super().__init__(kwargs)

        self_.key = key
        self_.name = name
        self_.value = value
