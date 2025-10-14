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
    from datadog_api_client.v2.model.gcp_scan_options_data_attributes import GcpScanOptionsDataAttributes
    from datadog_api_client.v2.model.gcp_scan_options_data_type import GcpScanOptionsDataType


class GcpScanOptionsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.gcp_scan_options_data_attributes import GcpScanOptionsDataAttributes
        from datadog_api_client.v2.model.gcp_scan_options_data_type import GcpScanOptionsDataType

        return {
            "attributes": (GcpScanOptionsDataAttributes,),
            "id": (str,),
            "type": (GcpScanOptionsDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: GcpScanOptionsDataType,
        attributes: Union[GcpScanOptionsDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Single GCP scan options entry.

        :param attributes: Attributes for GCP scan options configuration.
        :type attributes: GcpScanOptionsDataAttributes, optional

        :param id: The GCP project ID.
        :type id: str

        :param type: GCP scan options resource type.
        :type type: GcpScanOptionsDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
