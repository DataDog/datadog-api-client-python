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
    from datadog_api_client.v2.model.databricks_integration_account_pat_auth_type import (
        DatabricksIntegrationAccountPatAuthType,
    )


class DatabricksIntegrationAccountPatAuthResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.databricks_integration_account_pat_auth_type import (
            DatabricksIntegrationAccountPatAuthType,
        )

        return {
            "auth_type": (DatabricksIntegrationAccountPatAuthType,),
        }

    attribute_map = {
        "auth_type": "auth_type",
    }

    def __init__(self_, auth_type: DatabricksIntegrationAccountPatAuthType, **kwargs):
        """
        The Databricks personal access token authentication method configured on the account. Deprecated: migrate these accounts to ``databricks-oauth`` or ``private-action-runner``.

        :param auth_type: The authentication method type.
        :type auth_type: DatabricksIntegrationAccountPatAuthType
        """
        super().__init__(kwargs)

        self_.auth_type = auth_type
