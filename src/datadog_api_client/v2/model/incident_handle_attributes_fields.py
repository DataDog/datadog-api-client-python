# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class IncidentHandleAttributesFields(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "severity": ([str],),
        }

    attribute_map = {
        "severity": "severity",
    }

    def __init__(self_, severity: Union[List[str], UnsetType] = unset, **kwargs):
        """
        Dynamic fields associated with the handle

        :param severity: Severity levels associated with the handle
        :type severity: [str], optional
        """
        if severity is not unset:
            kwargs["severity"] = severity
        super().__init__(kwargs)
