# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsRetentionSumUsage(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "logs_indexed_logs_usage_sum": (int,),
            "logs_live_indexed_logs_usage_sum": (int,),
            "logs_rehydrated_indexed_logs_usage_sum": (int,),
            "retention": (str,),
        }

    attribute_map = {
        "logs_indexed_logs_usage_sum": "logs_indexed_logs_usage_sum",
        "logs_live_indexed_logs_usage_sum": "logs_live_indexed_logs_usage_sum",
        "logs_rehydrated_indexed_logs_usage_sum": "logs_rehydrated_indexed_logs_usage_sum",
        "retention": "retention",
    }

    def __init__(self_, *args, **kwargs):
        """
        Object containing indexed logs usage grouped by retention period and summed.

        :param logs_indexed_logs_usage_sum: Total indexed logs for this retention period.
        :type logs_indexed_logs_usage_sum: int, optional

        :param logs_live_indexed_logs_usage_sum: Live indexed logs for this retention period.
        :type logs_live_indexed_logs_usage_sum: int, optional

        :param logs_rehydrated_indexed_logs_usage_sum: Rehydrated indexed logs for this retention period.
        :type logs_rehydrated_indexed_logs_usage_sum: int, optional

        :param retention: The retention period in days or "custom" for all custom retention periods.
        :type retention: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
