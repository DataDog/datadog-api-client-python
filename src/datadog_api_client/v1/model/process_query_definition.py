# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class ProcessQueryDefinition(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {
        "limit": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types():
        return {
            "filter_by": ([str],),
            "limit": (int,),
            "metric": (str,),
            "search_by": (str,),
        }

    attribute_map = {
        "metric": "metric",
        "filter_by": "filter_by",
        "limit": "limit",
        "search_by": "search_by",
    }

    read_only_vars = {}

    def __init__(self, metric, *args, **kwargs):
        """ProcessQueryDefinition - a model defined in OpenAPI


        :param metric: Your chosen metric.
        :type metric: str

        :param filter_by: List of processes.
        :type filter_by: [str], optional

        :param limit: Max number of items in the filter list.
        :type limit: int, optional

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
