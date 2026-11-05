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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_metadata_capture_item import AiGatewayMetadataCaptureItem
    from datadog_api_client.v2.model.ai_gateway_capture_override_mode import AiGatewayCaptureOverrideMode
    from datadog_api_client.v2.model.ai_gateway_capture_response_scope import AiGatewayCaptureResponseScope


class AiGatewayCaptureOverride(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_metadata_capture_item import AiGatewayMetadataCaptureItem
        from datadog_api_client.v2.model.ai_gateway_capture_override_mode import AiGatewayCaptureOverrideMode
        from datadog_api_client.v2.model.ai_gateway_capture_response_scope import AiGatewayCaptureResponseScope

        return {
            "created_at": (datetime,),
            "id": (UUID,),
            "metadata_capture": ([AiGatewayMetadataCaptureItem],),
            "mode": (AiGatewayCaptureOverrideMode,),
            "name": (str,),
            "revision": (int,),
            "scope": (AiGatewayCaptureResponseScope,),
            "scope_restricted": (bool,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "created_at": "created_at",
        "id": "id",
        "metadata_capture": "metadata_capture",
        "mode": "mode",
        "name": "name",
        "revision": "revision",
        "scope": "scope",
        "scope_restricted": "scope_restricted",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        created_at: datetime,
        id: UUID,
        mode: AiGatewayCaptureOverrideMode,
        name: str,
        revision: int,
        scope: AiGatewayCaptureResponseScope,
        scope_restricted: bool,
        updated_at: datetime,
        metadata_capture: Union[List[AiGatewayMetadataCaptureItem], UnsetType] = unset,
        **kwargs,
    ):
        """
        Saved data capture override with its request filters, capture mode, revision, and timestamps.

        :param created_at: Timestamp when the override was created.
        :type created_at: datetime

        :param id: UUID identifying the override within the organization.
        :type id: UUID

        :param metadata_capture: Items Metadata-only capture adds, each listed once. An item requires the items whose information it already reveals: ``tool_output_size`` , ``tool_names`` and ``conversation_shape`` require ``tool_usage`` , and ``input_size_by_role`` requires ``tool_output_size``. A set that leaves out a required item is rejected. When several Metadata-only overrides match a request, it gets only the items all of them select.
        :type metadata_capture: [AiGatewayMetadataCaptureItem], optional

        :param mode: Capture mode for matching traffic.
        :type mode: AiGatewayCaptureOverrideMode

        :param name: Display name of the override. Names need not be unique; identify overrides by ``id``.
        :type name: str

        :param revision: Current override revision, required for replacement or deletion.
        :type revision: int

        :param scope: Visible request filters. Provider and model tags are withheld when the caller cannot view them. An empty object or empty tags can represent a fully restricted scope; scope_restricted identifies redaction.
        :type scope: AiGatewayCaptureResponseScope

        :param scope_restricted: Whether provider or model scope metadata was withheld. Omit unchanged scope fields on an unrelated update to preserve their saved values.
        :type scope_restricted: bool

        :param updated_at: Timestamp when the override was last modified.
        :type updated_at: datetime
        """
        if metadata_capture is not unset:
            kwargs["metadata_capture"] = metadata_capture
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.id = id
        self_.mode = mode
        self_.name = name
        self_.revision = revision
        self_.scope = scope
        self_.scope_restricted = scope_restricted
        self_.updated_at = updated_at
