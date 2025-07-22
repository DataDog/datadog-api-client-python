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
    from datadog_api_client.v2.model.launch_darkly_api_key_type import LaunchDarklyAPIKeyType


class LaunchDarklyAPIKeyUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.launch_darkly_api_key_type import LaunchDarklyAPIKeyType

        return {
            "api_token": (str,),
            "type": (LaunchDarklyAPIKeyType,),
        }

    attribute_map = {
        "api_token": "api_token",
        "type": "type",
    }

    def __init__(self_, type: LaunchDarklyAPIKeyType, api_token: Union[str, UnsetType] = unset, **kwargs):
        """
        The definition of the ``LaunchDarklyAPIKey`` object.

        :param api_token: The ``LaunchDarklyAPIKeyUpdate`` ``api_token``.
        :type api_token: str, optional

        :param type: The definition of the ``LaunchDarklyAPIKey`` object.
        :type type: LaunchDarklyAPIKeyType
        """
        if api_token is not unset:
            kwargs["api_token"] = api_token
        super().__init__(kwargs)

        self_.type = type
