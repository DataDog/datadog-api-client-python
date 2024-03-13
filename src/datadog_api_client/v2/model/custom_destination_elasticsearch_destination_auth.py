# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CustomDestinationElasticsearchDestinationAuth(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "password": (str,),
            "username": (str,),
        }

    attribute_map = {
        "password": "password",
        "username": "username",
    }

    def __init__(self_, password: str, username: str, **kwargs):
        """
        Basic access authentication.

        :param password: The password of the authentication. This field is not returned by the API.
        :type password: str

        :param username: The username of the authentication. This field is not returned by the API.
        :type username: str
        """
        super().__init__(kwargs)

        self_.password = password
        self_.username = username
