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
    from datadog_api_client.v2.model.ai_gateway_capture_delete_request_data_attributes_mode import (
        AiGatewayCaptureDeleteRequestDataAttributesMode,
    )
    from datadog_api_client.v2.model.ai_gateway_capture_delete_request_data_attributes_operation import (
        AiGatewayCaptureDeleteRequestDataAttributesOperation,
    )
    from datadog_api_client.v2.model.ai_gateway_capture_scope import AiGatewayCaptureScope


class AiGatewayCaptureDeleteRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_capture_delete_request_data_attributes_mode import (
            AiGatewayCaptureDeleteRequestDataAttributesMode,
        )
        from datadog_api_client.v2.model.ai_gateway_capture_delete_request_data_attributes_operation import (
            AiGatewayCaptureDeleteRequestDataAttributesOperation,
        )
        from datadog_api_client.v2.model.ai_gateway_capture_scope import AiGatewayCaptureScope

        return {
            "configuration_revision": (str,),
            "confirm_full_capture": (bool,),
            "mode": (AiGatewayCaptureDeleteRequestDataAttributesMode,),
            "name": (str,),
            "operation": (AiGatewayCaptureDeleteRequestDataAttributesOperation,),
            "revision": (int,),
            "scope": (AiGatewayCaptureScope,),
        }

    attribute_map = {
        "configuration_revision": "configuration_revision",
        "confirm_full_capture": "confirm_full_capture",
        "mode": "mode",
        "name": "name",
        "operation": "operation",
        "revision": "revision",
        "scope": "scope",
    }

    def __init__(
        self_,
        configuration_revision: str,
        revision: int,
        confirm_full_capture: Union[bool, UnsetType] = unset,
        mode: Union[AiGatewayCaptureDeleteRequestDataAttributesMode, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        operation: Union[AiGatewayCaptureDeleteRequestDataAttributesOperation, UnsetType] = unset,
        scope: Union[AiGatewayCaptureScope, UnsetType] = unset,
        **kwargs,
    ):
        """
        Revisions and confirmation used to delete the override.

        :param configuration_revision: Opaque revision of the organization default and all overrides. Writes require the revision returned by a current read or preview.
        :type configuration_revision: str

        :param confirm_full_capture: Set to ``true`` to confirm a change that can enable full capture, including a deletion that causes a ``full_capture`` override or the organization default to apply.
        :type confirm_full_capture: bool, optional

        :param mode: Capture mode for matching traffic.
        :type mode: AiGatewayCaptureDeleteRequestDataAttributesMode, optional

        :param name: Display name of the override. Names need not be unique; identify overrides by ``id``.
        :type name: str, optional

        :param operation: Proposed operation for preview. Write endpoints infer it from the HTTP method.
        :type operation: AiGatewayCaptureDeleteRequestDataAttributesOperation, optional

        :param revision: Current override revision, required for replacement or deletion.
        :type revision: int

        :param scope: All selected filters combine with AND, with one value per filter. The ``model`` and ``provider`` tags apply to each actual direct or routed attempt, including fallback destinations. Routes are not selectable filters. At least one filter is required.
            If any matching override uses ``metadata_only`` , that mode applies. Otherwise, if any matching override uses ``full_capture`` , that mode applies. The organization default applies only when no override matches. Overrides have no priority or specificity ordering.
        :type scope: AiGatewayCaptureScope, optional
        """
        if confirm_full_capture is not unset:
            kwargs["confirm_full_capture"] = confirm_full_capture
        if mode is not unset:
            kwargs["mode"] = mode
        if name is not unset:
            kwargs["name"] = name
        if operation is not unset:
            kwargs["operation"] = operation
        if scope is not unset:
            kwargs["scope"] = scope
        super().__init__(kwargs)

        self_.configuration_revision = configuration_revision
        self_.revision = revision
