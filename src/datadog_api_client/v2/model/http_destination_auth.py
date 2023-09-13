# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class HttpDestinationAuth(ModelComposed):
    def __init__(self, **kwargs):
        """
        The authentication method used for HTTP destinations.

        :param password: The password to use for the HTTP request.
        :type password: str

        :param type: The HTTP destination basic auth type.
        :type type: HttpDestinationBasicAuthType

        :param username: The username to use for the HTTP request.
        :type username: str

        :param header_name: The name of the header to use for the HTTP request.
        :type header_name: str

        :param header_value: The value of the header to use for the HTTP request.
        :type header_value: str
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.http_destination_basic_auth import HttpDestinationBasicAuth
        from datadog_api_client.v2.model.http_destination_custom_header_auth import HttpDestinationCustomHeaderAuth

        return {
            "oneOf": [
                HttpDestinationBasicAuth,
                HttpDestinationCustomHeaderAuth,
            ],
        }
