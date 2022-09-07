# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class EventAlertType(ModelSimple):
    """
    If an alert event is enabled, set its type.
        For example, `error`, `warning`, `info`, `success`, `user_update`,
        `recommendation`, and `snapshot`.

    :param value: Must be one of ["error", "warning", "info", "success", "user_update", "recommendation", "snapshot"].
    :type value: str
    """

    allowed_values = {
        "error",
        "warning",
        "info",
        "success",
        "user_update",
        "recommendation",
        "snapshot",
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EventAlertType.ERROR = EventAlertType("error")
EventAlertType.WARNING = EventAlertType("warning")
EventAlertType.INFO = EventAlertType("info")
EventAlertType.SUCCESS = EventAlertType("success")
EventAlertType.USER_UPDATE = EventAlertType("user_update")
EventAlertType.RECOMMENDATION = EventAlertType("recommendation")
EventAlertType.SNAPSHOT = EventAlertType("snapshot")
