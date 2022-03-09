# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ProcessQueryDefinition(ModelNormal):
    validations = {
        "limit": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "filter_by": ([str],),
            "limit": (int,),
            "metric": (str,),
            "search_by": (str,),
        }

    attribute_map = {
        "filter_by": "filter_by",
        "limit": "limit",
        "metric": "metric",
        "search_by": "search_by",
    }

    def __init__(self, metric, *args, **kwargs):
        """
        The process query to use in the widget.

        :param filter_by: List of processes.
        :type filter_by: [str], optional

        :param limit: Max number of items in the filter list.
        :type limit: int, optional

        :param metric: Your chosen metric.
        :type metric: str

        :param search_by: Your chosen search term.
        :type search_by: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.metric = metric

    @classmethod
    def _from_openapi_data(cls, metric, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ProcessQueryDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.metric = metric
        return self
