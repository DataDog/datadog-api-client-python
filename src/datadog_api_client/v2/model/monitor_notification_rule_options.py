# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MonitorNotificationRuleOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "is_threaded": (bool,),
        }

    attribute_map = {
        "is_threaded": "is_threaded",
    }

    def __init__(self_, is_threaded: bool, **kwargs):
        """
        Additional options for the monitor notification rule.

        :param is_threaded: Whether notifications from this rule are threaded. When ``true`` , follow-up notifications for the same monitor alert are posted in Slack as replies to the first notification.
            Cannot be ``true`` when ``bundle_config`` is set.
        :type is_threaded: bool
        """
        super().__init__(kwargs)

        self_.is_threaded = is_threaded
