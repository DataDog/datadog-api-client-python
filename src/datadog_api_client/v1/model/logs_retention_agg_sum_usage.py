# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsRetentionAggSumUsage(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "logs_indexed_logs_usage_agg_sum": (int,),
            "logs_live_indexed_logs_usage_agg_sum": (int,),
            "logs_rehydrated_indexed_logs_usage_agg_sum": (int,),
            "retention": (str,),
        }

    attribute_map = {
        "logs_indexed_logs_usage_agg_sum": "logs_indexed_logs_usage_agg_sum",
        "logs_live_indexed_logs_usage_agg_sum": "logs_live_indexed_logs_usage_agg_sum",
        "logs_rehydrated_indexed_logs_usage_agg_sum": "logs_rehydrated_indexed_logs_usage_agg_sum",
        "retention": "retention",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Object containing indexed logs usage aggregated across organizations and months for a retention period.

        :param logs_indexed_logs_usage_agg_sum: Total indexed logs for this retention period.
        :type logs_indexed_logs_usage_agg_sum: int, optional

        :param logs_live_indexed_logs_usage_agg_sum: Live indexed logs for this retention period.
        :type logs_live_indexed_logs_usage_agg_sum: int, optional

        :param logs_rehydrated_indexed_logs_usage_agg_sum: Rehydrated indexed logs for this retention period.
        :type logs_rehydrated_indexed_logs_usage_agg_sum: int, optional

        :param retention: The retention period in days or "custom" for all custom retention periods.
        :type retention: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsRetentionAggSumUsage, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
