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


class RumPermanentRetentionFilterEditability(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "trace_editable": (bool,),
        }

    attribute_map = {
        "trace_editable": "trace_editable",
    }

    def __init__(self_, trace_editable: Union[bool, UnsetType] = unset, **kwargs):
        """
        Indicates which cross-product fields of a permanent RUM retention filter can be updated.

        :param trace_editable: Whether the APM trace cross-product configuration of the filter can be updated.
        :type trace_editable: bool, optional
        """
        if trace_editable is not unset:
            kwargs["trace_editable"] = trace_editable
        super().__init__(kwargs)
