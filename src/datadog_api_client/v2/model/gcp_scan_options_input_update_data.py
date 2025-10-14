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
    from datadog_api_client.v2.model.gcp_scan_options_input_update_data_attributes import (
        GcpScanOptionsInputUpdateDataAttributes,
    )
    from datadog_api_client.v2.model.gcp_scan_options_input_update_data_type import GcpScanOptionsInputUpdateDataType


class GcpScanOptionsInputUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.gcp_scan_options_input_update_data_attributes import (
            GcpScanOptionsInputUpdateDataAttributes,
        )
        from datadog_api_client.v2.model.gcp_scan_options_input_update_data_type import (
            GcpScanOptionsInputUpdateDataType,
        )

        return {
            "attributes": (GcpScanOptionsInputUpdateDataAttributes,),
            "id": (str,),
            "type": (GcpScanOptionsInputUpdateDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: GcpScanOptionsInputUpdateDataType,
        attributes: Union[GcpScanOptionsInputUpdateDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for updating the scan options of a single GCP project.

        :param attributes: Attributes for updating GCP scan options configuration.
        :type attributes: GcpScanOptionsInputUpdateDataAttributes, optional

        :param id: The GCP project ID.
        :type id: str

        :param type: GCP scan options resource type.
        :type type: GcpScanOptionsInputUpdateDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
