# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ValidateV2Attributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "api_key_id": (str,),
            "api_key_scopes": ([str],),
            "valid": (bool,),
        }

    attribute_map = {
        "api_key_id": "api_key_id",
        "api_key_scopes": "api_key_scopes",
        "valid": "valid",
    }

    def __init__(self_, api_key_id: str, api_key_scopes: List[str], valid: bool, **kwargs):
        """
        Attributes of the API key validation response.

        :param api_key_id: The UUID of the API key.
        :type api_key_id: str

        :param api_key_scopes: List of scope names associated with the API key.
        :type api_key_scopes: [str]

        :param valid: Whether the API key is valid.
        :type valid: bool
        """
        super().__init__(kwargs)

        self_.api_key_id = api_key_id
        self_.api_key_scopes = api_key_scopes
        self_.valid = valid
