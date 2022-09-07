# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SecurityMonitoringSignalArchiveReason(ModelSimple):
    """
    Reason a signal is archived.

    :param value: Must be one of ["none", "false_positive", "testing_or_maintenance", "other"].
    :type value: str
    """

    allowed_values = {
        "none",
        "false_positive",
        "testing_or_maintenance",
        "other",
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringSignalArchiveReason.NONE = SecurityMonitoringSignalArchiveReason("none")
SecurityMonitoringSignalArchiveReason.FALSE_POSITIVE = SecurityMonitoringSignalArchiveReason("false_positive")
SecurityMonitoringSignalArchiveReason.TESTING_OR_MAINTENANCE = SecurityMonitoringSignalArchiveReason(
    "testing_or_maintenance"
)
SecurityMonitoringSignalArchiveReason.OTHER = SecurityMonitoringSignalArchiveReason("other")
