# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class ExperimentsBanditScheduledEndFailureV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "failed_at": (datetime,),
            "reason": (str,),
        }

    attribute_map = {
        "failed_at": "failed_at",
        "reason": "reason",
    }

    def __init__(self_, failed_at: datetime, reason: str, **kwargs):
        """
        Why the scheduled end couldn't run. It isn't retried until the end or fallback changes. Absent when there's no failure.

        :param failed_at: When the scheduled end failed.
        :type failed_at: datetime

        :param reason: Why the scheduled end failed.
        :type reason: str
        """
        super().__init__(kwargs)

        self_.failed_at = failed_at
        self_.reason = reason
