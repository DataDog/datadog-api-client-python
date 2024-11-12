# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AWSLogsServicesResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "logs_services": ([str],),
        }

    attribute_map = {
        "logs_services": "logs_services",
    }

    def __init__(self_, logs_services: List[str], **kwargs):
        """
        AWS Logs Services response body

        :param logs_services: List of AWS services that can send logs to Datadog
        :type logs_services: [str]
        """
        super().__init__(kwargs)

        self_.logs_services = logs_services
