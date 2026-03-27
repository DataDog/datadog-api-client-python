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
    from datadog_api_client.v2.model.synthetics_test_version_action_metadata import SyntheticsTestVersionActionMetadata


class SyntheticsTestVersionChangeMetadataItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_version_action_metadata import (
            SyntheticsTestVersionActionMetadata,
        )

        return {
            "action": (str,),
            "action_metadata": (SyntheticsTestVersionActionMetadata,),
        }

    attribute_map = {
        "action": "action",
        "action_metadata": "action_metadata",
    }

    def __init__(
        self_,
        action: Union[str, UnsetType] = unset,
        action_metadata: Union[SyntheticsTestVersionActionMetadata, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object describing a single change within a version.

        :param action: The action that was performed (for example, ``updated`` or ``created`` ).
        :type action: str, optional

        :param action_metadata: Object containing metadata about a change action.
        :type action_metadata: SyntheticsTestVersionActionMetadata, optional
        """
        if action is not unset:
            kwargs["action"] = action
        if action_metadata is not unset:
            kwargs["action_metadata"] = action_metadata
        super().__init__(kwargs)
