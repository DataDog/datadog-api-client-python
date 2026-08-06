# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.governance_insight_audit_query import GovernanceInsightAuditQuery
    from datadog_api_client.v2.model.governance_insight_event_query import GovernanceInsightEventQuery
    from datadog_api_client.v2.model.governance_insight_metric_query import GovernanceInsightMetricQuery
    from datadog_api_client.v2.model.governance_insight_percentage_query import GovernanceInsightPercentageQuery
    from datadog_api_client.v2.model.governance_insight_query_config import GovernanceInsightQueryConfig
    from datadog_api_client.v2.model.governance_insight_usage_query import GovernanceInsightUsageQuery


class GovernanceInsightAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_insight_audit_query import GovernanceInsightAuditQuery
        from datadog_api_client.v2.model.governance_insight_event_query import GovernanceInsightEventQuery
        from datadog_api_client.v2.model.governance_insight_metric_query import GovernanceInsightMetricQuery
        from datadog_api_client.v2.model.governance_insight_percentage_query import GovernanceInsightPercentageQuery
        from datadog_api_client.v2.model.governance_insight_query_config import GovernanceInsightQueryConfig
        from datadog_api_client.v2.model.governance_insight_usage_query import GovernanceInsightUsageQuery

        return {
            "audit_query": (GovernanceInsightAuditQuery,),
            "description": (str,),
            "display_name": (str,),
            "event_query": (GovernanceInsightEventQuery,),
            "metric_query": (GovernanceInsightMetricQuery,),
            "percentage_query": (GovernanceInsightPercentageQuery,),
            "product": (str,),
            "query_config": (GovernanceInsightQueryConfig,),
            "sub_product": (str,),
            "time_range": (str,),
            "unit_name": (str,),
            "usage_query": (GovernanceInsightUsageQuery,),
        }

    attribute_map = {
        "audit_query": "audit_query",
        "description": "description",
        "display_name": "display_name",
        "event_query": "event_query",
        "metric_query": "metric_query",
        "percentage_query": "percentage_query",
        "product": "product",
        "query_config": "query_config",
        "sub_product": "sub_product",
        "time_range": "time_range",
        "unit_name": "unit_name",
        "usage_query": "usage_query",
    }

    def __init__(
        self_,
        description: str,
        display_name: str,
        product: str,
        sub_product: str,
        time_range: str,
        unit_name: str,
        audit_query: Union[GovernanceInsightAuditQuery, UnsetType] = unset,
        event_query: Union[GovernanceInsightEventQuery, UnsetType] = unset,
        metric_query: Union[GovernanceInsightMetricQuery, UnsetType] = unset,
        percentage_query: Union[GovernanceInsightPercentageQuery, UnsetType] = unset,
        query_config: Union[GovernanceInsightQueryConfig, UnsetType] = unset,
        usage_query: Union[GovernanceInsightUsageQuery, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a governance insight. Exactly one of ``metric_query`` , ``event_query`` ,
        ``usage_query`` , ``audit_query`` , or ``percentage_query`` is populated, depending on the data
        source the insight is computed from; the rest are ``null``.

        :param audit_query: An audit log query used to compute an insight value.
        :type audit_query: GovernanceInsightAuditQuery, optional

        :param description: A human-readable description of what the insight measures.
        :type description: str

        :param display_name: Human-readable name of the insight.
        :type display_name: str

        :param event_query: An event query used to compute an insight value.
        :type event_query: GovernanceInsightEventQuery, optional

        :param metric_query: A metric query used to compute an insight value.
        :type metric_query: GovernanceInsightMetricQuery, optional

        :param percentage_query: A percentage query that computes an insight value as a ratio of two metric queries.
        :type percentage_query: GovernanceInsightPercentageQuery, optional

        :param product: The product the insight belongs to.
        :type product: str

        :param query_config: Query execution context for running insight queries directly.
        :type query_config: GovernanceInsightQueryConfig, optional

        :param sub_product: The sub-product the insight belongs to, if any.
        :type sub_product: str

        :param time_range: The time range the insight value is computed over, if applicable.
        :type time_range: str

        :param unit_name: The unit that the insight's value is measured in.
        :type unit_name: str

        :param usage_query: A usage query used to compute an insight value.
        :type usage_query: GovernanceInsightUsageQuery, optional
        """
        if audit_query is not unset:
            kwargs["audit_query"] = audit_query
        if event_query is not unset:
            kwargs["event_query"] = event_query
        if metric_query is not unset:
            kwargs["metric_query"] = metric_query
        if percentage_query is not unset:
            kwargs["percentage_query"] = percentage_query
        if query_config is not unset:
            kwargs["query_config"] = query_config
        if usage_query is not unset:
            kwargs["usage_query"] = usage_query
        super().__init__(kwargs)

        self_.description = description
        self_.display_name = display_name
        self_.product = product
        self_.sub_product = sub_product
        self_.time_range = time_range
        self_.unit_name = unit_name
