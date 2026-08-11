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
    from datadog_api_client.v2.model.twilio_basic_auth import TwilioBasicAuth


class TwilioAccountUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.twilio_authentication import TwilioAuthentication
        from datadog_api_client.v2.model.twilio_dataflow import TwilioDataflow
        from datadog_api_client.v2.model.twilio_settings_update import TwilioSettingsUpdate

        return {
            "authentication": (TwilioAuthentication,),
            "dataflows": ([TwilioDataflow],),
            "name": (str,),
            "settings": (TwilioSettingsUpdate,),
        }

    attribute_map = {
        "authentication": "authentication",
        "dataflows": "dataflows",
        "name": "name",
        "settings": "settings",
    }

    def __init__(
        self_,
        authentication: Union[TwilioAuthentication, TwilioBasicAuth, UnsetType] = unset,
        dataflows: Union[List[TwilioDataflow], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        settings: Union[TwilioSettingsUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        Updatable attributes of a Twilio integration account. Every field is optional; only the fields provided are changed.

        :param authentication: Authentication methods supported by the Twilio interface. Exactly one is set, selected by its ``type``.
        :type authentication: TwilioAuthentication, optional

        :param dataflows: Dataflows for the Twilio interface.
        :type dataflows: [TwilioDataflow], optional

        :param name: Human-readable name of the account.
        :type name: str, optional

        :param settings: Partial Twilio interface settings for updates.
        :type settings: TwilioSettingsUpdate, optional
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        if name is not unset:
            kwargs["name"] = name
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)
