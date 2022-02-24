# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.api_key_update_attributes import APIKeyUpdateAttributes
    from datadog_api_client.v2.model.api_keys_type import APIKeysType

    globals()["APIKeyUpdateAttributes"] = APIKeyUpdateAttributes
    globals()["APIKeysType"] = APIKeysType


class APIKeyUpdateData(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "attributes": (APIKeyUpdateAttributes,),
            "id": (str,),
            "type": (APIKeysType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, attributes, id, type, *args, **kwargs):
        """
        Object used to update an API key.

        :param attributes: Attributes used to update an API Key.
        :type attributes: APIKeyUpdateAttributes

        :param id: ID of the API key.
        :type id: str

        :param type: API Keys resource type.
        :type type: APIKeysType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.id = id
        self.type = type

    @classmethod
    def _from_openapi_data(cls, attributes, id, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(APIKeyUpdateData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.id = id
        self.type = type
        return self
