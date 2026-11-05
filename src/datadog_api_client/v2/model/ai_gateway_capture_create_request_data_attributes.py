# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_metadata_capture_item import AiGatewayMetadataCaptureItem
    from datadog_api_client.v2.model.ai_gateway_capture_create_request_data_attributes_mode import (
        AiGatewayCaptureCreateRequestDataAttributesMode,
    )
    from datadog_api_client.v2.model.ai_gateway_capture_create_request_data_attributes_operation import (
        AiGatewayCaptureCreateRequestDataAttributesOperation,
    )
    from datadog_api_client.v2.model.ai_gateway_capture_scope import AiGatewayCaptureScope


class AiGatewayCaptureCreateRequestDataAttributes(ModelNormal):
    validations = {
        "name": {
            "max_length": 256,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_metadata_capture_item import AiGatewayMetadataCaptureItem
        from datadog_api_client.v2.model.ai_gateway_capture_create_request_data_attributes_mode import (
            AiGatewayCaptureCreateRequestDataAttributesMode,
        )
        from datadog_api_client.v2.model.ai_gateway_capture_create_request_data_attributes_operation import (
            AiGatewayCaptureCreateRequestDataAttributesOperation,
        )
        from datadog_api_client.v2.model.ai_gateway_capture_scope import AiGatewayCaptureScope

        return {
            "configuration_revision": (str,),
            "confirm_full_capture": (bool,),
            "metadata_capture": ([AiGatewayMetadataCaptureItem],),
            "mode": (AiGatewayCaptureCreateRequestDataAttributesMode,),
            "name": (str,),
            "operation": (AiGatewayCaptureCreateRequestDataAttributesOperation,),
            "revision": (int,),
            "scope": (AiGatewayCaptureScope,),
        }

    attribute_map = {
        "configuration_revision": "configuration_revision",
        "confirm_full_capture": "confirm_full_capture",
        "metadata_capture": "metadata_capture",
        "mode": "mode",
        "name": "name",
        "operation": "operation",
        "revision": "revision",
        "scope": "scope",
    }

    def __init__(
        self_,
        configuration_revision: str,
        mode: AiGatewayCaptureCreateRequestDataAttributesMode,
        name: str,
        scope: AiGatewayCaptureScope,
        confirm_full_capture: Union[bool, UnsetType] = unset,
        metadata_capture: Union[List[AiGatewayMetadataCaptureItem], UnsetType] = unset,
        operation: Union[AiGatewayCaptureCreateRequestDataAttributesOperation, UnsetType] = unset,
        revision: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Settings and configuration revision for creating the override.

        :param configuration_revision: Opaque revision of the organization default and all overrides. Writes require the revision returned by a current read or preview.
        :type configuration_revision: str

        :param confirm_full_capture: Set to ``true`` to confirm a change that can enable full capture, including a deletion that causes a ``full_capture`` override or the organization default to apply.
        :type confirm_full_capture: bool, optional

        :param metadata_capture: Items Metadata-only capture adds, each listed once. An item requires the items whose information it already reveals: ``tool_output_size`` , ``tool_names`` and ``conversation_shape`` require ``tool_usage`` , and ``input_size_by_role`` requires ``tool_output_size``. A set that leaves out a required item is rejected. When several Metadata-only overrides match a request, it gets only the items all of them select.
        :type metadata_capture: [AiGatewayMetadataCaptureItem], optional

        :param mode: Capture mode for matching traffic.
        :type mode: AiGatewayCaptureCreateRequestDataAttributesMode

        :param name: Display name of the override. Names need not be unique; identify overrides by ``id``.
        :type name: str

        :param operation: Proposed operation for preview. Write endpoints infer it from the HTTP method.
        :type operation: AiGatewayCaptureCreateRequestDataAttributesOperation, optional

        :param revision: Current override revision, required for replacement or deletion.
        :type revision: int, optional

        :param scope: All selected filters combine with AND, with one value per filter. The ``model`` and ``provider`` tags apply to each actual direct or routed attempt, including fallback destinations. Routes are not selectable filters. At least one filter is required.
            If any matching override uses ``metadata_only`` , that mode applies. Otherwise, if any matching override uses ``full_capture`` , that mode applies. The organization default applies only when no override matches. Overrides have no priority or specificity ordering.
        :type scope: AiGatewayCaptureScope
        """
        if confirm_full_capture is not unset:
            kwargs["confirm_full_capture"] = confirm_full_capture
        if metadata_capture is not unset:
            kwargs["metadata_capture"] = metadata_capture
        if operation is not unset:
            kwargs["operation"] = operation
        if revision is not unset:
            kwargs["revision"] = revision
        super().__init__(kwargs)

        self_.configuration_revision = configuration_revision
        self_.mode = mode
        self_.name = name
        self_.scope = scope
