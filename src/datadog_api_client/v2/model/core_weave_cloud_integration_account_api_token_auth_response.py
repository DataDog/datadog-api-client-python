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


class CoreWeaveCloudIntegrationAccountAPITokenAuthResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.core_weave_cloud_integration_account_api_token_auth_type import (
            CoreWeaveCloudIntegrationAccountAPITokenAuthType,
        )

        return {
            "auth_type": (CoreWeaveCloudIntegrationAccountAPITokenAuthType,),
        }

    attribute_map = {
        "auth_type": "auth_type",
    }

    def __init__(self_, auth_type: CoreWeaveCloudIntegrationAccountAPITokenAuthType, **kwargs):
        """
        The API token authentication method configured on the account.

        :param auth_type: The authentication method type.
        :type auth_type: CoreWeaveCloudIntegrationAccountAPITokenAuthType
        """
        super().__init__(kwargs)

        self_.auth_type = auth_type
