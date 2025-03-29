# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.datadog_logs_destination_type import DatadogLogsDestinationType


class DatadogLogsDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.datadog_logs_destination_type import DatadogLogsDestinationType

        return {
            "id": (str,),
            "inputs": ([str],),
            "type": (DatadogLogsDestinationType,),
        }

    attribute_map = {
        "id": "id",
        "inputs": "inputs",
        "type": "type",
    }

    def __init__(self_, id: str, inputs: List[str], type: DatadogLogsDestinationType, **kwargs):
        """
        The ``datadog_logs`` destination forwards logs to Datadog Logs.

        :param id: The ``DatadogLogsDestination`` ``id``.
        :type id: str

        :param inputs: The ``DatadogLogsDestination`` ``inputs``.
        :type inputs: [str]

        :param type: The definition of ``DatadogLogsDestinationType`` object.
        :type type: DatadogLogsDestinationType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.inputs = inputs
        self_.type = type
