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
    from datadog_api_client.v2.model.synthetics_test_version_change_attributes import (
        SyntheticsTestVersionChangeAttributes,
    )
    from datadog_api_client.v2.model.synthetics_test_version_change_type import SyntheticsTestVersionChangeType


class SyntheticsTestVersionChangeData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_version_change_attributes import (
            SyntheticsTestVersionChangeAttributes,
        )
        from datadog_api_client.v2.model.synthetics_test_version_change_type import SyntheticsTestVersionChangeType

        return {
            "attributes": (SyntheticsTestVersionChangeAttributes,),
            "id": (str,),
            "type": (SyntheticsTestVersionChangeType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[SyntheticsTestVersionChangeAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[SyntheticsTestVersionChangeType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for a version change record.

        :param attributes: Attributes of a version change record.
        :type attributes: SyntheticsTestVersionChangeAttributes, optional

        :param id: UUID of the version change record.
        :type id: str, optional

        :param type: Type of the version metadata resource.
        :type type: SyntheticsTestVersionChangeType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
