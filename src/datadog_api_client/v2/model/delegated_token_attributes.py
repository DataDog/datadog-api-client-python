# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class DelegatedTokenAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "access_token": (str,),
            "expires": (datetime,),
        }

    attribute_map = {
        "access_token": "access_token",
        "expires": "expires",
    }

    def __init__(self_, access_token: str, expires: datetime, **kwargs):
        """
        Attributes of a delegated token.

        :param access_token: A short-lived JWT representing the authenticated Datadog user. Pass this as a bearer token in subsequent API calls.
        :type access_token: str

        :param expires: The expiry time of the token.
        :type expires: datetime
        """
        super().__init__(kwargs)

        self_.access_token = access_token
        self_.expires = expires
