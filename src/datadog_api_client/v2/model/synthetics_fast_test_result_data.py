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
    from datadog_api_client.v2.model.synthetics_fast_test_result_attributes import SyntheticsFastTestResultAttributes
    from datadog_api_client.v2.model.synthetics_fast_test_result_type import SyntheticsFastTestResultType


class SyntheticsFastTestResultData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_fast_test_result_attributes import (
            SyntheticsFastTestResultAttributes,
        )
        from datadog_api_client.v2.model.synthetics_fast_test_result_type import SyntheticsFastTestResultType

        return {
            "attributes": (SyntheticsFastTestResultAttributes,),
            "id": (str,),
            "type": (SyntheticsFastTestResultType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[SyntheticsFastTestResultAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[SyntheticsFastTestResultType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Fast test result data object (JSON:API format).

        :param attributes: Attributes of the fast test result.
        :type attributes: SyntheticsFastTestResultAttributes, optional

        :param id: The UUID of the fast test, used as the result identifier.
        :type id: str, optional

        :param type: JSON:API type for a fast test result.
        :type type: SyntheticsFastTestResultType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
