# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.http_basic_auth_type import HTTPBasicAuthType


class HTTPBasicAuth(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.http_basic_auth_type import HTTPBasicAuthType

        return {
            "password": (str,),
            "type": (HTTPBasicAuthType,),
            "username": (str,),
        }

    attribute_map = {
        "password": "password",
        "type": "type",
        "username": "username",
    }

    def __init__(self_, password: str, type: HTTPBasicAuthType, username: str, **kwargs):
        """
        The definition of the ``HTTPBasicAuth`` object.

        :param password: Password used for authentication. Saved in a secret store
        :type password: str

        :param type: The definition of the ``HTTPBasicAuth`` object.
        :type type: HTTPBasicAuthType

        :param username: Username used for authentication.
        :type username: str
        """
        super().__init__(kwargs)

        self_.password = password
        self_.type = type
        self_.username = username
