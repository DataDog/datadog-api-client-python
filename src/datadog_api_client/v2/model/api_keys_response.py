# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.partial_api_key import PartialAPIKey
    from datadog_api_client.v2.model.api_key_response_included_item import APIKeyResponseIncludedItem
    from datadog_api_client.v2.model.api_keys_response_meta import APIKeysResponseMeta
    from datadog_api_client.v2.model.user import User


class APIKeysResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.partial_api_key import PartialAPIKey
        from datadog_api_client.v2.model.api_key_response_included_item import APIKeyResponseIncludedItem
        from datadog_api_client.v2.model.api_keys_response_meta import APIKeysResponseMeta

        return {
            "data": ([PartialAPIKey],),
            "included": ([APIKeyResponseIncludedItem],),
            "meta": (APIKeysResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[PartialAPIKey], UnsetType] = unset,
        included: Union[List[Union[APIKeyResponseIncludedItem, User]], UnsetType] = unset,
        meta: Union[APIKeysResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response for a list of API keys.

        :param data: Array of API keys.
        :type data: [PartialAPIKey], optional

        :param included: Array of objects related to the API key.
        :type included: [APIKeyResponseIncludedItem], optional

        :param meta: Additional information related to api keys response.
        :type meta: APIKeysResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
