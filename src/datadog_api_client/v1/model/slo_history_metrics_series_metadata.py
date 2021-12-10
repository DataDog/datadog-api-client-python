# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    date,
    datetime,
    file_type,
    none_type,
)


def lazy_import():
    from datadog_api_client.v1.model.slo_history_metrics_series_metadata_unit import SLOHistoryMetricsSeriesMetadataUnit

    globals()["SLOHistoryMetricsSeriesMetadataUnit"] = SLOHistoryMetricsSeriesMetadataUnit


class SLOHistoryMetricsSeriesMetadata(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "aggr": (str,),
            "expression": (str,),
            "metric": (str,),
            "query_index": (int,),
            "scope": (str,),
            "unit": (
                [SLOHistoryMetricsSeriesMetadataUnit],
                none_type,
            ),
        }

    attribute_map = {
        "aggr": "aggr",
        "expression": "expression",
        "metric": "metric",
        "query_index": "query_index",
        "scope": "scope",
        "unit": "unit",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """SLOHistoryMetricsSeriesMetadata - a model defined in OpenAPI

        Keyword Args:
            aggr (str): [optional] Query aggregator function.
            expression (str): [optional] Query expression.
            metric (str): [optional] Query metric used.
            query_index (int): [optional] Query index from original combined query.
            scope (str): [optional] Query scope.
            unit ([SLOHistoryMetricsSeriesMetadataUnit], none_type): [optional] An array of metric units that contains up to two unit objects. For example, bytes represents one unit object and bytes per second represents two unit objects. If a metric query only has one unit object, the second array element is null.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SLOHistoryMetricsSeriesMetadata, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
