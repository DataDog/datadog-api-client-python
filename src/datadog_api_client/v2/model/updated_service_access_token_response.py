# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.updated_service_access_token import UpdatedServiceAccessToken


class UpdatedServiceAccessTokenResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.updated_service_access_token import UpdatedServiceAccessToken

        return {
            "data": (UpdatedServiceAccessToken,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: UpdatedServiceAccessToken, **kwargs):
        """
        Response for updating an access token.

        :param data: Datadog access token returned by the update endpoint.
        :type data: UpdatedServiceAccessToken
        """
        super().__init__(kwargs)

        self_.data = data
