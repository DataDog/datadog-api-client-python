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
    from datadog_api_client.v2.model.findings import Findings
    from datadog_api_client.v2.model.case_management_project import CaseManagementProject


class CreateJiraIssueRequestDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.findings import Findings
        from datadog_api_client.v2.model.case_management_project import CaseManagementProject

        return {
            "findings": (Findings,),
            "project": (CaseManagementProject,),
        }

    attribute_map = {
        "findings": "findings",
        "project": "project",
    }

    def __init__(self_, findings: Findings, project: CaseManagementProject, **kwargs):
        """
        Relationships of the Jira issue to create.

        :param findings: A list of security findings.
        :type findings: Findings

        :param project: Case management project.
        :type project: CaseManagementProject
        """
        super().__init__(kwargs)

        self_.findings = findings
        self_.project = project
