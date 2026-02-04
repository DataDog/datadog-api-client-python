# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringContentPackTimestampBucket(ModelSimple):
    """
    Timestamp bucket indicating when logs were last collected

    :param value: Must be one of ["not_seen", "within_24_hours", "within_24_to_72_hours", "over_72h_to_30d", "over_30d"].
    :type value: str
    """

    allowed_values = {
        "not_seen",
        "within_24_hours",
        "within_24_to_72_hours",
        "over_72h_to_30d",
        "over_30d",
    }
    NOT_SEEN: ClassVar["SecurityMonitoringContentPackTimestampBucket"]
    WITHIN_24_HOURS: ClassVar["SecurityMonitoringContentPackTimestampBucket"]
    WITHIN_24_TO_72_HOURS: ClassVar["SecurityMonitoringContentPackTimestampBucket"]
    OVER_72H_TO_30D: ClassVar["SecurityMonitoringContentPackTimestampBucket"]
    OVER_30D: ClassVar["SecurityMonitoringContentPackTimestampBucket"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringContentPackTimestampBucket.NOT_SEEN = SecurityMonitoringContentPackTimestampBucket("not_seen")
SecurityMonitoringContentPackTimestampBucket.WITHIN_24_HOURS = SecurityMonitoringContentPackTimestampBucket(
    "within_24_hours"
)
SecurityMonitoringContentPackTimestampBucket.WITHIN_24_TO_72_HOURS = SecurityMonitoringContentPackTimestampBucket(
    "within_24_to_72_hours"
)
SecurityMonitoringContentPackTimestampBucket.OVER_72H_TO_30D = SecurityMonitoringContentPackTimestampBucket(
    "over_72h_to_30d"
)
SecurityMonitoringContentPackTimestampBucket.OVER_30D = SecurityMonitoringContentPackTimestampBucket("over_30d")
