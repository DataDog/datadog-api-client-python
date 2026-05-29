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
    from datadog_api_client.v2.model.access_token_list_item import AccessTokenListItem
    from datadog_api_client.v2.model.personal_access_token_response_meta import PersonalAccessTokenResponseMeta


class ListPersonalAccessTokensResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.access_token_list_item import AccessTokenListItem
        from datadog_api_client.v2.model.personal_access_token_response_meta import PersonalAccessTokenResponseMeta

        return {
            "data": ([AccessTokenListItem],),
            "meta": (PersonalAccessTokenResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[AccessTokenListItem], UnsetType] = unset,
        meta: Union[PersonalAccessTokenResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response for a list of access tokens. Includes both personal and service access tokens.

        :param data: Array of access tokens. Includes both personal and service access tokens.
        :type data: [AccessTokenListItem], optional

        :param meta: Additional information related to the access token response.
        :type meta: PersonalAccessTokenResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
