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
    from datadog_api_client.v2.model.synthetics_test_parent_suite_attributes import SyntheticsTestParentSuiteAttributes
    from datadog_api_client.v2.model.synthetics_test_parent_suite_type import SyntheticsTestParentSuiteType


class SyntheticsTestParentSuiteData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_parent_suite_attributes import (
            SyntheticsTestParentSuiteAttributes,
        )
        from datadog_api_client.v2.model.synthetics_test_parent_suite_type import SyntheticsTestParentSuiteType

        return {
            "attributes": (SyntheticsTestParentSuiteAttributes,),
            "id": (str,),
            "type": (SyntheticsTestParentSuiteType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[SyntheticsTestParentSuiteAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[SyntheticsTestParentSuiteType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for a parent suite.

        :param attributes: Object containing details about a parent suite of a Synthetic test.
        :type attributes: SyntheticsTestParentSuiteAttributes, optional

        :param id: The public ID of the parent suite.
        :type id: str, optional

        :param type: Type of the parent suite resource.
        :type type: SyntheticsTestParentSuiteType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
