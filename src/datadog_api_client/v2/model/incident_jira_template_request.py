# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_jira_template_data_request import IncidentJiraTemplateDataRequest


class IncidentJiraTemplateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_jira_template_data_request import IncidentJiraTemplateDataRequest

        return {
            "data": (IncidentJiraTemplateDataRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IncidentJiraTemplateDataRequest, **kwargs):
        """
        Create or update request for an incident Jira template.

        :param data: Incident Jira template data for a create or update request.
        :type data: IncidentJiraTemplateDataRequest
        """
        super().__init__(kwargs)

        self_.data = data
