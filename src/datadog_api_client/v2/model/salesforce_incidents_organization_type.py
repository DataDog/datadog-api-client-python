# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SalesforceIncidentsOrganizationType(ModelSimple):
    """
    Salesforce organization resource type.

    :param value: If omitted defaults to "salesforce-incidents-org". Must be one of ["salesforce-incidents-org"].
    :type value: str
    """

    allowed_values = {
        "salesforce-incidents-org",
    }
    SALESFORCE_INCIDENTS_ORG: ClassVar["SalesforceIncidentsOrganizationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SalesforceIncidentsOrganizationType.SALESFORCE_INCIDENTS_ORG = SalesforceIncidentsOrganizationType(
    "salesforce-incidents-org"
)
