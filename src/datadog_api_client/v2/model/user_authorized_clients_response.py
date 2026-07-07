# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.user_authorized_client_data import UserAuthorizedClientData
    from datadog_api_client.v2.model.response_meta_attributes import ResponseMetaAttributes


class UserAuthorizedClientsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_authorized_client_data import UserAuthorizedClientData
        from datadog_api_client.v2.model.response_meta_attributes import ResponseMetaAttributes

        return {
            "data": ([UserAuthorizedClientData],),
            "meta": (ResponseMetaAttributes,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[UserAuthorizedClientData], meta: ResponseMetaAttributes, **kwargs):
        """
        Response containing a list of user authorized clients.

        :param data: List of user authorized client data objects.
        :type data: [UserAuthorizedClientData]

        :param meta: Object describing meta attributes of response.
        :type meta: ResponseMetaAttributes
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
