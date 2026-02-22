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
    from datadog_api_client.v2.model.personal_access_token import PersonalAccessToken
    from datadog_api_client.v2.model.personal_access_tokens_response_meta import PersonalAccessTokensResponseMeta


class PersonalAccessTokensListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.personal_access_token import PersonalAccessToken
        from datadog_api_client.v2.model.personal_access_tokens_response_meta import PersonalAccessTokensResponseMeta

        return {
            "data": ([PersonalAccessToken],),
            "meta": (PersonalAccessTokensResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[PersonalAccessToken], UnsetType] = unset,
        meta: Union[PersonalAccessTokensResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response for a list of personal access tokens.

        :param data: Array of personal access tokens.
        :type data: [PersonalAccessToken], optional

        :param meta: Additional information related to the personal access tokens response.
        :type meta: PersonalAccessTokensResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
