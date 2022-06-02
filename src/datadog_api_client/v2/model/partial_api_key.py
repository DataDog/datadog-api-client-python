# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class PartialAPIKey(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.partial_api_key_attributes import PartialAPIKeyAttributes
        from datadog_api_client.v2.model.api_key_relationships import APIKeyRelationships
        from datadog_api_client.v2.model.api_keys_type import APIKeysType

        return {
            "attributes": (PartialAPIKeyAttributes,),
            "id": (str,),
            "relationships": (APIKeyRelationships,),
            "type": (APIKeysType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        Partial Datadog API key.

        :param attributes: Attributes of a partial API key.
        :type attributes: PartialAPIKeyAttributes, optional

        :param id: ID of the API key.
        :type id: str, optional

        :param relationships: Resources related to the API key.
        :type relationships: APIKeyRelationships, optional

        :param type: API Keys resource type.
        :type type: APIKeysType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(PartialAPIKey, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
