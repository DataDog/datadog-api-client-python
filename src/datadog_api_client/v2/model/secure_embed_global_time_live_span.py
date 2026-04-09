# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecureEmbedGlobalTimeLiveSpan(ModelSimple):
    """
    Dashboard global time live_span selection.

    :param value: Must be one of ["15m", "1h", "4h", "1d", "2d", "1w", "1mo", "3mo"].
    :type value: str
    """

    allowed_values = {
        "15m",
        "1h",
        "4h",
        "1d",
        "2d",
        "1w",
        "1mo",
        "3mo",
    }
    PAST_FIFTEEN_MINUTES: ClassVar["SecureEmbedGlobalTimeLiveSpan"]
    PAST_ONE_HOUR: ClassVar["SecureEmbedGlobalTimeLiveSpan"]
    PAST_FOUR_HOURS: ClassVar["SecureEmbedGlobalTimeLiveSpan"]
    PAST_ONE_DAY: ClassVar["SecureEmbedGlobalTimeLiveSpan"]
    PAST_TWO_DAYS: ClassVar["SecureEmbedGlobalTimeLiveSpan"]
    PAST_ONE_WEEK: ClassVar["SecureEmbedGlobalTimeLiveSpan"]
    PAST_ONE_MONTH: ClassVar["SecureEmbedGlobalTimeLiveSpan"]
    PAST_THREE_MONTHS: ClassVar["SecureEmbedGlobalTimeLiveSpan"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecureEmbedGlobalTimeLiveSpan.PAST_FIFTEEN_MINUTES = SecureEmbedGlobalTimeLiveSpan("15m")
SecureEmbedGlobalTimeLiveSpan.PAST_ONE_HOUR = SecureEmbedGlobalTimeLiveSpan("1h")
SecureEmbedGlobalTimeLiveSpan.PAST_FOUR_HOURS = SecureEmbedGlobalTimeLiveSpan("4h")
SecureEmbedGlobalTimeLiveSpan.PAST_ONE_DAY = SecureEmbedGlobalTimeLiveSpan("1d")
SecureEmbedGlobalTimeLiveSpan.PAST_TWO_DAYS = SecureEmbedGlobalTimeLiveSpan("2d")
SecureEmbedGlobalTimeLiveSpan.PAST_ONE_WEEK = SecureEmbedGlobalTimeLiveSpan("1w")
SecureEmbedGlobalTimeLiveSpan.PAST_ONE_MONTH = SecureEmbedGlobalTimeLiveSpan("1mo")
SecureEmbedGlobalTimeLiveSpan.PAST_THREE_MONTHS = SecureEmbedGlobalTimeLiveSpan("3mo")
