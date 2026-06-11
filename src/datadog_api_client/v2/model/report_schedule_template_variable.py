# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ReportScheduleTemplateVariable(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "values": ([str],),
        }

    attribute_map = {
        "name": "name",
        "values": "values",
    }

    def __init__(self_, name: str, values: List[str], **kwargs):
        """
        A dashboard template variable applied when rendering the report.

        :param name: The name of the template variable.
        :type name: str

        :param values: The selected values for the template variable.
        :type values: [str]
        """
        super().__init__(kwargs)

        self_.name = name
        self_.values = values
