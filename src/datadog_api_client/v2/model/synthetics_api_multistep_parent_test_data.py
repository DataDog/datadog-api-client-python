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
    from datadog_api_client.v2.model.synthetics_api_multistep_parent_test_attributes import (
        SyntheticsApiMultistepParentTestAttributes,
    )
    from datadog_api_client.v2.model.synthetics_api_multistep_parent_test_type import (
        SyntheticsApiMultistepParentTestType,
    )


class SyntheticsApiMultistepParentTestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_api_multistep_parent_test_attributes import (
            SyntheticsApiMultistepParentTestAttributes,
        )
        from datadog_api_client.v2.model.synthetics_api_multistep_parent_test_type import (
            SyntheticsApiMultistepParentTestType,
        )

        return {
            "attributes": (SyntheticsApiMultistepParentTestAttributes,),
            "id": (str,),
            "type": (SyntheticsApiMultistepParentTestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[SyntheticsApiMultistepParentTestAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[SyntheticsApiMultistepParentTestType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for a parent API multistep test.

        :param attributes: Attributes of a parent API multistep test.
        :type attributes: SyntheticsApiMultistepParentTestAttributes, optional

        :param id: The public ID of the parent test.
        :type id: str, optional

        :param type: Type of the parent test resource.
        :type type: SyntheticsApiMultistepParentTestType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
