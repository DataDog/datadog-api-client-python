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
    from datadog_api_client.v2.model.twilio_interface_update import TwilioInterfaceUpdate
    from datadog_api_client.v2.model.twilio_integration_type import TwilioIntegrationType


class TwilioIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.twilio_interface_update import TwilioInterfaceUpdate
        from datadog_api_client.v2.model.twilio_integration_type import TwilioIntegrationType

        return {
            "interface": (TwilioInterfaceUpdate,),
            "type": (TwilioIntegrationType,),
        }

    attribute_map = {
        "interface": "interface",
        "type": "type",
    }

    def __init__(
        self_, type: TwilioIntegrationType, interface: Union[TwilioInterfaceUpdate, UnsetType] = unset, **kwargs
    ):
        """
        Partial Twilio integration configuration for updates.

        :param interface: Partial Twilio interface (source-type) configuration for updates.
        :type interface: TwilioInterfaceUpdate, optional

        :param type: Integration discriminator for Twilio.
        :type type: TwilioIntegrationType
        """
        if interface is not unset:
            kwargs["interface"] = interface
        super().__init__(kwargs)

        self_.type = type
