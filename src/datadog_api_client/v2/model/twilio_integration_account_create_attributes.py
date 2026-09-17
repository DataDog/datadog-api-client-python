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
    from datadog_api_client.v2.model.twilio_integration_account_authentication_request import (
        TwilioIntegrationAccountAuthenticationRequest,
    )
    from datadog_api_client.v2.model.twilio_integration_dataflows_request import TwilioIntegrationDataflowsRequest
    from datadog_api_client.v2.model.twilio_integration_account_settings_request import (
        TwilioIntegrationAccountSettingsRequest,
    )
    from datadog_api_client.v2.model.twilio_integration_account_basic_auth_request import (
        TwilioIntegrationAccountBasicAuthRequest,
    )


class TwilioIntegrationAccountCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.twilio_integration_account_authentication_request import (
            TwilioIntegrationAccountAuthenticationRequest,
        )
        from datadog_api_client.v2.model.twilio_integration_dataflows_request import TwilioIntegrationDataflowsRequest
        from datadog_api_client.v2.model.twilio_integration_account_settings_request import (
            TwilioIntegrationAccountSettingsRequest,
        )

        return {
            "authentication": (TwilioIntegrationAccountAuthenticationRequest,),
            "dataflows": (TwilioIntegrationDataflowsRequest,),
            "name": (str,),
            "settings": (TwilioIntegrationAccountSettingsRequest,),
        }

    attribute_map = {
        "authentication": "authentication",
        "dataflows": "dataflows",
        "name": "name",
        "settings": "settings",
    }

    def __init__(
        self_,
        authentication: Union[TwilioIntegrationAccountAuthenticationRequest, TwilioIntegrationAccountBasicAuthRequest],
        name: str,
        settings: TwilioIntegrationAccountSettingsRequest,
        dataflows: Union[TwilioIntegrationDataflowsRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Writable attributes used to create a Twilio integration account.

        :param authentication: Authentication for creating the Twilio integration account. Exactly one method is set.
        :type authentication: TwilioIntegrationAccountAuthenticationRequest

        :param dataflows: Data Datadog collects from Twilio, keyed by dataflow id. Each dataflow turns on a distinct kind of collection: set ``enabled`` to start or stop it. Defaults listed on each dataflow apply when the account is created; on update, omitted fields keep their current values. Where a dataflow depends on a Twilio feature being enabled, that prerequisite is noted on the dataflow; a dataflow enabled without it is stored but collects no data.
        :type dataflows: TwilioIntegrationDataflowsRequest, optional

        :param name: Human-readable name of the Twilio integration account.
        :type name: str

        :param settings: Settings for creating the Twilio integration account.
        :type settings: TwilioIntegrationAccountSettingsRequest
        """
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.authentication = authentication
        self_.name = name
        self_.settings = settings
