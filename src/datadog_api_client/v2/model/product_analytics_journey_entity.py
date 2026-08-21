# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsJourneyEntity(ModelSimple):
    """
    The kind of entity returned by a journey list query.

    :param value: Must be one of ["session", "user", "account"].
    :type value: str
    """

    allowed_values = {
        "session",
        "user",
        "account",
    }
    SESSION: ClassVar["ProductAnalyticsJourneyEntity"]
    USER: ClassVar["ProductAnalyticsJourneyEntity"]
    ACCOUNT: ClassVar["ProductAnalyticsJourneyEntity"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsJourneyEntity.SESSION = ProductAnalyticsJourneyEntity("session")
ProductAnalyticsJourneyEntity.USER = ProductAnalyticsJourneyEntity("user")
ProductAnalyticsJourneyEntity.ACCOUNT = ProductAnalyticsJourneyEntity("account")
