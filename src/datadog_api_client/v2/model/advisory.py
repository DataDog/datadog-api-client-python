# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class Advisory(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "base_severity": (str,),
            "id": (str,),
            "severity": (str,),
        }

    attribute_map = {
        "base_severity": "base_severity",
        "id": "id",
        "severity": "severity",
    }

    def __init__(self_, base_severity: str, id: str, severity: Union[str, UnsetType] = unset, **kwargs):
        """
        Advisory.

        :param base_severity: Advisory base severity.
        :type base_severity: str

        :param id: Advisory id.
        :type id: str

        :param severity: Advisory Datadog severity.
        :type severity: str, optional
        """
        if severity is not unset:
            kwargs["severity"] = severity
        super().__init__(kwargs)

        self_.base_severity = base_severity
        self_.id = id
