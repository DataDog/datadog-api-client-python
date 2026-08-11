# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.twilio_authentication import TwilioAuthentication
    from datadog_api_client.v2.model.twilio_dataflow import TwilioDataflow
    from datadog_api_client.v2.model.integration_account_permissions import IntegrationAccountPermissions
    from datadog_api_client.v2.model.twilio_settings import TwilioSettings
    from datadog_api_client.v2.model.twilio_basic_auth import TwilioBasicAuth


class TwilioAccountAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.twilio_authentication import TwilioAuthentication
        from datadog_api_client.v2.model.twilio_dataflow import TwilioDataflow
        from datadog_api_client.v2.model.integration_account_permissions import IntegrationAccountPermissions
        from datadog_api_client.v2.model.twilio_settings import TwilioSettings

        return {
            "authentication": (TwilioAuthentication,),
            "dataflows": ([TwilioDataflow],),
            "name": (str,),
            "permissions": (IntegrationAccountPermissions,),
            "settings": (TwilioSettings,),
        }

    attribute_map = {
        "authentication": "authentication",
        "dataflows": "dataflows",
        "name": "name",
        "permissions": "permissions",
        "settings": "settings",
    }
    read_only_vars = {
        "permissions",
    }

    def __init__(
        self_,
        authentication: Union[TwilioAuthentication, TwilioBasicAuth],
        name: str,
        dataflows: Union[List[TwilioDataflow], UnsetType] = unset,
        permissions: Union[IntegrationAccountPermissions, UnsetType] = unset,
        settings: Union[TwilioSettings, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a Twilio integration account. The Twilio configuration is hoisted directly onto the attributes; there is no interface wrapper because the ``twilio`` interface is fixed by the endpoint path.

        :param authentication: Authentication methods supported by the Twilio interface. Exactly one is set, selected by its ``type``.
        :type authentication: TwilioAuthentication

        :param dataflows: Dataflows for the Twilio interface.
        :type dataflows: [TwilioDataflow], optional

        :param name: Human-readable name of the account.
        :type name: str

        :param permissions: Read-only permission information for the account, derived from its restriction policy.
        :type permissions: IntegrationAccountPermissions, optional

        :param settings: Twilio interface settings.
        :type settings: TwilioSettings, optional
        """
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        if permissions is not unset:
            kwargs["permissions"] = permissions
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)

        self_.authentication = authentication
        self_.name = name
