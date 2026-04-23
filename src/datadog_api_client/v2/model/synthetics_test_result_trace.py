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


class SyntheticsTestResultTrace(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "otel_id": (str,),
        }

    attribute_map = {
        "id": "id",
        "otel_id": "otel_id",
    }

    def __init__(self_, id: Union[str, UnsetType] = unset, otel_id: Union[str, UnsetType] = unset, **kwargs):
        """
        Trace identifiers associated with a Synthetic test result.

        :param id: Datadog APM trace identifier.
        :type id: str, optional

        :param otel_id: OpenTelemetry trace identifier.
        :type otel_id: str, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if otel_id is not unset:
            kwargs["otel_id"] = otel_id
        super().__init__(kwargs)
