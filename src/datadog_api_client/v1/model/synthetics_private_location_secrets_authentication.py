# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsPrivateLocationSecretsAuthentication(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "key": (str,),
        }

    attribute_map = {
        "id": "id",
        "key": "key",
    }
    read_only_vars = {
        "id",
        "key",
    }

    def __init__(self, *args, **kwargs):
        """
        Authentication part of the secrets.

        :param id: Access key for the private location.
        :type id: str, optional

        :param key: Secret access key for the private location.
        :type key: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsPrivateLocationSecretsAuthentication, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
