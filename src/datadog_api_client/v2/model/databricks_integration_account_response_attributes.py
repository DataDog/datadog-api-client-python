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
    from datadog_api_client.v2.model.databricks_integration_account_authentication_response import (
        DatabricksIntegrationAccountAuthenticationResponse,
    )
    from datadog_api_client.v2.model.databricks_integration_dataflows_response import (
        DatabricksIntegrationDataflowsResponse,
    )
    from datadog_api_client.v2.model.databricks_integration_account_settings_response import (
        DatabricksIntegrationAccountSettingsResponse,
    )
    from datadog_api_client.v2.model.databricks_integration_account_o_auth_auth_response import (
        DatabricksIntegrationAccountOAuthAuthResponse,
    )
    from datadog_api_client.v2.model.integration_account_private_action_runner_auth_response import (
        IntegrationAccountPrivateActionRunnerAuthResponse,
    )
    from datadog_api_client.v2.model.databricks_integration_account_pat_auth_response import (
        DatabricksIntegrationAccountPatAuthResponse,
    )


class DatabricksIntegrationAccountResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.databricks_integration_account_authentication_response import (
            DatabricksIntegrationAccountAuthenticationResponse,
        )
        from datadog_api_client.v2.model.databricks_integration_dataflows_response import (
            DatabricksIntegrationDataflowsResponse,
        )
        from datadog_api_client.v2.model.databricks_integration_account_settings_response import (
            DatabricksIntegrationAccountSettingsResponse,
        )

        return {
            "authentication": (DatabricksIntegrationAccountAuthenticationResponse,),
            "dataflows": (DatabricksIntegrationDataflowsResponse,),
            "name": (str,),
            "settings": (DatabricksIntegrationAccountSettingsResponse,),
        }

    attribute_map = {
        "authentication": "authentication",
        "dataflows": "dataflows",
        "name": "name",
        "settings": "settings",
    }

    def __init__(
        self_,
        name: str,
        settings: DatabricksIntegrationAccountSettingsResponse,
        authentication: Union[
            DatabricksIntegrationAccountAuthenticationResponse,
            DatabricksIntegrationAccountOAuthAuthResponse,
            IntegrationAccountPrivateActionRunnerAuthResponse,
            DatabricksIntegrationAccountPatAuthResponse,
            UnsetType,
        ] = unset,
        dataflows: Union[DatabricksIntegrationDataflowsResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a Databricks integration account returned in responses.

        :param authentication: Authentication configured on the Databricks integration account.
        :type authentication: DatabricksIntegrationAccountAuthenticationResponse, optional

        :param dataflows: Dataflows configured on the Databricks integration account, keyed by dataflow id.
        :type dataflows: DatabricksIntegrationDataflowsResponse, optional

        :param name: Human-readable name of the Databricks integration account.
        :type name: str

        :param settings: Settings configured on the Databricks integration account.
        :type settings: DatabricksIntegrationAccountSettingsResponse
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.name = name
        self_.settings = settings
