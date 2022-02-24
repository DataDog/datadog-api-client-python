# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.logs_metric_create_attributes import LogsMetricCreateAttributes
    from datadog_api_client.v2.model.logs_metric_type import LogsMetricType

    globals()["LogsMetricCreateAttributes"] = LogsMetricCreateAttributes
    globals()["LogsMetricType"] = LogsMetricType


class LogsMetricCreateData(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "attributes": (LogsMetricCreateAttributes,),
            "id": (str,),
            "type": (LogsMetricType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, attributes, id, type, *args, **kwargs):
        """
        The new log-based metric properties.

        :param attributes: The object describing the Datadog log-based metric to create.
        :type attributes: LogsMetricCreateAttributes

        :param id: The name of the log-based metric.
        :type id: str

        :param type: The type of the resource. The value should always be logs_metrics.
        :type type: LogsMetricType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.id = id
        self.type = type

    @classmethod
    def _from_openapi_data(cls, attributes, id, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsMetricCreateData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.id = id
        self.type = type
        return self
