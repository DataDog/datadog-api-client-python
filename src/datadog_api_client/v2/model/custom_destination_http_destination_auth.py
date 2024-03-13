# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class CustomDestinationHttpDestinationAuth(ModelComposed):
    def __init__(self, **kwargs):
        """
        Authentication method of the HTTP requests.

        :param password: The password of the authentication. This field is not returned by the API.
        :type password: str

        :param type: Type of the basic access authentication.
        :type type: CustomDestinationHttpDestinationAuthBasicType

        :param username: The username of the authentication. This field is not returned by the API.
        :type username: str

        :param header_name: The header name of the authentication.
        :type header_name: str

        :param header_value: The header value of the authentication. This field is not returned by the API.
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
        from datadog_api_client.v2.model.custom_destination_http_destination_auth_basic import (
            CustomDestinationHttpDestinationAuthBasic,
        )
        from datadog_api_client.v2.model.custom_destination_http_destination_auth_custom_header import (
            CustomDestinationHttpDestinationAuthCustomHeader,
        )

        return {
            "oneOf": [
                CustomDestinationHttpDestinationAuthBasic,
                CustomDestinationHttpDestinationAuthCustomHeader,
            ],
        }
