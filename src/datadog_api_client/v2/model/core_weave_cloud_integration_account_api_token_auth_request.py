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
    from datadog_api_client.v2.model.core_weave_cloud_integration_account_api_token_auth_type import (
        CoreWeaveCloudIntegrationAccountAPITokenAuthType,
    )


class CoreWeaveCloudIntegrationAccountAPITokenAuthRequest(ModelNormal):
    validations = {
        "api_token": {},
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.core_weave_cloud_integration_account_api_token_auth_type import (
            CoreWeaveCloudIntegrationAccountAPITokenAuthType,
        )

        return {
            "api_token": (str,),
            "auth_type": (CoreWeaveCloudIntegrationAccountAPITokenAuthType,),
        }

    attribute_map = {
        "api_token": "api_token",
        "auth_type": "auth_type",
    }

    def __init__(self_, api_token: str, auth_type: CoreWeaveCloudIntegrationAccountAPITokenAuthType, **kwargs):
        """
        API token authentication, the only method CoreWeave integration accounts support. Create the token in the CoreWeave Cloud console under Access Tokens; it starts with ``CW-SECRET-``. The user who owns the token must have the Observability Viewer role, because tokens inherit their user's permissions.

        :param api_token: Secret CoreWeave API access token used to authenticate with CoreWeave. Values that do not start with ``CW-SECRET-`` are rejected with a ``422`` response.
        :type api_token: str

        :param auth_type: The authentication method type.
        :type auth_type: CoreWeaveCloudIntegrationAccountAPITokenAuthType
        """
        super().__init__(kwargs)

        self_.api_token = api_token
        self_.auth_type = auth_type
