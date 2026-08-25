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
    from datadog_api_client.v2.model.integration_account_basic_auth_type import IntegrationAccountBasicAuthType


class IntegrationAccountBasicAuthUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.integration_account_basic_auth_type import IntegrationAccountBasicAuthType

        return {
            "auth_type": (IntegrationAccountBasicAuthType,),
            "password": (str,),
            "username": (str,),
        }

    attribute_map = {
        "auth_type": "auth_type",
        "password": "password",
        "username": "username",
    }

    def __init__(
        self_,
        auth_type: IntegrationAccountBasicAuthType,
        password: Union[str, UnsetType] = unset,
        username: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Username and password authentication. Only the fields provided are changed; omit ``password`` to keep the stored one.

        :param auth_type: The authentication method type.
        :type auth_type: IntegrationAccountBasicAuthType

        :param password: Secret password or private key.
        :type password: str, optional

        :param username: Non-secret username or public identifier for the credential pair.
        :type username: str, optional
        """
        if password is not unset:
            kwargs["password"] = password
        if username is not unset:
            kwargs["username"] = username
        super().__init__(kwargs)

        self_.auth_type = auth_type
