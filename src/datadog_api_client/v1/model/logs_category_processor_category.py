# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsCategoryProcessorCategory(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_filter import LogsFilter

        return {
            "filter": (LogsFilter,),
            "name": (str,),
        }

    attribute_map = {
        "filter": "filter",
        "name": "name",
    }

    def __init__(self, *args, **kwargs):
        """
        Object describing the logs filter.

        :param filter: Filter for logs.
        :type filter: LogsFilter, optional

        :param name: Value to assign to the target attribute.
        :type name: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsCategoryProcessorCategory, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
