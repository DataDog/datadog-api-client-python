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
    from datadog_api_client.v2.model.databricks_integration_account_authentication_update import (
        DatabricksIntegrationAccountAuthenticationUpdate,
    )
    from datadog_api_client.v2.model.databricks_integration_dataflows_request import (
        DatabricksIntegrationDataflowsRequest,
    )
    from datadog_api_client.v2.model.databricks_integration_account_settings_update import (
        DatabricksIntegrationAccountSettingsUpdate,
    )
    from datadog_api_client.v2.model.databricks_integration_account_o_auth_auth_update import (
        DatabricksIntegrationAccountOAuthAuthUpdate,
    )
    from datadog_api_client.v2.model.integration_account_private_action_runner_auth_request import (
        IntegrationAccountPrivateActionRunnerAuthRequest,
    )
    from datadog_api_client.v2.model.databricks_integration_account_pat_auth_update import (
        DatabricksIntegrationAccountPatAuthUpdate,
    )


class DatabricksIntegrationAccountUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.databricks_integration_account_authentication_update import (
            DatabricksIntegrationAccountAuthenticationUpdate,
        )
        from datadog_api_client.v2.model.databricks_integration_dataflows_request import (
            DatabricksIntegrationDataflowsRequest,
        )
        from datadog_api_client.v2.model.databricks_integration_account_settings_update import (
            DatabricksIntegrationAccountSettingsUpdate,
        )

        return {
            "authentication": (DatabricksIntegrationAccountAuthenticationUpdate,),
            "dataflows": (DatabricksIntegrationDataflowsRequest,),
            "name": (str,),
            "settings": (DatabricksIntegrationAccountSettingsUpdate,),
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
            DatabricksIntegrationAccountAuthenticationUpdate,
            DatabricksIntegrationAccountOAuthAuthUpdate,
            IntegrationAccountPrivateActionRunnerAuthRequest,
            DatabricksIntegrationAccountPatAuthUpdate,
            UnsetType,
        ] = unset,
        dataflows: Union[DatabricksIntegrationDataflowsRequest, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        settings: Union[DatabricksIntegrationAccountSettingsUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        Writable attributes used to update a Databricks integration account. Every field is optional; only the fields provided are changed. When ``dataflows`` is provided, only the dataflow ids included in the request are modified; dataflows omitted from the map keep their current configuration, as do the settings of an included dataflow that provides only ``enabled``.

        :param authentication: Authentication for updating the Databricks integration account. Exactly one method is set. Choosing ``private-action-runner`` leaves the ``databricks-model-serving-metrics`` dataflow unable to collect data. ``pat`` is accepted only on accounts that already use it, so it cannot move an account onto personal access token authentication.
        :type authentication: DatabricksIntegrationAccountAuthenticationUpdate, optional

        :param dataflows: Dataflows to configure on the Databricks integration account, keyed by dataflow id. Some dataflows and settings have prerequisites, noted on each. Those prerequisites are not checked when the request is made, so anything left enabled without them is stored but collects no data.
        :type dataflows: DatabricksIntegrationDataflowsRequest, optional

        :param name: Human-readable name of the Databricks integration account.
        :type name: str, optional

        :param settings: Settings for updating the Databricks integration account. Only the fields provided are changed.
        :type settings: DatabricksIntegrationAccountSettingsUpdate, optional
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        if name is not unset:
            kwargs["name"] = name
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)
