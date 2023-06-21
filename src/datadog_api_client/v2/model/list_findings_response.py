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
    from datadog_api_client.v2.model.finding import Finding
    from datadog_api_client.v2.model.list_findings_meta import ListFindingsMeta
    from datadog_api_client.v2.model.finding_evaluation import FindingEvaluation
    from datadog_api_client.v2.model.finding_mute import FindingMute
    from datadog_api_client.v2.model.finding_rule import FindingRule
    from datadog_api_client.v2.model.finding_status import FindingStatus


@dataclass
class ListFindingsResponseJSON:
    id: str
    evaluation: Union[FindingEvaluation, UnsetType] = unset
    evaluation_changed_at: Union[int, UnsetType] = unset
    mute: Union[FindingMute, UnsetType] = unset
    resource: Union[str, UnsetType] = unset
    resource_discovery_date: Union[int, UnsetType] = unset
    resource_type: Union[str, UnsetType] = unset
    rule: Union[FindingRule, UnsetType] = unset
    status: Union[FindingStatus, UnsetType] = unset
    tags: Union[List[str], UnsetType] = unset


class ListFindingsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.finding import Finding
        from datadog_api_client.v2.model.list_findings_meta import ListFindingsMeta

        return {
            "data": ([Finding],),
            "meta": (ListFindingsMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }
    json_api_model = ListFindingsResponseJSON

    def __init__(self_, data: List[Finding], meta: ListFindingsMeta, **kwargs):
        """
        The expected response schema when listing findings.

        :param data: Array of findings.
        :type data: [Finding]

        :param meta: Metadata for pagination.
        :type meta: ListFindingsMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
