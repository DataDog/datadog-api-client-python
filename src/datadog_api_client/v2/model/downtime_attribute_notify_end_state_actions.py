# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DowntimeAttributeNotifyEndStateActions(ModelSimple):
    """
    Action that will trigger a monitor notification if the downtime is in the `notify_end_types` state.

    :param value: Must be one of ["canceled", "expired"].
    :type value: str
    """

    allowed_values = {
        "canceled",
        "expired",
    }
    CANCELED: ClassVar["DowntimeAttributeNotifyEndStateActions"]
    EXPIRED: ClassVar["DowntimeAttributeNotifyEndStateActions"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DowntimeAttributeNotifyEndStateActions.CANCELED = DowntimeAttributeNotifyEndStateActions("canceled")
DowntimeAttributeNotifyEndStateActions.EXPIRED = DowntimeAttributeNotifyEndStateActions("expired")
