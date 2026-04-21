# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringSKU(ModelSimple):
    """
    The SIEM pricing model (SKU) for the organization

    :param value: Must be one of ["per_gb_analyzed", "per_event_in_siem_index_2023", "add_on_2024"].
    :type value: str
    """

    allowed_values = {
        "per_gb_analyzed",
        "per_event_in_siem_index_2023",
        "add_on_2024",
    }
    PER_GB_ANALYZED: ClassVar["SecurityMonitoringSKU"]
    PER_EVENT_IN_SIEM_INDEX_2023: ClassVar["SecurityMonitoringSKU"]
    ADD_ON_2024: ClassVar["SecurityMonitoringSKU"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringSKU.PER_GB_ANALYZED = SecurityMonitoringSKU("per_gb_analyzed")
SecurityMonitoringSKU.PER_EVENT_IN_SIEM_INDEX_2023 = SecurityMonitoringSKU("per_event_in_siem_index_2023")
SecurityMonitoringSKU.ADD_ON_2024 = SecurityMonitoringSKU("add_on_2024")
