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
    from datadog_api_client.v2.model.notion_api_key_type import NotionAPIKeyType


class NotionAPIKey(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notion_api_key_type import NotionAPIKeyType

        return {
            "api_token": (str,),
            "type": (NotionAPIKeyType,),
        }

    attribute_map = {
        "api_token": "api_token",
        "type": "type",
    }

    def __init__(self_, api_token: str, type: NotionAPIKeyType, **kwargs):
        """
        The definition of the ``NotionAPIKey`` object.

        :param api_token: The ``NotionAPIKey`` ``api_token``.
        :type api_token: str

        :param type: The definition of the ``NotionAPIKey`` object.
        :type type: NotionAPIKeyType
        """
        super().__init__(kwargs)

        self_.api_token = api_token
        self_.type = type
