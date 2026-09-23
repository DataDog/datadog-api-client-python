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
    from datadog_api_client.v2.model.databricks_integration_account_private_action_runner_auth_update import (
        DatabricksIntegrationAccountPrivateActionRunnerAuthUpdate,
    )
    from datadog_api_client.v2.model.databricks_integration_account_bearer_token_auth_update import (
        DatabricksIntegrationAccountBearerTokenAuthUpdate,
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
            DatabricksIntegrationAccountPrivateActionRunnerAuthUpdate,
            DatabricksIntegrationAccountBearerTokenAuthUpdate,
            UnsetType,
        ] = unset,
        dataflows: Union[DatabricksIntegrationDataflowsRequest, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        settings: Union[DatabricksIntegrationAccountSettingsUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        Writable attributes used to update a Databricks integration account. Every field is optional; only the fields provided are changed. When ``dataflows`` is provided, only the dataflow ids included in the request are modified; dataflows omitted from the map keep their current configuration, as do the settings of an included dataflow that provides only ``enabled``.

        :param authentication: Authentication for updating the Databricks integration account. Exactly one method is set. Choosing ``private_action_runner`` leaves the ``databricks-model-serving-metrics`` dataflow unable to collect data. ``bearer_token`` is deprecated on Databricks: it is accepted only on accounts that already use it and never on creation, so it cannot move an account onto token authentication. Migrate those accounts to ``databricks_oauth`` or ``private_action_runner``.
        :type authentication: DatabricksIntegrationAccountAuthenticationUpdate, optional

        :param dataflows: Data Datadog collects from Databricks, keyed by dataflow id. Each dataflow turns on a distinct kind of collection: set ``enabled`` to start or stop it, and use ``settings`` to configure what it collects. Defaults listed on each dataflow apply when the account is created; on update, omitted fields keep their current values. Some dataflows have prerequisites, noted on each; unless one is documented as rejecting the request, it is not verified, so a dataflow enabled without it is stored but collects no data.
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
