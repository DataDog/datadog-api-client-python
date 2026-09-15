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
    from datadog_api_client.v2.model.snowflake_integration_account_authentication_response import (
        SnowflakeIntegrationAccountAuthenticationResponse,
    )
    from datadog_api_client.v2.model.snowflake_integration_dataflows_response import (
        SnowflakeIntegrationDataflowsResponse,
    )
    from datadog_api_client.v2.model.snowflake_integration_account_settings_response import (
        SnowflakeIntegrationAccountSettingsResponse,
    )
    from datadog_api_client.v2.model.snowflake_integration_account_private_key_auth_response import (
        SnowflakeIntegrationAccountPrivateKeyAuthResponse,
    )


class SnowflakeIntegrationAccountResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.snowflake_integration_account_authentication_response import (
            SnowflakeIntegrationAccountAuthenticationResponse,
        )
        from datadog_api_client.v2.model.snowflake_integration_dataflows_response import (
            SnowflakeIntegrationDataflowsResponse,
        )
        from datadog_api_client.v2.model.snowflake_integration_account_settings_response import (
            SnowflakeIntegrationAccountSettingsResponse,
        )

        return {
            "authentication": (SnowflakeIntegrationAccountAuthenticationResponse,),
            "dataflows": (SnowflakeIntegrationDataflowsResponse,),
            "name": (str,),
            "settings": (SnowflakeIntegrationAccountSettingsResponse,),
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
        settings: SnowflakeIntegrationAccountSettingsResponse,
        authentication: Union[
            SnowflakeIntegrationAccountAuthenticationResponse,
            SnowflakeIntegrationAccountPrivateKeyAuthResponse,
            UnsetType,
        ] = unset,
        dataflows: Union[SnowflakeIntegrationDataflowsResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a Snowflake integration account returned in responses.

        :param authentication: Authentication configured on the Snowflake integration account.
        :type authentication: SnowflakeIntegrationAccountAuthenticationResponse, optional

        :param dataflows: Data Datadog collects from Snowflake, keyed by dataflow id.
        :type dataflows: SnowflakeIntegrationDataflowsResponse, optional

        :param name: Human-readable name of the Snowflake integration account.
        :type name: str

        :param settings: Settings configured on the Snowflake integration account.
        :type settings: SnowflakeIntegrationAccountSettingsResponse
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.name = name
        self_.settings = settings
