# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.governance_insight_audit_query import GovernanceInsightAuditQuery
    from datadog_api_client.v2.model.governance_best_practice_definition import GovernanceBestPracticeDefinition
    from datadog_api_client.v2.model.governance_insight_event_query import GovernanceInsightEventQuery
    from datadog_api_client.v2.model.governance_insight_metric_query import GovernanceInsightMetricQuery
    from datadog_api_client.v2.model.governance_insight_percentage_query import GovernanceInsightPercentageQuery
    from datadog_api_client.v2.model.governance_insight_query_config import GovernanceInsightQueryConfig
    from datadog_api_client.v2.model.governance_insight_usage_query import GovernanceInsightUsageQuery


class GovernanceInsightAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_insight_audit_query import GovernanceInsightAuditQuery
        from datadog_api_client.v2.model.governance_best_practice_definition import GovernanceBestPracticeDefinition
        from datadog_api_client.v2.model.governance_insight_event_query import GovernanceInsightEventQuery
        from datadog_api_client.v2.model.governance_insight_metric_query import GovernanceInsightMetricQuery
        from datadog_api_client.v2.model.governance_insight_percentage_query import GovernanceInsightPercentageQuery
        from datadog_api_client.v2.model.governance_insight_query_config import GovernanceInsightQueryConfig
        from datadog_api_client.v2.model.governance_insight_usage_query import GovernanceInsightUsageQuery

        return {
            "audit_query": (GovernanceInsightAuditQuery,),
            "best_practice": (GovernanceBestPracticeDefinition,),
            "deep_link": (str,),
            "description": (str,),
            "display_name": (str,),
            "event_query": (GovernanceInsightEventQuery,),
            "metric_query": (GovernanceInsightMetricQuery,),
            "old_value": (float, none_type),
            "percentage_query": (GovernanceInsightPercentageQuery,),
            "product": (str,),
            "query_config": (GovernanceInsightQueryConfig,),
            "sort_order": (int,),
            "state": (str,),
            "sub_product": (str,),
            "time_range": (str,),
            "unit_name": (str,),
            "usage_query": (GovernanceInsightUsageQuery,),
            "value": (float, none_type),
        }

    attribute_map = {
        "audit_query": "audit_query",
        "best_practice": "best_practice",
        "deep_link": "deep_link",
        "description": "description",
        "display_name": "display_name",
        "event_query": "event_query",
        "metric_query": "metric_query",
        "old_value": "old_value",
        "percentage_query": "percentage_query",
        "product": "product",
        "query_config": "query_config",
        "sort_order": "sort_order",
        "state": "state",
        "sub_product": "sub_product",
        "time_range": "time_range",
        "unit_name": "unit_name",
        "usage_query": "usage_query",
        "value": "value",
    }

    def __init__(
        self_,
        audit_query: GovernanceInsightAuditQuery,
        best_practice: GovernanceBestPracticeDefinition,
        deep_link: str,
        description: str,
        display_name: str,
        event_query: GovernanceInsightEventQuery,
        metric_query: GovernanceInsightMetricQuery,
        old_value: Union[float, none_type],
        percentage_query: GovernanceInsightPercentageQuery,
        product: str,
        state: str,
        sub_product: str,
        time_range: str,
        unit_name: str,
        usage_query: GovernanceInsightUsageQuery,
        value: Union[float, none_type],
        query_config: Union[GovernanceInsightQueryConfig, UnsetType] = unset,
        sort_order: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a governance insight.

        :param audit_query: An audit log query used to compute an insight value.
        :type audit_query: GovernanceInsightAuditQuery

        :param best_practice: The best practice associated with an insight. Populated with the first active best practice
            matched to the insight; ``null`` when no best practice is attached.
        :type best_practice: GovernanceBestPracticeDefinition

        :param deep_link: A relative link to the product surface where the insight can be acted upon.
        :type deep_link: str

        :param description: A human-readable description of what the insight measures.
        :type description: str

        :param display_name: Human-readable name of the insight.
        :type display_name: str

        :param event_query: An event query used to compute an insight value.
        :type event_query: GovernanceInsightEventQuery

        :param metric_query: A metric query used to compute an insight value.
        :type metric_query: GovernanceInsightMetricQuery

        :param old_value: The value of the insight over the previous comparison window. ``null`` when values were
            not requested or could not be computed.
        :type old_value: float, none_type

        :param percentage_query: A percentage query that computes an insight value as a ratio of two metric queries.
        :type percentage_query: GovernanceInsightPercentageQuery

        :param product: The product the insight belongs to.
        :type product: str

        :param query_config: Query execution context that allows the frontend to execute insight queries directly.
        :type query_config: GovernanceInsightQueryConfig, optional

        :param sort_order: The relative order in which the insight should be displayed.
        :type sort_order: int, optional

        :param state: The state of the insight. A ``critical`` insight receives extra UI treatment to draw
            attention to it.
        :type state: str

        :param sub_product: The sub-product the insight belongs to, if any.
        :type sub_product: str

        :param time_range: The time range the insight value is computed over, if applicable.
        :type time_range: str

        :param unit_name: The unit that the insight's value is measured in.
        :type unit_name: str

        :param usage_query: A usage query used to compute an insight value.
        :type usage_query: GovernanceInsightUsageQuery

        :param value: The current value of the insight. ``null`` when values were not requested or could not be computed.
        :type value: float, none_type
        """
        if query_config is not unset:
            kwargs["query_config"] = query_config
        if sort_order is not unset:
            kwargs["sort_order"] = sort_order
        super().__init__(kwargs)

        self_.audit_query = audit_query
        self_.best_practice = best_practice
        self_.deep_link = deep_link
        self_.description = description
        self_.display_name = display_name
        self_.event_query = event_query
        self_.metric_query = metric_query
        self_.old_value = old_value
        self_.percentage_query = percentage_query
        self_.product = product
        self_.state = state
        self_.sub_product = sub_product
        self_.time_range = time_range
        self_.unit_name = unit_name
        self_.usage_query = usage_query
        self_.value = value
