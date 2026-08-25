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
    from datadog_api_client.v2.model.twilio_integration_account_authentication_response import (
        TwilioIntegrationAccountAuthenticationResponse,
    )
    from datadog_api_client.v2.model.twilio_integration_dataflows_response import TwilioIntegrationDataflowsResponse
    from datadog_api_client.v2.model.twilio_integration_account_settings_response import (
        TwilioIntegrationAccountSettingsResponse,
    )
    from datadog_api_client.v2.model.integration_account_basic_auth_response import IntegrationAccountBasicAuthResponse


class TwilioIntegrationAccountResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.twilio_integration_account_authentication_response import (
            TwilioIntegrationAccountAuthenticationResponse,
        )
        from datadog_api_client.v2.model.twilio_integration_dataflows_response import TwilioIntegrationDataflowsResponse
        from datadog_api_client.v2.model.twilio_integration_account_settings_response import (
            TwilioIntegrationAccountSettingsResponse,
        )

        return {
            "authentication": (TwilioIntegrationAccountAuthenticationResponse,),
            "dataflows": (TwilioIntegrationDataflowsResponse,),
            "name": (str,),
            "settings": (TwilioIntegrationAccountSettingsResponse,),
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
        settings: TwilioIntegrationAccountSettingsResponse,
        authentication: Union[
            TwilioIntegrationAccountAuthenticationResponse, IntegrationAccountBasicAuthResponse, UnsetType
        ] = unset,
        dataflows: Union[TwilioIntegrationDataflowsResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a Twilio integration account returned in responses.

        :param authentication: Authentication configured on the Twilio integration account.
        :type authentication: TwilioIntegrationAccountAuthenticationResponse, optional

        :param dataflows: Dataflows configured on the Twilio integration account, keyed by dataflow id.
        :type dataflows: TwilioIntegrationDataflowsResponse, optional

        :param name: Human-readable name of the Twilio integration account.
        :type name: str

        :param settings: Settings configured on the Twilio integration account.
        :type settings: TwilioIntegrationAccountSettingsResponse
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.name = name
        self_.settings = settings
