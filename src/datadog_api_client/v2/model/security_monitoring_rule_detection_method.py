# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SecurityMonitoringRuleDetectionMethod(ModelSimple):
    """
    The detection method.

    :param value: Must be one of ["threshold", "new_value", "anomaly_detection", "impossible_travel", "hardcoded"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "THRESHOLD": "threshold",
            "NEW_VALUE": "new_value",
            "ANOMALY_DETECTION": "anomaly_detection",
            "IMPOSSIBLE_TRAVEL": "impossible_travel",
            "HARDCODED": "hardcoded",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
