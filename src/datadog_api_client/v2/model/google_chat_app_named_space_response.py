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
    from datadog_api_client.v2.model.google_chat_app_named_space_response_data import (
        GoogleChatAppNamedSpaceResponseData,
    )


class GoogleChatAppNamedSpaceResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.google_chat_app_named_space_response_data import (
            GoogleChatAppNamedSpaceResponseData,
        )

        return {
            "data": (GoogleChatAppNamedSpaceResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: GoogleChatAppNamedSpaceResponseData, **kwargs):
        """
        Response of a Google Chat app named space.

        :param data: Google Chat app named space data from a response.
        :type data: GoogleChatAppNamedSpaceResponseData
        """
        super().__init__(kwargs)

        self_.data = data
