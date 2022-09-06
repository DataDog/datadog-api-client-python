# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AuthNMappingUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "attribute_key": (str,),
            "attribute_value": (str,),
        }

    attribute_map = {
        "attribute_key": "attribute_key",
        "attribute_value": "attribute_value",
    }

    def __init__(self_, *args, **kwargs):
        """
        Key/Value pair of attributes used for update request.

        :param attribute_key: Key portion of a key/value pair of the attribute sent from the Identity Provider.
        :type attribute_key: str, optional

        :param attribute_value: Value portion of a key/value pair of the attribute sent from the Identity Provider.
        :type attribute_value: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
