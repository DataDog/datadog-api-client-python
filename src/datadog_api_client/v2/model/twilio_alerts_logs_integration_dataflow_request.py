# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class TwilioAlertsLogsIntegrationDataflowRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "enabled": (bool,),
        }

    attribute_map = {
        "enabled": "enabled",
    }

    def __init__(self_, enabled: Union[bool, UnsetType] = unset, **kwargs):
        """
        Twilio Alert resource logs, which detail the errors and warnings raised when Twilio makes a webhook request to your server or when your application calls the Twilio REST API. This is the one kind of data the integration collects by default.

        :param enabled: Whether Datadog collects this data. Defaults to ``true`` ; set to ``false`` to stop collection.
        :type enabled: bool, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        super().__init__(kwargs)
