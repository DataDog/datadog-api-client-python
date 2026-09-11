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


class DatabricksIntegrationAccountPatAuthUpdate(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.databricks_integration_account_pat_auth_type import (
            DatabricksIntegrationAccountPatAuthType,
        )

        return {
            "auth_type": (DatabricksIntegrationAccountPatAuthType,),
            "token": (str,),
        }

    attribute_map = {
        "auth_type": "auth_type",
        "token": "token",
    }

    def __init__(self_, auth_type: DatabricksIntegrationAccountPatAuthType, token: str, **kwargs):
        """
        Databricks personal access token authentication. Deprecated: accepted only on accounts that already use it, and never on creation. Use ``databricks-oauth`` or ``private-action-runner`` instead. An update replaces this object as a whole, so ``token`` must be sent with it.

        :param auth_type: The authentication method type.
        :type auth_type: DatabricksIntegrationAccountPatAuthType

        :param token: Secret Databricks personal access token.
        :type token: str
        """
        super().__init__(kwargs)

        self_.auth_type = auth_type
        self_.token = token
