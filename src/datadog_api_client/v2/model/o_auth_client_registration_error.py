# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class OAuthClientRegistrationError(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "error": (str,),
            "error_description": (str,),
        }

    attribute_map = {
        "error": "error",
        "error_description": "error_description",
    }

    def __init__(self_, error: str, error_description: str, **kwargs):
        """
        Error payload returned by OAuth2 dynamic client registration as defined by RFC 7591.

        :param error: Single ASCII error code per RFC 7591, such as ``invalid_request`` or ``invalid_client_metadata``.
        :type error: str

        :param error_description: Human-readable description of the error.
        :type error_description: str
        """
        super().__init__(kwargs)

        self_.error = error
        self_.error_description = error_description
