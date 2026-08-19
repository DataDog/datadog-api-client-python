# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MonitorNotificationRuleBundleConfig(ModelNormal):
    validations = {
        "duration": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "duration": (int,),
        }

    attribute_map = {
        "duration": "duration",
    }

    def __init__(self_, duration: int, **kwargs):
        """
        Use bundle config to enable alert bundling to reduce monitor signal noises. **Note** : This feature is in preview and is subject to change.
        If you have any feedback, contact `Datadog support <https://docs.datadoghq.com/help/>`_.

        :param duration: Duration of the bundling period.
        :type duration: int
        """
        super().__init__(kwargs)

        self_.duration = duration
