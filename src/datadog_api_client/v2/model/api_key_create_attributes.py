# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class APIKeyCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
        }

    attribute_map = {
        "name": "name",
    }

    def __init__(self_, name: str, *args, **kwargs):
        """
        Attributes used to create an API Key.

        :param name: Name of the API key.
        :type name: str
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.name = name
