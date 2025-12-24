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


class TeamNotificationRuleAttributesPagerduty(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "service_name": (str,),
        }

    attribute_map = {
        "service_name": "service_name",
    }

    def __init__(self_, service_name: Union[str, UnsetType] = unset, **kwargs):
        """
        PagerDuty notification settings for the team

        :param service_name: Service name for PagerDuty
        :type service_name: str, optional
        """
        if service_name is not unset:
            kwargs["service_name"] = service_name
        super().__init__(kwargs)
