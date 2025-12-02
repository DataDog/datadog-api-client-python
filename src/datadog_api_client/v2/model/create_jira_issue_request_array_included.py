# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class CreateJiraIssueRequestArrayIncluded(ModelComposed):
    def __init__(self, **kwargs):
        """
        Attributes and relationships of the case linked to the Jira issue. Should contain all of the following: case, project, and security findings.

        :param attributes: Attributes of the case to create.
        :type attributes: CreateCaseRequestDataAttributes, optional

        :param id: The unique identifier of the case.
        :type id: str, optional

        :param relationships: Relationships of the case to create.
        :type relationships: CreateCaseRequestDataRelationships, optional

        :param type: Cases resource type.
        :type type: CaseDataType
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.create_case_request_data import CreateCaseRequestData
        from datadog_api_client.v2.model.case_management_project_data import CaseManagementProjectData
        from datadog_api_client.v2.model.finding_data import FindingData

        return {
            "oneOf": [
                CreateCaseRequestData,
                CaseManagementProjectData,
                FindingData,
            ],
        }
