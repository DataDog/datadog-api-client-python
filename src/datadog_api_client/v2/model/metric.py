# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (  # noqa: F401
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
    from datadog_api_client.v2.model.metric_type import MetricType

    globals()["MetricType"] = MetricType


class Metric(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "id": (str,),
            "type": (MetricType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """Metric - a model defined in OpenAPI

        Keyword Args:
            id (str): [optional] The metric name for this resource.
            type (MetricType): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(Metric, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
