# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_test_version_change_metadata_item import (
        SyntheticsTestVersionChangeMetadataItem,
    )


class SyntheticsTestVersionChangeAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_version_change_metadata_item import (
            SyntheticsTestVersionChangeMetadataItem,
        )

        return {
            "author_uuid": (str,),
            "change_metadata": ([SyntheticsTestVersionChangeMetadataItem],),
            "version_number": (int,),
            "version_payload_created_at": (datetime,),
        }

    attribute_map = {
        "author_uuid": "author_uuid",
        "change_metadata": "change_metadata",
        "version_number": "version_number",
        "version_payload_created_at": "version_payload_created_at",
    }

    def __init__(
        self_,
        author_uuid: Union[str, UnsetType] = unset,
        change_metadata: Union[List[SyntheticsTestVersionChangeMetadataItem], UnsetType] = unset,
        version_number: Union[int, UnsetType] = unset,
        version_payload_created_at: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a version change record.

        :param author_uuid: UUID of the user who created this version.
        :type author_uuid: str, optional

        :param change_metadata: List of metadata describing individual changes in this version.
        :type change_metadata: [SyntheticsTestVersionChangeMetadataItem], optional

        :param version_number: The sequential version number.
        :type version_number: int, optional

        :param version_payload_created_at: Timestamp of when this version was created.
        :type version_payload_created_at: datetime, optional
        """
        if author_uuid is not unset:
            kwargs["author_uuid"] = author_uuid
        if change_metadata is not unset:
            kwargs["change_metadata"] = change_metadata
        if version_number is not unset:
            kwargs["version_number"] = version_number
        if version_payload_created_at is not unset:
            kwargs["version_payload_created_at"] = version_payload_created_at
        super().__init__(kwargs)
