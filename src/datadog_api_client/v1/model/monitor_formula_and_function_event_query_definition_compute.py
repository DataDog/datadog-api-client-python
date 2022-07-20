# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MonitorFormulaAndFunctionEventQueryDefinitionCompute(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_formula_and_function_event_aggregation import (
            MonitorFormulaAndFunctionEventAggregation,
        )

        return {
            "aggregation": (MonitorFormulaAndFunctionEventAggregation,),
            "interval": (int,),
            "metric": (str,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "interval": "interval",
        "metric": "metric",
    }

    def __init__(self, aggregation, *args, **kwargs):
        """
        Compute options.

        :param aggregation: Aggregation methods for event platform queries.
        :type aggregation: MonitorFormulaAndFunctionEventAggregation

        :param interval: A time interval in milliseconds.
        :type interval: int, optional

        :param metric: Measurable attribute to compute.
        :type metric: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.aggregation = aggregation

    @classmethod
    def _from_openapi_data(cls, aggregation, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MonitorFormulaAndFunctionEventQueryDefinitionCompute, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.aggregation = aggregation
        return self
