# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsJourneySearchGraphFilterName(ModelSimple):
    """
    The journey-level metric the graph filter applies to.

    :param value: Must be one of ["__dd.time_to_convert", "__dd.session", "__dd.dropoff_rate"].
    :type value: str
    """

    allowed_values = {
        "__dd.time_to_convert",
        "__dd.session",
        "__dd.dropoff_rate",
    }
    TIME_TO_CONVERT: ClassVar["ProductAnalyticsJourneySearchGraphFilterName"]
    SESSION: ClassVar["ProductAnalyticsJourneySearchGraphFilterName"]
    DROPOFF_RATE: ClassVar["ProductAnalyticsJourneySearchGraphFilterName"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsJourneySearchGraphFilterName.TIME_TO_CONVERT = ProductAnalyticsJourneySearchGraphFilterName(
    "__dd.time_to_convert"
)
ProductAnalyticsJourneySearchGraphFilterName.SESSION = ProductAnalyticsJourneySearchGraphFilterName("__dd.session")
ProductAnalyticsJourneySearchGraphFilterName.DROPOFF_RATE = ProductAnalyticsJourneySearchGraphFilterName(
    "__dd.dropoff_rate"
)
