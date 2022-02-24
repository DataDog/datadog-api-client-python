# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class GraphSnapshot(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "graph_def": (str,),
            "metric_query": (str,),
            "snapshot_url": (str,),
        }

    attribute_map = {
        "graph_def": "graph_def",
        "metric_query": "metric_query",
        "snapshot_url": "snapshot_url",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Object representing a graph snapshot.

        :param graph_def: A JSON document defining the graph. `graph_def` can be used instead of `metric_query`.
            The JSON document uses the [grammar defined here](https://docs.datadoghq.com/graphing/graphing_json/#grammar)
            and should be formatted to a single line then URL encoded.
        :type graph_def: str, optional

        :param metric_query: The metric query. One of `metric_query` or `graph_def` is required.
        :type metric_query: str, optional

        :param snapshot_url: URL of your [graph snapshot](https://docs.datadoghq.com/metrics/explorer/#snapshot).
        :type snapshot_url: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(GraphSnapshot, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
