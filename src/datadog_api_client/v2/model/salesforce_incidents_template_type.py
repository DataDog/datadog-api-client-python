# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SalesforceIncidentsTemplateType(ModelSimple):
    """
    Salesforce incident template resource type.

    :param value: If omitted defaults to "salesforce-incidents-incident-template". Must be one of ["salesforce-incidents-incident-template"].
    :type value: str
    """

    allowed_values = {
        "salesforce-incidents-incident-template",
    }
    SALESFORCE_INCIDENTS_INCIDENT_TEMPLATE: ClassVar["SalesforceIncidentsTemplateType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SalesforceIncidentsTemplateType.SALESFORCE_INCIDENTS_INCIDENT_TEMPLATE = SalesforceIncidentsTemplateType(
    "salesforce-incidents-incident-template"
)
