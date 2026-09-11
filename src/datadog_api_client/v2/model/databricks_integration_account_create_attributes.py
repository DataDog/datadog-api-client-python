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
    from datadog_api_client.v2.model.databricks_integration_account_authentication_request import (
        DatabricksIntegrationAccountAuthenticationRequest,
    )
    from datadog_api_client.v2.model.databricks_integration_dataflows_request import (
        DatabricksIntegrationDataflowsRequest,
    )
    from datadog_api_client.v2.model.databricks_integration_account_settings_request import (
        DatabricksIntegrationAccountSettingsRequest,
    )
    from datadog_api_client.v2.model.databricks_integration_account_o_auth_auth_request import (
        DatabricksIntegrationAccountOAuthAuthRequest,
    )
    from datadog_api_client.v2.model.integration_account_private_action_runner_auth_request import (
        IntegrationAccountPrivateActionRunnerAuthRequest,
    )


class DatabricksIntegrationAccountCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.databricks_integration_account_authentication_request import (
            DatabricksIntegrationAccountAuthenticationRequest,
        )
        from datadog_api_client.v2.model.databricks_integration_dataflows_request import (
            DatabricksIntegrationDataflowsRequest,
        )
        from datadog_api_client.v2.model.databricks_integration_account_settings_request import (
            DatabricksIntegrationAccountSettingsRequest,
        )

        return {
            "authentication": (DatabricksIntegrationAccountAuthenticationRequest,),
            "dataflows": (DatabricksIntegrationDataflowsRequest,),
            "name": (str,),
            "settings": (DatabricksIntegrationAccountSettingsRequest,),
        }

    attribute_map = {
        "authentication": "authentication",
        "dataflows": "dataflows",
        "name": "name",
        "settings": "settings",
    }

    def __init__(
        self_,
        authentication: Union[
            DatabricksIntegrationAccountAuthenticationRequest,
            DatabricksIntegrationAccountOAuthAuthRequest,
            IntegrationAccountPrivateActionRunnerAuthRequest,
        ],
        name: str,
        settings: DatabricksIntegrationAccountSettingsRequest,
        dataflows: Union[DatabricksIntegrationDataflowsRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Writable attributes used to create a Databricks integration account.

        :param authentication: Authentication for creating the Databricks integration account. Exactly one method is set. Choosing ``private-action-runner`` leaves the ``databricks-model-serving-metrics`` dataflow unable to collect data.
        :type authentication: DatabricksIntegrationAccountAuthenticationRequest

        :param dataflows: Data Datadog collects from Databricks, keyed by dataflow id. Each dataflow turns on a distinct kind of collection: set ``enabled`` to start or stop it, and use ``settings`` to tune what it gathers. The defaults noted below apply when the account is created; on update, anything left out keeps its current value. Some dataflows have prerequisites, noted on each; unless one is documented as rejecting the request, it is not verified, so a dataflow enabled without it is stored but collects no data.
        :type dataflows: DatabricksIntegrationDataflowsRequest, optional

        :param name: Human-readable name of the Databricks integration account.
        :type name: str

        :param settings: Settings for creating the Databricks integration account.
        :type settings: DatabricksIntegrationAccountSettingsRequest
        """
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.authentication = authentication
        self_.name = name
        self_.settings = settings
