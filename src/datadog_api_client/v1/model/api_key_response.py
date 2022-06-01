# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ApiKeyResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.api_key import ApiKey

        return {
            "api_key": (ApiKey,),
        }

    attribute_map = {
        "api_key": "api_key",
    }

    def __init__(self, *args, **kwargs):
        """
        An API key with its associated metadata.

        :param api_key: Datadog API key.
        :type api_key: ApiKey, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ApiKeyResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
