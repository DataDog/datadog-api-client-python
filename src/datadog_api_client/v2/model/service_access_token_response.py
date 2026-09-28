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
    from datadog_api_client.v2.model.service_access_token import ServiceAccessToken
    from datadog_api_client.v2.model.access_token_response_included_item import AccessTokenResponseIncludedItem
    from datadog_api_client.v2.model.leaked_key import LeakedKey


class ServiceAccessTokenResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_access_token import ServiceAccessToken
        from datadog_api_client.v2.model.access_token_response_included_item import AccessTokenResponseIncludedItem

        return {
            "data": (ServiceAccessToken,),
            "included": ([AccessTokenResponseIncludedItem],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: Union[ServiceAccessToken, UnsetType] = unset,
        included: Union[List[Union[AccessTokenResponseIncludedItem, LeakedKey]], UnsetType] = unset,
        **kwargs,
    ):
        """
        Response for retrieving an access token.

        :param data: Datadog access token.
        :type data: ServiceAccessToken, optional

        :param included: Array of objects related to the access tokens.
        :type included: [AccessTokenResponseIncludedItem], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)
