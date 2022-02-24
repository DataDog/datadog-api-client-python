# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.logs_metric_response_attributes import LogsMetricResponseAttributes
    from datadog_api_client.v2.model.logs_metric_type import LogsMetricType

    globals()["LogsMetricResponseAttributes"] = LogsMetricResponseAttributes
    globals()["LogsMetricType"] = LogsMetricType


class LogsMetricResponseData(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "attributes": (LogsMetricResponseAttributes,),
            "id": (str,),
            "type": (LogsMetricType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        The log-based metric properties.

        :param attributes: The object describing a Datadog log-based metric.
        :type attributes: LogsMetricResponseAttributes, optional

        :param id: The name of the log-based metric.
        :type id: str, optional

        :param type: The type of the resource. The value should always be logs_metrics.
        :type type: LogsMetricType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsMetricResponseData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
