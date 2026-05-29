# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.full_service_access_token import FullServiceAccessToken


class ServiceAccessTokenCreateResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.full_service_access_token import FullServiceAccessToken

        return {
            "data": (FullServiceAccessToken,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[FullServiceAccessToken, UnsetType] = unset, **kwargs):
        """
        Response for creating an access token. Includes the token key.

        :param data: Datadog access token, including the token key.
        :type data: FullServiceAccessToken, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
