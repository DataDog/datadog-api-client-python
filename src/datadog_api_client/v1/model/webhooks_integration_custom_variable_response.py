# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class WebhooksIntegrationCustomVariableResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "is_secret": (bool,),
            "name": (str,),
            "value": (str,),
        }

    attribute_map = {
        "is_secret": "is_secret",
        "name": "name",
        "value": "value",
    }

    def __init__(self, is_secret, name, *args, **kwargs):
        """
        Custom variable for Webhook integration.

        :param is_secret: Make custom variable is secret or not.
            If the custom variable is secret, the value is not returned in the response payload.
        :type is_secret: bool

        :param name: The name of the variable. It corresponds with ``<CUSTOM_VARIABLE_NAME>``. It must only contains upper-case characters, integers or underscores.
        :type name: str

        :param value: Value of the custom variable. It won't be returned if the variable is secret.
        :type value: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.is_secret = is_secret
        self.name = name

    @classmethod
    def _from_openapi_data(cls, is_secret, name, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(WebhooksIntegrationCustomVariableResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.is_secret = is_secret
        self.name = name
        return self
