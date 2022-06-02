# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsIndexUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_exclusion import LogsExclusion
        from datadog_api_client.v1.model.logs_filter import LogsFilter

        return {
            "daily_limit": (int,),
            "disable_daily_limit": (bool,),
            "exclusion_filters": ([LogsExclusion],),
            "filter": (LogsFilter,),
            "num_retention_days": (int,),
        }

    attribute_map = {
        "daily_limit": "daily_limit",
        "disable_daily_limit": "disable_daily_limit",
        "exclusion_filters": "exclusion_filters",
        "filter": "filter",
        "num_retention_days": "num_retention_days",
    }

    def __init__(self, filter, *args, **kwargs):
        """
        Object for updating a Datadog Log index.

        :param daily_limit: The number of log events you can send in this index per day before you are rate-limited.
        :type daily_limit: int, optional

        :param disable_daily_limit: If true, sets the ``daily_limit`` value to null and the index is not limited on a daily basis (any
            specified ``daily_limit`` value in the request is ignored). If false or omitted, the index's current
            ``daily_limit`` is maintained.
        :type disable_daily_limit: bool, optional

        :param exclusion_filters: An array of exclusion objects. The logs are tested against the query of each filter,
            following the order of the array. Only the first matching active exclusion matters,
            others (if any) are ignored.
        :type exclusion_filters: [LogsExclusion], optional

        :param filter: Filter for logs.
        :type filter: LogsFilter

        :param num_retention_days: The number of days before logs are deleted from this index. Available values depend on
            retention plans specified in your organization's contract/subscriptions.

            **Note:** Changing the retention for an index adjusts the length of retention for all logs
            already in this index. It may also affect billing.
        :type num_retention_days: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.filter = filter

    @classmethod
    def _from_openapi_data(cls, filter, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsIndexUpdateRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.filter = filter
        return self
