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
    from datadog_api_client.v1_20270101.model.number_format_unit_canonical_type import NumberFormatUnitCanonicalType


class NumberFormatUnitCanonical(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.number_format_unit_canonical_type import NumberFormatUnitCanonicalType

        return {
            "per_unit_name": (str,),
            "type": (NumberFormatUnitCanonicalType,),
            "unit_name": (str,),
        }

    attribute_map = {
        "per_unit_name": "per_unit_name",
        "type": "type",
        "unit_name": "unit_name",
    }

    def __init__(
        self_,
        type: NumberFormatUnitCanonicalType,
        per_unit_name: Union[str, UnsetType] = unset,
        unit_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param per_unit_name: Datadog canonical unit identifier, for example byte or second.
        :type per_unit_name: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: NumberFormatUnitCanonicalType

        :param unit_name: Datadog canonical unit identifier, for example byte or second.
        :type unit_name: str, optional
        """
        if per_unit_name is not unset:
            kwargs["per_unit_name"] = per_unit_name
        if unit_name is not unset:
            kwargs["unit_name"] = unit_name
        super().__init__(kwargs)

        self_.type = type
