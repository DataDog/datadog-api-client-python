# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class LogsByRetentionMonthlyUsage(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_retention_sum_usage import LogsRetentionSumUsage

        return {
            "date": (datetime,),
            "usage": ([LogsRetentionSumUsage],),
        }

    attribute_map = {
        "date": "date",
        "usage": "usage",
    }

    def __init__(self, *args, **kwargs):
        """
        Object containing a summary of indexed logs usage by retention period for a single month.

        :param date: The month for the usage.
        :type date: datetime, optional

        :param usage: Indexed logs usage for each active retention for the month.
        :type usage: [LogsRetentionSumUsage], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsByRetentionMonthlyUsage, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
