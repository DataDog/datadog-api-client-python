# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ScatterplotDataProjectionQueryStorage(ModelSimple):
    """
    Storage tier to query.

    :param value: Must be one of ["live", "hot", "habanero", "online_archives", "driveline", "flex_tier", "case_insensitive", "cloud_prem"].
    :type value: str
    """

    allowed_values = {
        "live",
        "hot",
        "habanero",
        "online_archives",
        "driveline",
        "flex_tier",
        "case_insensitive",
        "cloud_prem",
    }
    LIVE: ClassVar["ScatterplotDataProjectionQueryStorage"]
    HOT: ClassVar["ScatterplotDataProjectionQueryStorage"]
    HABANERO: ClassVar["ScatterplotDataProjectionQueryStorage"]
    ONLINE_ARCHIVES: ClassVar["ScatterplotDataProjectionQueryStorage"]
    DRIVELINE: ClassVar["ScatterplotDataProjectionQueryStorage"]
    FLEX_TIER: ClassVar["ScatterplotDataProjectionQueryStorage"]
    CASE_INSENSITIVE: ClassVar["ScatterplotDataProjectionQueryStorage"]
    CLOUD_PREM: ClassVar["ScatterplotDataProjectionQueryStorage"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ScatterplotDataProjectionQueryStorage.LIVE = ScatterplotDataProjectionQueryStorage("live")
ScatterplotDataProjectionQueryStorage.HOT = ScatterplotDataProjectionQueryStorage("hot")
ScatterplotDataProjectionQueryStorage.HABANERO = ScatterplotDataProjectionQueryStorage("habanero")
ScatterplotDataProjectionQueryStorage.ONLINE_ARCHIVES = ScatterplotDataProjectionQueryStorage("online_archives")
ScatterplotDataProjectionQueryStorage.DRIVELINE = ScatterplotDataProjectionQueryStorage("driveline")
ScatterplotDataProjectionQueryStorage.FLEX_TIER = ScatterplotDataProjectionQueryStorage("flex_tier")
ScatterplotDataProjectionQueryStorage.CASE_INSENSITIVE = ScatterplotDataProjectionQueryStorage("case_insensitive")
ScatterplotDataProjectionQueryStorage.CLOUD_PREM = ScatterplotDataProjectionQueryStorage("cloud_prem")
