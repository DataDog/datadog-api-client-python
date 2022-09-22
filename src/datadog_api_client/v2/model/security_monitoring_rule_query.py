# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringRuleQuery(ModelNormal):
    validations = {
        "correlated_query_index": {
            "inclusive_maximum": 9,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_query_aggregation import (
            SecurityMonitoringRuleQueryAggregation,
        )

        return {
            "aggregation": (SecurityMonitoringRuleQueryAggregation,),
            "correlated_by_fields": ([str],),
            "correlated_query_index": (int,),
            "distinct_fields": ([str],),
            "group_by_fields": ([str],),
            "metric": (str,),
            "metrics": ([str],),
            "name": (str,),
            "query": (str,),
            "rule_id": (str,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "correlated_by_fields": "correlatedByFields",
        "correlated_query_index": "correlatedQueryIndex",
        "distinct_fields": "distinctFields",
        "group_by_fields": "groupByFields",
        "metric": "metric",
        "metrics": "metrics",
        "name": "name",
        "query": "query",
        "rule_id": "ruleId",
    }

    def __init__(self_, *args, **kwargs):
        """
        Query for matching rule.

        :param aggregation: The aggregation type.
        :type aggregation: SecurityMonitoringRuleQueryAggregation, optional

        :param correlated_by_fields: Fields to group by for Signal Correlation rules.
        :type correlated_by_fields: [str], optional

        :param correlated_query_index: Index of the rule query used to retrieve the correlated field for Signal Correlation rules.
        :type correlated_query_index: int, optional

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
        :type query: str, optional

        :param rule_id: Rule ID to match on signals for Signal Correlation rules.
        :type rule_id: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
