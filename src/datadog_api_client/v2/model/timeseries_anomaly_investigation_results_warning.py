# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class TimeseriesAnomalyInvestigationResultsWarning(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "message": (str,),
            "name": (str,),
        }

    attribute_map = {
        "message": "message",
        "name": "name",
    }

    def __init__(self_, message: str, name: str, **kwargs):
        """
        Non-fatal warning produced while executing the investigation.

        :param message: Human-readable warning message.
        :type message: str

        :param name: Machine-readable warning name.
        :type name: str
        """
        super().__init__(kwargs)

        self_.message = message
        self_.name = name
