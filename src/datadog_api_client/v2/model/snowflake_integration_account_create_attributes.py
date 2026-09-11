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
    from datadog_api_client.v2.model.snowflake_integration_account_authentication_request import (
        SnowflakeIntegrationAccountAuthenticationRequest,
    )
    from datadog_api_client.v2.model.snowflake_integration_dataflows_request import SnowflakeIntegrationDataflowsRequest
    from datadog_api_client.v2.model.snowflake_integration_account_settings_request import (
        SnowflakeIntegrationAccountSettingsRequest,
    )


class SnowflakeIntegrationAccountCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.snowflake_integration_account_authentication_request import (
            SnowflakeIntegrationAccountAuthenticationRequest,
        )
        from datadog_api_client.v2.model.snowflake_integration_dataflows_request import (
            SnowflakeIntegrationDataflowsRequest,
        )
        from datadog_api_client.v2.model.snowflake_integration_account_settings_request import (
            SnowflakeIntegrationAccountSettingsRequest,
        )

        return {
            "authentication": (SnowflakeIntegrationAccountAuthenticationRequest,),
            "dataflows": (SnowflakeIntegrationDataflowsRequest,),
            "name": (str,),
            "settings": (SnowflakeIntegrationAccountSettingsRequest,),
        }

    attribute_map = {
        "authentication": "authentication",
        "dataflows": "dataflows",
        "name": "name",
        "settings": "settings",
    }

    def __init__(
        self_,
        authentication: SnowflakeIntegrationAccountAuthenticationRequest,
        name: str,
        settings: SnowflakeIntegrationAccountSettingsRequest,
        dataflows: Union[SnowflakeIntegrationDataflowsRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Writable attributes used to create a Snowflake integration account.

        :param authentication: RSA key pair authentication, the only method Snowflake integration accounts support. Generate an RSA key pair and assign the public key to the Snowflake user named in ``settings.username``. Because an update replaces this object as a whole, every required field must be sent again on each update, even when only one of them is changing.
        :type authentication: SnowflakeIntegrationAccountAuthenticationRequest

        :param dataflows: Data Datadog collects from Snowflake, keyed by dataflow id. Each dataflow turns on a distinct kind of collection: set ``enabled`` to start or stop it, and use ``settings`` to configure what it collects. Defaults listed on each dataflow apply when the account is created; on update, omitted fields keep their current values. Every dataflow reads from Snowflake as the user in ``settings.username`` , so that user's role must be granted access to the underlying views; a dataflow enabled without those grants is stored but collects no data.
        :type dataflows: SnowflakeIntegrationDataflowsRequest, optional

        :param name: Human-readable name of the Snowflake integration account. Must be
            unique within your Datadog organization.
        :type name: str

        :param settings: Settings for creating the Snowflake integration account.
        :type settings: SnowflakeIntegrationAccountSettingsRequest
        """
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.authentication = authentication
        self_.name = name
        self_.settings = settings
