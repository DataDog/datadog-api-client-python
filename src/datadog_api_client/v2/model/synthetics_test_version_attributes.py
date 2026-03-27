# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_test_version_author import SyntheticsTestVersionAuthor
    from datadog_api_client.v2.model.synthetics_test_version_change_metadata_item import (
        SyntheticsTestVersionChangeMetadataItem,
    )


class SyntheticsTestVersionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_version_author import SyntheticsTestVersionAuthor
        from datadog_api_client.v2.model.synthetics_test_version_change_metadata_item import (
            SyntheticsTestVersionChangeMetadataItem,
        )

        return {
            "author": (SyntheticsTestVersionAuthor,),
            "change_metadata": ([SyntheticsTestVersionChangeMetadataItem],),
            "payload": (
                {
                    str: (
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
                    )
                },
            ),
            "version_payload_created_at": (datetime,),
        }

    attribute_map = {
        "author": "author",
        "change_metadata": "change_metadata",
        "payload": "payload",
        "version_payload_created_at": "version_payload_created_at",
    }

    def __init__(
        self_,
        author: Union[SyntheticsTestVersionAuthor, UnsetType] = unset,
        change_metadata: Union[List[SyntheticsTestVersionChangeMetadataItem], UnsetType] = unset,
        payload: Union[Dict[str, Any], UnsetType] = unset,
        version_payload_created_at: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a specific Synthetic test version.

        :param author: Object describing the author of a test version.
        :type author: SyntheticsTestVersionAuthor, optional

        :param change_metadata: List of metadata describing individual changes in this version.
            Only returned when the ``include_change_metadata`` query parameter is ``true``.
        :type change_metadata: [SyntheticsTestVersionChangeMetadataItem], optional

        :param payload: The full test configuration at this version.
        :type payload: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param version_payload_created_at: Timestamp of when this version was created.
        :type version_payload_created_at: datetime, optional
        """
        if author is not unset:
            kwargs["author"] = author
        if change_metadata is not unset:
            kwargs["change_metadata"] = change_metadata
        if payload is not unset:
            kwargs["payload"] = payload
        if version_payload_created_at is not unset:
            kwargs["version_payload_created_at"] = version_payload_created_at
        super().__init__(kwargs)
