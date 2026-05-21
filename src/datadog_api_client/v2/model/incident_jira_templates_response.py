# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_jira_template_data_response import IncidentJiraTemplateDataResponse


class IncidentJiraTemplatesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_jira_template_data_response import IncidentJiraTemplateDataResponse

        return {
            "data": ([IncidentJiraTemplateDataResponse],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[IncidentJiraTemplateDataResponse], **kwargs):
        """
        Response with a list of incident Jira templates.

        :param data: List of incident Jira templates.
        :type data: [IncidentJiraTemplateDataResponse]
        """
        super().__init__(kwargs)

        self_.data = data
