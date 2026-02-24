# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentImportRelatedObject(ModelSimple):
    """
    Object related to an incident that can be included in the response.

    :param value: Must be one of ["last_modified_by_user", "created_by_user", "commander_user", "declared_by_user", "incident_type"].
    :type value: str
    """

    allowed_values = {
        "last_modified_by_user",
        "created_by_user",
        "commander_user",
        "declared_by_user",
        "incident_type",
    }
    LAST_MODIFIED_BY_USER: ClassVar["IncidentImportRelatedObject"]
    CREATED_BY_USER: ClassVar["IncidentImportRelatedObject"]
    COMMANDER_USER: ClassVar["IncidentImportRelatedObject"]
    DECLARED_BY_USER: ClassVar["IncidentImportRelatedObject"]
    INCIDENT_TYPE: ClassVar["IncidentImportRelatedObject"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentImportRelatedObject.LAST_MODIFIED_BY_USER = IncidentImportRelatedObject("last_modified_by_user")
IncidentImportRelatedObject.CREATED_BY_USER = IncidentImportRelatedObject("created_by_user")
IncidentImportRelatedObject.COMMANDER_USER = IncidentImportRelatedObject("commander_user")
IncidentImportRelatedObject.DECLARED_BY_USER = IncidentImportRelatedObject("declared_by_user")
IncidentImportRelatedObject.INCIDENT_TYPE = IncidentImportRelatedObject("incident_type")
