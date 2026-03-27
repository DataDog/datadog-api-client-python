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
    from datadog_api_client.v2.model.synthetics_api_multistep_subtest_attributes import (
        SyntheticsApiMultistepSubtestAttributes,
    )
    from datadog_api_client.v2.model.synthetics_api_multistep_subtest_type import SyntheticsApiMultistepSubtestType


class SyntheticsApiMultistepSubtestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_api_multistep_subtest_attributes import (
            SyntheticsApiMultistepSubtestAttributes,
        )
        from datadog_api_client.v2.model.synthetics_api_multistep_subtest_type import SyntheticsApiMultistepSubtestType

        return {
            "attributes": (SyntheticsApiMultistepSubtestAttributes,),
            "id": (str,),
            "type": (SyntheticsApiMultistepSubtestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[SyntheticsApiMultistepSubtestAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[SyntheticsApiMultistepSubtestType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for a Synthetic API multistep subtest.

        :param attributes: Attributes of a Synthetic API multistep subtest.
        :type attributes: SyntheticsApiMultistepSubtestAttributes, optional

        :param id: The public ID of the subtest.
        :type id: str, optional

        :param type: Type of the subtest resource.
        :type type: SyntheticsApiMultistepSubtestType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
