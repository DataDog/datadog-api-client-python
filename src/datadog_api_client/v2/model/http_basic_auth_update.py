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
    from datadog_api_client.v2.model.http_basic_auth_type import HTTPBasicAuthType


class HTTPBasicAuthUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.http_basic_auth_type import HTTPBasicAuthType

        return {
            "password": (str,),
            "type": (HTTPBasicAuthType,),
            "username": (str,),
        }

    attribute_map = {
        "password": "password",
        "type": "type",
        "username": "username",
    }

    def __init__(
        self_,
        type: HTTPBasicAuthType,
        password: Union[str, UnsetType] = unset,
        username: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``HTTPBasicAuth`` object.

        :param password: Password used for authentication. Saved in a secret store
        :type password: str, optional

        :param type: The definition of the ``HTTPBasicAuth`` object.
        :type type: HTTPBasicAuthType

        :param username: Username used for authentication.
        :type username: str, optional
        """
        if password is not unset:
            kwargs["password"] = password
        if username is not unset:
            kwargs["username"] = username
        super().__init__(kwargs)

        self_.type = type
