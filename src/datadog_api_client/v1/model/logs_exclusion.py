# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsExclusion(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_exclusion_filter import LogsExclusionFilter

        return {
            "filter": (LogsExclusionFilter,),
            "is_enabled": (bool,),
            "name": (str,),
        }

    attribute_map = {
        "filter": "filter",
        "is_enabled": "is_enabled",
        "name": "name",
    }

    def __init__(self, name, *args, **kwargs):
        """
        Represents the index exclusion filter object from configuration API.

        :param filter: Exclusion filter is defined by a query, a sampling rule, and a active/inactive toggle.
        :type filter: LogsExclusionFilter, optional

        :param is_enabled: Whether or not the exclusion filter is active.
        :type is_enabled: bool, optional

        :param name: Name of the index exclusion filter.
        :type name: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.name = name

    @classmethod
    def _from_openapi_data(cls, name, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsExclusion, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.name = name
        return self
