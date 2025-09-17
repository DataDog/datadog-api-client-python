# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentImpactRelatedObject(ModelSimple):
    """
    A reference to a resource related to an incident impact.

    :param value: Must be one of ["incident", "created_by_user", "last_modified_by_user"].
    :type value: str
    """

    allowed_values = {
        "incident",
        "created_by_user",
        "last_modified_by_user",
    }
    INCIDENT: ClassVar["IncidentImpactRelatedObject"]
    CREATED_BY_USER: ClassVar["IncidentImpactRelatedObject"]
    LAST_MODIFIED_BY_USER: ClassVar["IncidentImpactRelatedObject"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentImpactRelatedObject.INCIDENT = IncidentImpactRelatedObject("incident")
IncidentImpactRelatedObject.CREATED_BY_USER = IncidentImpactRelatedObject("created_by_user")
IncidentImpactRelatedObject.LAST_MODIFIED_BY_USER = IncidentImpactRelatedObject("last_modified_by_user")
