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


class TwilioIntegrationAccountUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.twilio_interface_update import TwilioInterfaceUpdate

        return {
            "interface": (TwilioInterfaceUpdate,),
            "name": (str,),
        }

    attribute_map = {
        "interface": "interface",
        "name": "name",
    }

    def __init__(
        self_, interface: Union[TwilioInterfaceUpdate, UnsetType] = unset, name: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Updatable attributes of a Twilio integration account. Every field is optional; only the fields provided are changed.

        :param interface: Partial Twilio interface (source-type) configuration for updates.
        :type interface: TwilioInterfaceUpdate, optional

        :param name: Human-readable name of the account.
        :type name: str, optional
        """
        if interface is not unset:
            kwargs["interface"] = interface
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
