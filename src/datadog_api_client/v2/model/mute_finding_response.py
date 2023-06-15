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


from datadog_api_client.v2.model.finding_evaluation import FindingEvaluation
from datadog_api_client.v2.model.mute_finding_response_properties import MuteFindingResponseProperties
from datadog_api_client.v2.model.finding_rule import FindingRule
from datadog_api_client.v2.model.finding_status import FindingStatus
from datadog_api_client.v2.model.finding_evaluation import FindingEvaluation
from datadog_api_client.v2.model.mute_finding_response_properties import MuteFindingResponseProperties
from datadog_api_client.v2.model.finding_rule import FindingRule
from datadog_api_client.v2.model.finding_status import FindingStatus

if TYPE_CHECKING:
    from datadog_api_client.v2.model.mute_finding_response_data import MuteFindingResponseData


@dataclass
class MuteFindingResponseJSON:
    id: str
    evaluation: Union[FindingEvaluation, UnsetType] = unset
    evaluation_changed_at: Union[int, UnsetType] = unset
    mute: Union[MuteFindingResponseProperties, UnsetType] = unset
    resource: Union[str, UnsetType] = unset
    resource_discovery_date: Union[int, UnsetType] = unset
    resource_type: Union[str, UnsetType] = unset
    rule: Union[FindingRule, UnsetType] = unset
    status: Union[FindingStatus, UnsetType] = unset
    tags: Union[List[str], UnsetType] = unset


class MuteFindingResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.mute_finding_response_data import MuteFindingResponseData

        return {
            "data": (MuteFindingResponseData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = MuteFindingResponseJSON

    def __init__(self_, data: MuteFindingResponseData, **kwargs):
        """
        The expected response schema.

        :param data: Data object containing the updated finding.
        :type data: MuteFindingResponseData
        """
        super().__init__(kwargs)

        self_.data = data
