# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ListApplicationKeysResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.partial_application_key import PartialApplicationKey
        from datadog_api_client.v2.model.application_key_response_included_item import (
            ApplicationKeyResponseIncludedItem,
        )

        return {
            "data": ([PartialApplicationKey],),
            "included": ([ApplicationKeyResponseIncludedItem],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(self, *args, **kwargs):
        """
        Response for a list of application keys.

        :param data: Array of application keys.
        :type data: [PartialApplicationKey], optional

        :param included: Array of objects related to the application key.
        :type included: [ApplicationKeyResponseIncludedItem], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ListApplicationKeysResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
