# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class FullAPIKeyAttributes(ModelNormal):
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
            "modified_at": (str,),
            "name": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "key": "key",
        "last4": "last4",
        "modified_at": "modified_at",
        "name": "name",
    }
    read_only_vars = {
        "created_at",
        "key",
        "last4",
        "modified_at",
    }

    def __init__(self_, *args, **kwargs):
        """
        Attributes of a full API key.

        :param created_at: Creation date of the API key.
        :type created_at: str, optional

        :param key: The API key.
        :type key: str, optional

        :param last4: The last four characters of the API key.
        :type last4: str, optional

        :param modified_at: Date the API key was last modified.
        :type modified_at: str, optional

        :param name: Name of the API key.
        :type name: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
