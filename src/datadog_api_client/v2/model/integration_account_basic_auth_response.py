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
    from datadog_api_client.v2.model.integration_account_basic_auth_type import IntegrationAccountBasicAuthType


class IntegrationAccountBasicAuthResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.integration_account_basic_auth_type import IntegrationAccountBasicAuthType

        return {
            "auth_type": (IntegrationAccountBasicAuthType,),
            "username": (str,),
        }

    attribute_map = {
        "auth_type": "auth_type",
        "username": "username",
    }

    def __init__(self_, auth_type: IntegrationAccountBasicAuthType, username: str, **kwargs):
        """
        The basic authentication method and username configured on the account.

        :param auth_type: The authentication method type.
        :type auth_type: IntegrationAccountBasicAuthType

        :param username: Non-secret username or public identifier for the credential pair.
        :type username: str
        """
        super().__init__(kwargs)

        self_.auth_type = auth_type
        self_.username = username
