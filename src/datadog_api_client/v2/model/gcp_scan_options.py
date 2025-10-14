# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.gcp_scan_options_data import GcpScanOptionsData


class GcpScanOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.gcp_scan_options_data import GcpScanOptionsData

        return {
            "data": (GcpScanOptionsData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[GcpScanOptionsData, UnsetType] = unset, **kwargs):
        """
        Response object containing GCP scan options for a single project.

        :param data: Single GCP scan options entry.
        :type data: GcpScanOptionsData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
