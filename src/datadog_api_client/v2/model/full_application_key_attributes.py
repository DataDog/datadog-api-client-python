# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class FullApplicationKeyAttributes(ModelNormal):
    validations = {
        "last4": {
            "max_length": 4,
            "min_length": 4,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "created_at": (str,),
            "key": (str,),
            "last4": (str,),
            "name": (str,),
            "scopes": ([str], none_type),
        }

    attribute_map = {
        "created_at": "created_at",
        "key": "key",
        "last4": "last4",
        "name": "name",
        "scopes": "scopes",
    }
    read_only_vars = {
        "created_at",
        "key",
        "last4",
    }

    def __init__(self, *args, **kwargs):
        """
        Attributes of a full application key.

        :param created_at: Creation date of the application key.
        :type created_at: str, optional

        :param key: The application key.
        :type key: str, optional

        :param last4: The last four characters of the application key.
        :type last4: str, optional

        :param name: Name of the application key.
        :type name: str, optional

        :param scopes: Array of scopes to grant the application key. This feature is in private beta, please contact Datadog support to enable scopes for your application keys.
        :type scopes: [str], none_type, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(FullApplicationKeyAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
