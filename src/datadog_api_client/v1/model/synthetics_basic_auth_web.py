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
    from datadog_api_client.v1.model.synthetics_basic_auth_web_type import SyntheticsBasicAuthWebType


class SyntheticsBasicAuthWeb(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_basic_auth_web_type import SyntheticsBasicAuthWebType

        return {
            "password": (str,),
            "type": (SyntheticsBasicAuthWebType,),
            "username": (str,),
        }

    attribute_map = {
        "password": "password",
        "type": "type",
        "username": "username",
    }

    def __init__(
        self_,
        password: Union[str, UnsetType] = unset,
        type: Union[SyntheticsBasicAuthWebType, UnsetType] = unset,
        username: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object to handle basic authentication when performing the test.

        :param password: Password to use for the basic authentication.
        :type password: str, optional

        :param type: The type of basic authentication to use when performing the test.
        :type type: SyntheticsBasicAuthWebType, optional

        :param username: Username to use for the basic authentication.
        :type username: str, optional
        """
        if password is not unset:
            kwargs["password"] = password
        if type is not unset:
            kwargs["type"] = type
        if username is not unset:
            kwargs["username"] = username
        super().__init__(kwargs)
