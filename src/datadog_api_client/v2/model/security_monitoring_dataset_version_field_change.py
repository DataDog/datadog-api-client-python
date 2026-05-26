# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


class SecurityMonitoringDatasetVersionFieldChange(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "current": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "field": (str,),
            "previous": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
        }

    attribute_map = {
        "current": "current",
        "field": "field",
        "previous": "previous",
    }

    def __init__(self_, current: Any, field: str, previous: Any, **kwargs):
        """
        A single field change between two versions of a dataset.

        :param current: The current value of the field, serialized as a JSON value.
        :type current: bool, date, datetime, dict, float, int, list, str, UUID, none_type

        :param field: The name of the field that changed.
        :type field: str

        :param previous: The previous value of the field, serialized as a JSON value.
        :type previous: bool, date, datetime, dict, float, int, list, str, UUID, none_type
        """
        super().__init__(kwargs)

        self_.current = current
        self_.field = field
        self_.previous = previous
