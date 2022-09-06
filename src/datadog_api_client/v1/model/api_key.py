# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ApiKey(ModelNormal):
    validations = {
        "key": {
            "max_length": 32,
            "min_length": 32,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "created": (str,),
            "created_by": (str,),
            "key": (str,),
            "name": (str,),
        }

    attribute_map = {
        "created": "created",
        "created_by": "created_by",
        "key": "key",
        "name": "name",
    }
    read_only_vars = {
        "created",
        "created_by",
        "key",
    }

    def __init__(self_, *args, **kwargs):
        """
        Datadog API key.

        :param created: Date of creation of the API key.
        :type created: str, optional

        :param created_by: Datadog user handle that created the API key.
        :type created_by: str, optional

        :param key: API key.
        :type key: str, optional

        :param name: Name of your API key.
        :type name: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
