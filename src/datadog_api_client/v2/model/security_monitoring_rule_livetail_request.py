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
    from datadog_api_client.v2.model.security_monitoring_rule_detection_method import (
        SecurityMonitoringRuleDetectionMethod,
    )
    from datadog_api_client.v2.model.security_monitoring_filter import SecurityMonitoringFilter
    from datadog_api_client.v2.model.security_monitoring_rule_type_read import SecurityMonitoringRuleTypeRead


class SecurityMonitoringRuleLivetailRequest(ModelNormal):
    validations = {
        "query_index": {
            "inclusive_maximum": 9,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_detection_method import (
            SecurityMonitoringRuleDetectionMethod,
        )
        from datadog_api_client.v2.model.security_monitoring_filter import SecurityMonitoringFilter
        from datadog_api_client.v2.model.security_monitoring_rule_type_read import SecurityMonitoringRuleTypeRead

        return {
            "data_source": (str,),
            "detection_method": (SecurityMonitoringRuleDetectionMethod,),
            "distinct_fields": ([str],),
            "filters": ([SecurityMonitoringFilter],),
            "group_by_fields": ([str],),
            "query": (str,),
            "query_index": (int,),
            "type": (SecurityMonitoringRuleTypeRead,),
        }

    attribute_map = {
        "data_source": "dataSource",
        "detection_method": "detectionMethod",
        "distinct_fields": "distinctFields",
        "filters": "filters",
        "group_by_fields": "groupByFields",
        "query": "query",
        "query_index": "queryIndex",
        "type": "type",
    }

    def __init__(
        self_,
        data_source: str,
        detection_method: SecurityMonitoringRuleDetectionMethod,
        query: str,
        query_index: int,
        type: SecurityMonitoringRuleTypeRead,
        distinct_fields: Union[List[str], UnsetType] = unset,
        filters: Union[List[SecurityMonitoringFilter], UnsetType] = unset,
        group_by_fields: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Request to preview a rule query with applied filters.

        :param data_source: Data source for the query.
        :type data_source: str

        :param detection_method: The detection method.
        :type detection_method: SecurityMonitoringRuleDetectionMethod

        :param distinct_fields: Fields to apply distinct on.
        :type distinct_fields: [str], optional

        :param filters: Additional security filters to apply.
        :type filters: [SecurityMonitoringFilter], optional

        :param group_by_fields: Fields to group by.
        :type group_by_fields: [str], optional

        :param query: The query to preview.
        :type query: str

        :param query_index: Index of the query in the rule.
        :type query_index: int

        :param type: The rule type.
        :type type: SecurityMonitoringRuleTypeRead
        """
        if distinct_fields is not unset:
            kwargs["distinct_fields"] = distinct_fields
        if filters is not unset:
            kwargs["filters"] = filters
        if group_by_fields is not unset:
            kwargs["group_by_fields"] = group_by_fields
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.detection_method = detection_method
        self_.query = query
        self_.query_index = query_index
        self_.type = type
