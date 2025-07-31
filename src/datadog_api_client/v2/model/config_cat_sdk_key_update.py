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
    from datadog_api_client.v2.model.config_cat_sdk_key_type import ConfigCatSDKKeyType


class ConfigCatSDKKeyUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.config_cat_sdk_key_type import ConfigCatSDKKeyType

        return {
            "api_password": (str,),
            "api_username": (str,),
            "sdk_key": (str,),
            "type": (ConfigCatSDKKeyType,),
        }

    attribute_map = {
        "api_password": "api_password",
        "api_username": "api_username",
        "sdk_key": "sdk_key",
        "type": "type",
    }

    def __init__(
        self_,
        type: ConfigCatSDKKeyType,
        api_password: Union[str, UnsetType] = unset,
        api_username: Union[str, UnsetType] = unset,
        sdk_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``ConfigCatSDKKey`` object.

        :param api_password: The ``ConfigCatSDKKeyUpdate`` ``api_password``.
        :type api_password: str, optional

        :param api_username: The ``ConfigCatSDKKeyUpdate`` ``api_username``.
        :type api_username: str, optional

        :param sdk_key: The ``ConfigCatSDKKeyUpdate`` ``sdk_key``.
        :type sdk_key: str, optional

        :param type: The definition of the ``ConfigCatSDKKey`` object.
        :type type: ConfigCatSDKKeyType
        """
        if api_password is not unset:
            kwargs["api_password"] = api_password
        if api_username is not unset:
            kwargs["api_username"] = api_username
        if sdk_key is not unset:
            kwargs["sdk_key"] = sdk_key
        super().__init__(kwargs)

        self_.type = type
