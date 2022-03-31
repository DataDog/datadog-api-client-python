# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class UsageLogsHour(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "billable_ingested_bytes": (int,),
            "hour": (datetime,),
            "indexed_events_count": (int,),
            "ingested_events_bytes": (int,),
            "logs_live_indexed_count": (int,),
            "logs_live_ingested_bytes": (int,),
            "logs_rehydrated_indexed_count": (int,),
            "logs_rehydrated_ingested_bytes": (int,),
            "org_name": (str,),
            "public_id": (str,),
        }

    attribute_map = {
        "billable_ingested_bytes": "billable_ingested_bytes",
        "hour": "hour",
        "indexed_events_count": "indexed_events_count",
        "ingested_events_bytes": "ingested_events_bytes",
        "logs_live_indexed_count": "logs_live_indexed_count",
        "logs_live_ingested_bytes": "logs_live_ingested_bytes",
        "logs_rehydrated_indexed_count": "logs_rehydrated_indexed_count",
        "logs_rehydrated_ingested_bytes": "logs_rehydrated_ingested_bytes",
        "org_name": "org_name",
        "public_id": "public_id",
    }

    def __init__(self, *args, **kwargs):
        """
        Hour usage for logs.

        :param billable_ingested_bytes: Contains the number of billable log bytes ingested.
        :type billable_ingested_bytes: int, optional

        :param hour: The hour for the usage.
        :type hour: datetime, optional

        :param indexed_events_count: Contains the number of log events indexed.
        :type indexed_events_count: int, optional

        :param ingested_events_bytes: Contains the number of log bytes ingested.
        :type ingested_events_bytes: int, optional

        :param logs_live_indexed_count: Contains the number of live log events indexed (data available as of December 1, 2020).
        :type logs_live_indexed_count: int, optional

        :param logs_live_ingested_bytes: Contains the number of live log bytes ingested (data available as of December 1, 2020).
        :type logs_live_ingested_bytes: int, optional

        :param logs_rehydrated_indexed_count: Contains the number of rehydrated log events indexed (data available as of December 1, 2020).
        :type logs_rehydrated_indexed_count: int, optional

        :param logs_rehydrated_ingested_bytes: Contains the number of rehydrated log bytes ingested (data available as of December 1, 2020).
        :type logs_rehydrated_ingested_bytes: int, optional

        :param org_name: The organization name.
        :type org_name: str, optional

        :param public_id: The organization public ID.
        :type public_id: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageLogsHour, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
