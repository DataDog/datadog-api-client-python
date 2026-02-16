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
    from datadog_api_client.v2.model.jira_issue_finding import JiraIssueFinding


class JiraIssueDataMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.jira_issue_finding import JiraIssueFinding

        return {
            "findings": ([JiraIssueFinding],),
            "vulnerabilities": ([JiraIssueFinding],),
        }

    attribute_map = {
        "findings": "findings",
        "vulnerabilities": "vulnerabilities",
    }

    def __init__(
        self_,
        findings: Union[List[JiraIssueFinding], UnsetType] = unset,
        vulnerabilities: Union[List[JiraIssueFinding], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param findings:
        :type findings: [JiraIssueFinding], optional

        :param vulnerabilities:
        :type vulnerabilities: [JiraIssueFinding], optional
        """
        if findings is not unset:
            kwargs["findings"] = findings
        if vulnerabilities is not unset:
            kwargs["vulnerabilities"] = vulnerabilities
        super().__init__(kwargs)
