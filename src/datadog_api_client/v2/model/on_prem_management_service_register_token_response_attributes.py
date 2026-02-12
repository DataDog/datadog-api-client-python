# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class OnPremManagementServiceRegisterTokenResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "token_string": (str,),
        }

    attribute_map = {
        "token_string": "token_string",
    }

    def __init__(self_, token_string: str, **kwargs):
        """
        Attributes for the registered token.

        :param token_string: The token string.
        :type token_string: str
        """
        super().__init__(kwargs)

        self_.token_string = token_string
