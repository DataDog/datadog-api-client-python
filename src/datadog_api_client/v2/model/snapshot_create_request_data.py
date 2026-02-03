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
    from datadog_api_client.v2.model.snapshot_create_request_data_attributes import SnapshotCreateRequestDataAttributes
    from datadog_api_client.v2.model.snapshot_update_request_data_type import SnapshotUpdateRequestDataType


class SnapshotCreateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.snapshot_create_request_data_attributes import (
            SnapshotCreateRequestDataAttributes,
        )
        from datadog_api_client.v2.model.snapshot_update_request_data_type import SnapshotUpdateRequestDataType

        return {
            "attributes": (SnapshotCreateRequestDataAttributes,),
            "type": (SnapshotUpdateRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: SnapshotUpdateRequestDataType,
        attributes: Union[SnapshotCreateRequestDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes:
        :type attributes: SnapshotCreateRequestDataAttributes, optional

        :param type: Snapshots resource type.
        :type type: SnapshotUpdateRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
