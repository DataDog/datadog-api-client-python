# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentTypeSlugSource(ModelSimple):
    """
    When set to `servicenow`, incidents will display the ServiceNow record ID instead of the public ID. If no ServiceNow integration exists, the public ID will be displayed.

    :param value: If omitted defaults to "default". Must be one of ["default", "servicenow"].
    :type value: str
    """

    allowed_values = {
        "default",
        "servicenow",
    }
    DEFAULT: ClassVar["IncidentTypeSlugSource"]
    SERVICENOW: ClassVar["IncidentTypeSlugSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentTypeSlugSource.DEFAULT = IncidentTypeSlugSource("default")
IncidentTypeSlugSource.SERVICENOW = IncidentTypeSlugSource("servicenow")
