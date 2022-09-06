# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsMetricResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_metric_response_data import LogsMetricResponseData

        return {
            "data": (LogsMetricResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, *args, **kwargs):
        """
        The log-based metric object.

        :param data: The log-based metric properties.
        :type data: LogsMetricResponseData, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
