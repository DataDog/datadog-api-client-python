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


class DetailedFindingAttributes(ModelNormal):
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

        return {
            "evaluation": (FindingEvaluation,),
            "evaluation_changed_at": (int,),
            "message": (str,),
            "mute": (FindingMute,),
            "resource": (str,),
            "resource_configuration": (dict,),
            "resource_discovery_date": (int,),
            "resource_type": (str,),
            "rule": (FindingRule,),
            "status": (FindingStatus,),
            "tags": ([str],),
        }

    attribute_map = {
        "evaluation": "evaluation",
        "evaluation_changed_at": "evaluation_changed_at",
        "message": "message",
        "mute": "mute",
        "resource": "resource",
        "resource_configuration": "resource_configuration",
        "resource_discovery_date": "resource_discovery_date",
        "resource_type": "resource_type",
        "rule": "rule",
        "status": "status",
        "tags": "tags",
    }

    def __init__(
        self_,
        evaluation: Union[FindingEvaluation, UnsetType] = unset,
        evaluation_changed_at: Union[int, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        mute: Union[FindingMute, UnsetType] = unset,
        resource: Union[str, UnsetType] = unset,
        resource_configuration: Union[dict, UnsetType] = unset,
        resource_discovery_date: Union[int, UnsetType] = unset,
        resource_type: Union[str, UnsetType] = unset,
        rule: Union[FindingRule, UnsetType] = unset,
        status: Union[FindingStatus, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The JSON:API attributes of the detailed finding.

        :param evaluation: The evaluation of the finding.
        :type evaluation: FindingEvaluation, optional

        :param evaluation_changed_at: The date on which the evaluation for this finding changed (Unix ms).
        :type evaluation_changed_at: int, optional

        :param message: The remediation message for this finding.
        :type message: str, optional

        :param mute: Information about the mute status of this finding.
        :type mute: FindingMute, optional

        :param resource: The resource name of this finding.
        :type resource: str, optional

        :param resource_configuration: The resource configuration for this finding.
        :type resource_configuration: dict, optional

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
        """
        if evaluation is not unset:
            kwargs["evaluation"] = evaluation
        if evaluation_changed_at is not unset:
            kwargs["evaluation_changed_at"] = evaluation_changed_at
        if message is not unset:
            kwargs["message"] = message
        if mute is not unset:
            kwargs["mute"] = mute
        if resource is not unset:
            kwargs["resource"] = resource
        if resource_configuration is not unset:
            kwargs["resource_configuration"] = resource_configuration
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
        super().__init__(kwargs)
