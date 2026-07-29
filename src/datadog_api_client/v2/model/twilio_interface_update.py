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
    from datadog_api_client.v2.model.twilio_settings_update import TwilioSettingsUpdate
    from datadog_api_client.v2.model.twilio_interface_type import TwilioInterfaceType
    from datadog_api_client.v2.model.twilio_basic_auth import TwilioBasicAuth


class TwilioInterfaceUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.twilio_authentication import TwilioAuthentication
        from datadog_api_client.v2.model.twilio_dataflow import TwilioDataflow
        from datadog_api_client.v2.model.twilio_settings_update import TwilioSettingsUpdate
        from datadog_api_client.v2.model.twilio_interface_type import TwilioInterfaceType

        return {
            "authentication": (TwilioAuthentication,),
            "dataflows": ([TwilioDataflow],),
            "settings": (TwilioSettingsUpdate,),
            "type": (TwilioInterfaceType,),
        }

    attribute_map = {
        "authentication": "authentication",
        "dataflows": "dataflows",
        "settings": "settings",
        "type": "type",
    }

    def __init__(
        self_,
        type: TwilioInterfaceType,
        authentication: Union[TwilioAuthentication, TwilioBasicAuth, UnsetType] = unset,
        dataflows: Union[List[TwilioDataflow], UnsetType] = unset,
        settings: Union[TwilioSettingsUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        Partial Twilio interface (source-type) configuration for updates.

        :param authentication: Authentication methods supported by the Twilio interface. Exactly one is set, selected by its ``type``.
        :type authentication: TwilioAuthentication, optional

        :param dataflows: Dataflows for the Twilio interface.
        :type dataflows: [TwilioDataflow], optional

        :param settings: Partial Twilio interface settings for updates.
        :type settings: TwilioSettingsUpdate, optional

        :param type: Interface discriminator for Twilio.
        :type type: TwilioInterfaceType
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)

        self_.type = type
