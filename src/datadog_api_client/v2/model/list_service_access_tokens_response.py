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
    from datadog_api_client.v2.model.service_access_token_response_meta import ServiceAccessTokenResponseMeta
    from datadog_api_client.v2.model.leaked_key import LeakedKey


class ListServiceAccessTokensResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_access_token import ServiceAccessToken
        from datadog_api_client.v2.model.access_token_response_included_item import AccessTokenResponseIncludedItem
        from datadog_api_client.v2.model.service_access_token_response_meta import ServiceAccessTokenResponseMeta

        return {
            "data": ([ServiceAccessToken],),
            "included": ([AccessTokenResponseIncludedItem],),
            "meta": (ServiceAccessTokenResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[ServiceAccessToken], UnsetType] = unset,
        included: Union[List[Union[AccessTokenResponseIncludedItem, LeakedKey]], UnsetType] = unset,
        meta: Union[ServiceAccessTokenResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response for a list of access tokens.

        :param data: Array of access tokens.
        :type data: [ServiceAccessToken], optional

        :param included: Array of objects related to the access tokens.
        :type included: [AccessTokenResponseIncludedItem], optional

        :param meta: Additional information related to the access token response.
        :type meta: ServiceAccessTokenResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
