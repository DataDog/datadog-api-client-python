# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class FunnelQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.funnel_source import FunnelSource
        from datadog_api_client.v1.model.funnel_step import FunnelStep

        return {
            "data_source": (FunnelSource,),
            "query_string": (str,),
            "steps": ([FunnelStep],),
        }

    attribute_map = {
        "data_source": "data_source",
        "query_string": "query_string",
        "steps": "steps",
    }

    def __init__(self, data_source, query_string, steps, *args, **kwargs):
        """
        Updated funnel widget.

        :param data_source: Source from which to query items to display in the funnel.
        :type data_source: FunnelSource

        :param query_string: The widget query.
        :type query_string: str

        :param steps: List of funnel steps.
        :type steps: [FunnelStep]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.data_source = data_source
        self.query_string = query_string
        self.steps = steps

    @classmethod
    def _from_openapi_data(cls, data_source, query_string, steps, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(FunnelQuery, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.data_source = data_source
        self.query_string = query_string
        self.steps = steps
        return self
