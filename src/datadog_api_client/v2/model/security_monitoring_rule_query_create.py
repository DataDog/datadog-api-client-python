# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringRuleQueryCreate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_query_aggregation import (
            SecurityMonitoringRuleQueryAggregation,
        )

        return {
            "aggregation": (SecurityMonitoringRuleQueryAggregation,),
            "distinct_fields": ([str],),
            "group_by_fields": ([str],),
            "metric": (str,),
            "metrics": ([str],),
            "name": (str,),
            "query": (str,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "distinct_fields": "distinctFields",
        "group_by_fields": "groupByFields",
        "metric": "metric",
        "metrics": "metrics",
        "name": "name",
        "query": "query",
    }

    def __init__(self, query, *args, **kwargs):
        """
        Query for matching rule.

        :param aggregation: The aggregation type.
        :type aggregation: SecurityMonitoringRuleQueryAggregation, optional

        :param distinct_fields: Field for which the cardinality is measured. Sent as an array.
        :type distinct_fields: [str], optional

        :param group_by_fields: Fields to group by.
        :type group_by_fields: [str], optional

        :param metric: The target field to aggregate over when using the sum or max
            aggregations.
        :type metric: str, optional

        :param metrics: Group of target fields to aggregate over when using the new value aggregations.
        :type metrics: [str], optional

        :param name: Name of the query.
        :type name: str, optional

        :param query: Query to run on logs.
        :type query: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.query = query

    @classmethod
    def _from_openapi_data(cls, query, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityMonitoringRuleQueryCreate, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.query = query
        return self
