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
    from datadog_api_client.v2.model.twilio_interface import TwilioInterface
    from datadog_api_client.v2.model.integration_account_permissions import IntegrationAccountPermissions


class TwilioIntegrationAccountAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.twilio_interface import TwilioInterface
        from datadog_api_client.v2.model.integration_account_permissions import IntegrationAccountPermissions

        return {
            "interface": (TwilioInterface,),
            "name": (str,),
            "permissions": (IntegrationAccountPermissions,),
        }

    attribute_map = {
        "interface": "interface",
        "name": "name",
        "permissions": "permissions",
    }
    read_only_vars = {
        "permissions",
    }

    def __init__(
        self_,
        interface: TwilioInterface,
        name: str,
        permissions: Union[IntegrationAccountPermissions, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a Twilio integration account.

        :param interface: Twilio interface (source-type) configuration.
        :type interface: TwilioInterface

        :param name: Human-readable name of the account.
        :type name: str

        :param permissions: Read-only permission information for the account, derived from its restriction policy.
        :type permissions: IntegrationAccountPermissions, optional
        """
        if permissions is not unset:
            kwargs["permissions"] = permissions
        super().__init__(kwargs)

        self_.interface = interface
        self_.name = name
