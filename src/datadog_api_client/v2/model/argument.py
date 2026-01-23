# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class Argument(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "name": (str,),
        }

    attribute_map = {
        "description": "description",
        "name": "name",
    }

    def __init__(self_, description: str, name: str, **kwargs):
        """


        :param description: Base64-encoded argument description
        :type description: str

        :param name: Base64-encoded argument name
        :type name: str
        """
        super().__init__(kwargs)

        self_.description = description
        self_.name = name
