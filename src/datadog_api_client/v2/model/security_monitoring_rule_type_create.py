# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SecurityMonitoringRuleTypeCreate(ModelSimple):
    """
    The rule type.

    :param value: Must be one of ["log_detection", "workload_security"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "LOG_DETECTION": "log_detection",
            "WORKLOAD_SECURITY": "workload_security",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
