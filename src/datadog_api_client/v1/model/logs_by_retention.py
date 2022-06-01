# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsByRetention(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_by_retention_orgs import LogsByRetentionOrgs
        from datadog_api_client.v1.model.logs_retention_agg_sum_usage import LogsRetentionAggSumUsage
        from datadog_api_client.v1.model.logs_by_retention_monthly_usage import LogsByRetentionMonthlyUsage

        return {
            "orgs": (LogsByRetentionOrgs,),
            "usage": ([LogsRetentionAggSumUsage],),
            "usage_by_month": (LogsByRetentionMonthlyUsage,),
        }

    attribute_map = {
        "orgs": "orgs",
        "usage": "usage",
        "usage_by_month": "usage_by_month",
    }

    def __init__(self, *args, **kwargs):
        """
        Object containing logs usage data broken down by retention period.

        :param orgs: Indexed logs usage summary for each organization for each retention period with usage.
        :type orgs: LogsByRetentionOrgs, optional

        :param usage: Aggregated index logs usage for each retention period with usage.
        :type usage: [LogsRetentionAggSumUsage], optional

        :param usage_by_month: Object containing a summary of indexed logs usage by retention period for a single month.
        :type usage_by_month: LogsByRetentionMonthlyUsage, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsByRetention, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
