# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentJiraTemplateType(ModelSimple):
    """
    Incident Jira template resource type.

    :param value: If omitted defaults to "incidents_jira_templates". Must be one of ["incidents_jira_templates"].
    :type value: str
    """

    allowed_values = {
        "incidents_jira_templates",
    }
    INCIDENTS_JIRA_TEMPLATES: ClassVar["IncidentJiraTemplateType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentJiraTemplateType.INCIDENTS_JIRA_TEMPLATES = IncidentJiraTemplateType("incidents_jira_templates")
