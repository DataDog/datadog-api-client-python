# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.jira_issue_finding_id import JiraIssueFindingId
    from datadog_api_client.v2.model.finding_status import FindingStatus


class JiraIssueFinding(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.jira_issue_finding_id import JiraIssueFindingId
        from datadog_api_client.v2.model.finding_status import FindingStatus

        return {
            "description": (str,),
            "ids": ([JiraIssueFindingId],),
            "impacted": (int,),
            "references": (str,),
            "remediation": (str,),
            "severity": (FindingStatus,),
            "title": (str,),
            "type": (str,),
        }

    attribute_map = {
        "description": "description",
        "ids": "ids",
        "impacted": "impacted",
        "references": "references",
        "remediation": "remediation",
        "severity": "severity",
        "title": "title",
        "type": "type",
    }

    def __init__(
        self_,
        description: str,
        ids: List[JiraIssueFindingId],
        references: str,
        remediation: str,
        severity: FindingStatus,
        title: str,
        type: str,
        impacted: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param description: Description of the finding.
        :type description: str

        :param ids:
        :type ids: [JiraIssueFindingId]

        :param impacted: Number of impacted resources.
        :type impacted: int, optional

        :param references: References for the finding.
        :type references: str

        :param remediation: Remediation instructions for the finding.
        :type remediation: str

        :param severity: The status of the finding.
        :type severity: FindingStatus

        :param title: Title of the finding.
        :type title: str

        :param type: Type of the finding.
        :type type: str
        """
        if impacted is not unset:
            kwargs["impacted"] = impacted
        super().__init__(kwargs)

        self_.description = description
        self_.ids = ids
        self_.references = references
        self_.remediation = remediation
        self_.severity = severity
        self_.title = title
        self_.type = type
