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
    from datadog_api_client.v2.model.case_data_type import CaseDataType


class CreateJiraIssueRequestDataRelationshipsCaseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_data_type import CaseDataType

        return {
            "id": (str,),
            "type": (CaseDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: CaseDataType, **kwargs):
        """
        Case linked to the Jira issue.

        :param id:
        :type id: str

        :param type: Cases resource type.
        :type type: CaseDataType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
