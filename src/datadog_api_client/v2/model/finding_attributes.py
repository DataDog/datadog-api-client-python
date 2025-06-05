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
    from datadog_api_client.v2.model.finding_evaluation import FindingEvaluation
    from datadog_api_client.v2.model.finding_mute import FindingMute
    from datadog_api_client.v2.model.finding_rule import FindingRule
    from datadog_api_client.v2.model.finding_status import FindingStatus
    from datadog_api_client.v2.model.finding_vulnerability_type import FindingVulnerabilityType


class FindingAttributes(ModelNormal):
    validations = {
        "evaluation_changed_at": {
            "inclusive_minimum": 1,
        },
        "resource_discovery_date": {
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.finding_evaluation import FindingEvaluation
        from datadog_api_client.v2.model.finding_mute import FindingMute
        from datadog_api_client.v2.model.finding_rule import FindingRule
        from datadog_api_client.v2.model.finding_status import FindingStatus
        from datadog_api_client.v2.model.finding_vulnerability_type import FindingVulnerabilityType

        return {
            "datadog_link": (str,),
            "description": (str,),
            "evaluation": (FindingEvaluation,),
            "evaluation_changed_at": (int,),
            "external_id": (str,),
            "mute": (FindingMute,),
            "resource": (str,),
            "resource_discovery_date": (int,),
            "resource_type": (str,),
            "rule": (FindingRule,),
            "status": (FindingStatus,),
            "tags": ([str],),
            "vulnerability_type": (FindingVulnerabilityType,),
        }

    attribute_map = {
        "datadog_link": "datadog_link",
        "description": "description",
        "evaluation": "evaluation",
        "evaluation_changed_at": "evaluation_changed_at",
        "external_id": "external_id",
        "mute": "mute",
        "resource": "resource",
        "resource_discovery_date": "resource_discovery_date",
        "resource_type": "resource_type",
        "rule": "rule",
        "status": "status",
        "tags": "tags",
        "vulnerability_type": "vulnerability_type",
    }

    def __init__(
        self_,
        datadog_link: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        evaluation: Union[FindingEvaluation, UnsetType] = unset,
        evaluation_changed_at: Union[int, UnsetType] = unset,
        external_id: Union[str, UnsetType] = unset,
        mute: Union[FindingMute, UnsetType] = unset,
        resource: Union[str, UnsetType] = unset,
        resource_discovery_date: Union[int, UnsetType] = unset,
        resource_type: Union[str, UnsetType] = unset,
        rule: Union[FindingRule, UnsetType] = unset,
        status: Union[FindingStatus, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        vulnerability_type: Union[FindingVulnerabilityType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The JSON:API attributes of the finding.

        :param datadog_link: The Datadog relative link for this finding.
        :type datadog_link: str, optional

        :param description: The description and remediation steps for this finding.
        :type description: str, optional

        :param evaluation: The evaluation of the finding.
        :type evaluation: FindingEvaluation, optional

        :param evaluation_changed_at: The date on which the evaluation for this finding changed (Unix ms).
        :type evaluation_changed_at: int, optional

        :param external_id: The cloud-based ID for the resource related to the finding.
        :type external_id: str, optional

        :param mute: Information about the mute status of this finding.
        :type mute: FindingMute, optional

        :param resource: The resource name of this finding.
        :type resource: str, optional

        :param resource_discovery_date: The date on which the resource was discovered (Unix ms).
        :type resource_discovery_date: int, optional

        :param resource_type: The resource type of this finding.
        :type resource_type: str, optional

        :param rule: The rule that triggered this finding.
        :type rule: FindingRule, optional

        :param status: The status of the finding.
        :type status: FindingStatus, optional

        :param tags: The tags associated with this finding.
        :type tags: [str], optional

        :param vulnerability_type: The vulnerability type of the finding.
        :type vulnerability_type: FindingVulnerabilityType, optional
        """
        if datadog_link is not unset:
            kwargs["datadog_link"] = datadog_link
        if description is not unset:
            kwargs["description"] = description
        if evaluation is not unset:
            kwargs["evaluation"] = evaluation
        if evaluation_changed_at is not unset:
            kwargs["evaluation_changed_at"] = evaluation_changed_at
        if external_id is not unset:
            kwargs["external_id"] = external_id
        if mute is not unset:
            kwargs["mute"] = mute
        if resource is not unset:
            kwargs["resource"] = resource
        if resource_discovery_date is not unset:
            kwargs["resource_discovery_date"] = resource_discovery_date
        if resource_type is not unset:
            kwargs["resource_type"] = resource_type
        if rule is not unset:
            kwargs["rule"] = rule
        if status is not unset:
            kwargs["status"] = status
        if tags is not unset:
            kwargs["tags"] = tags
        if vulnerability_type is not unset:
            kwargs["vulnerability_type"] = vulnerability_type
        super().__init__(kwargs)
