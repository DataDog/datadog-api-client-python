# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class APIKeysResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.partial_api_key import PartialAPIKey
        from datadog_api_client.v2.model.api_key_response_included_item import APIKeyResponseIncludedItem

        return {
            "data": ([PartialAPIKey],),
            "included": ([APIKeyResponseIncludedItem],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(self, *args, **kwargs):
        """
        Response for a list of API keys.

        :param data: Array of API keys.
        :type data: [PartialAPIKey], optional

        :param included: Array of objects related to the API key.
        :type included: [APIKeyResponseIncludedItem], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(APIKeysResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
