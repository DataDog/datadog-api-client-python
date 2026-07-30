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
    from datadog_api_client.v2.model.twilio_settings import TwilioSettings
    from datadog_api_client.v2.model.twilio_interface_type import TwilioInterfaceType
    from datadog_api_client.v2.model.twilio_basic_auth import TwilioBasicAuth


class TwilioInterface(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.twilio_authentication import TwilioAuthentication
        from datadog_api_client.v2.model.twilio_dataflow import TwilioDataflow
        from datadog_api_client.v2.model.twilio_settings import TwilioSettings
        from datadog_api_client.v2.model.twilio_interface_type import TwilioInterfaceType

        return {
            "authentication": (TwilioAuthentication,),
            "dataflows": ([TwilioDataflow],),
            "settings": (TwilioSettings,),
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
        authentication: Union[TwilioAuthentication, TwilioBasicAuth],
        type: TwilioInterfaceType,
        dataflows: Union[List[TwilioDataflow], UnsetType] = unset,
        settings: Union[TwilioSettings, UnsetType] = unset,
        **kwargs,
    ):
        """
        Twilio interface (source-type) configuration.

        :param authentication: Authentication methods supported by the Twilio interface. Exactly one is set, selected by its ``type``.
        :type authentication: TwilioAuthentication

        :param dataflows: Dataflows for the Twilio interface.
        :type dataflows: [TwilioDataflow], optional

        :param settings: Twilio interface settings.
        :type settings: TwilioSettings, optional

        :param type: Interface discriminator for Twilio.
        :type type: TwilioInterfaceType
        """
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)

        self_.authentication = authentication
        self_.type = type
