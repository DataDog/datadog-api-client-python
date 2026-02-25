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
    from datadog_api_client.v2.model.full_personal_access_token import FullPersonalAccessToken


class PersonalAccessTokenResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.full_personal_access_token import FullPersonalAccessToken

        return {
            "data": (FullPersonalAccessToken,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[FullPersonalAccessToken, UnsetType] = unset, **kwargs):
        """
        Response for creating a personal access token.

        :param data: Personal access token object with the secret key value. This is only
            returned when creating a new token.
        :type data: FullPersonalAccessToken, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
