# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class SecurityMonitoringRuleMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "entities": ([bool, date, datetime, dict, float, int, list, str, UUID, none_type], none_type),
            "sources": ([str], none_type),
        }

    attribute_map = {
        "entities": "entities",
        "sources": "sources",
    }

    def __init__(
        self_,
        entities: Union[List[Any], none_type, UnsetType] = unset,
        sources: Union[List[str], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata associated with the rule.

        :param entities: Entities associated with the rule, or null when metadata is not requested.
        :type entities: [bool, date, datetime, dict, float, int, list, str, UUID, none_type], none_type, optional

        :param sources: Sources associated with the rule, or null when metadata is not requested.
        :type sources: [str], none_type, optional
        """
        if entities is not unset:
            kwargs["entities"] = entities
        if sources is not unset:
            kwargs["sources"] = sources
        super().__init__(kwargs)
