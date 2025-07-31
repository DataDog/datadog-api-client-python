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
    from datadog_api_client.v2.model.asana_access_token_type import AsanaAccessTokenType


class AsanaAccessToken(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.asana_access_token_type import AsanaAccessTokenType

        return {
            "access_token": (str,),
            "type": (AsanaAccessTokenType,),
        }

    attribute_map = {
        "access_token": "access_token",
        "type": "type",
    }

    def __init__(self_, access_token: str, type: AsanaAccessTokenType, **kwargs):
        """
        The definition of the ``AsanaAccessToken`` object.

        :param access_token: The ``AsanaAccessToken`` ``access_token``.
        :type access_token: str

        :param type: The definition of the ``AsanaAccessToken`` object.
        :type type: AsanaAccessTokenType
        """
        super().__init__(kwargs)

        self_.access_token = access_token
        self_.type = type
