# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SalesforceIncidentsTemplatePriority(ModelSimple):
    """
    Priority of the Salesforce incident created from this template.

    :param value: Must be one of ["Critical", "High", "Moderate", "Low"].
    :type value: str
    """

    allowed_values = {
        "Critical",
        "High",
        "Moderate",
        "Low",
    }
    CRITICAL: ClassVar["SalesforceIncidentsTemplatePriority"]
    HIGH: ClassVar["SalesforceIncidentsTemplatePriority"]
    MODERATE: ClassVar["SalesforceIncidentsTemplatePriority"]
    LOW: ClassVar["SalesforceIncidentsTemplatePriority"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SalesforceIncidentsTemplatePriority.CRITICAL = SalesforceIncidentsTemplatePriority("Critical")
SalesforceIncidentsTemplatePriority.HIGH = SalesforceIncidentsTemplatePriority("High")
SalesforceIncidentsTemplatePriority.MODERATE = SalesforceIncidentsTemplatePriority("Moderate")
SalesforceIncidentsTemplatePriority.LOW = SalesforceIncidentsTemplatePriority("Low")
