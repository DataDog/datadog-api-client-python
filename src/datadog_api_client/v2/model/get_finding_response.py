# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.detailed_finding import DetailedFinding
    from datadog_api_client.v2.model.finding_evaluation import FindingEvaluation
    from datadog_api_client.v2.model.finding_mute import FindingMute
    from datadog_api_client.v2.model.finding_rule import FindingRule
    from datadog_api_client.v2.model.finding_status import FindingStatus


@dataclass
class GetFindingResponseJSON:
    id: str
    evaluation: Union[FindingEvaluation, UnsetType] = unset
    evaluation_changed_at: Union[int, UnsetType] = unset
    message: Union[str, UnsetType] = unset
    mute: Union[FindingMute, UnsetType] = unset
    resource: Union[str, UnsetType] = unset
    resource_configuration: Union[dict, UnsetType] = unset
    resource_discovery_date: Union[int, UnsetType] = unset
    resource_type: Union[str, UnsetType] = unset
    rule: Union[FindingRule, UnsetType] = unset
    status: Union[FindingStatus, UnsetType] = unset
    tags: Union[List[str], UnsetType] = unset


class GetFindingResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.detailed_finding import DetailedFinding

        return {
            "data": (DetailedFinding,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = GetFindingResponseJSON

    def __init__(self_, data: DetailedFinding, **kwargs):
        """
        The expected response schema when getting a finding.

        :param data: A single finding with with message and resource configuration.
        :type data: DetailedFinding
        """
        super().__init__(kwargs)

        self_.data = data
