# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.full_api_key import FullAPIKey
    from datadog_api_client.v2.model.api_key_response_included_item import APIKeyResponseIncludedItem
    from datadog_api_client.v2.model.user import User


@dataclass
class APIKeyResponseJSON:
    id: str
    created_at: Union[str, UnsetType] = unset
    key: Union[str, UnsetType] = unset
    last4: Union[str, UnsetType] = unset
    modified_at: Union[str, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    created_by: Union[str, UnsetType] = unset
    modified_by: Union[str, UnsetType] = unset


class APIKeyResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.full_api_key import FullAPIKey
        from datadog_api_client.v2.model.api_key_response_included_item import APIKeyResponseIncludedItem

        return {
            "data": (FullAPIKey,),
            "included": ([APIKeyResponseIncludedItem],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }
    json_api_model = APIKeyResponseJSON

    def __init__(
        self_,
        data: Union[FullAPIKey, UnsetType] = unset,
        included: Union[List[Union[APIKeyResponseIncludedItem, User]], UnsetType] = unset,
        **kwargs,
    ):
        """
        Response for retrieving an API key.

        :param data: Datadog API key.
        :type data: FullAPIKey, optional

        :param included: Array of objects related to the API key.
        :type included: [APIKeyResponseIncludedItem], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)
