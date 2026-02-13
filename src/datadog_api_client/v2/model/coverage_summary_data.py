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
    from datadog_api_client.v2.model.coverage_summary_attributes import CoverageSummaryAttributes
    from datadog_api_client.v2.model.coverage_summary_type import CoverageSummaryType


class CoverageSummaryData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.coverage_summary_attributes import CoverageSummaryAttributes
        from datadog_api_client.v2.model.coverage_summary_type import CoverageSummaryType

        return {
            "attributes": (CoverageSummaryAttributes,),
            "id": (str,),
            "type": (CoverageSummaryType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[CoverageSummaryAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[CoverageSummaryType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for coverage summary response.

        :param attributes: Attributes object for code coverage summary response.
        :type attributes: CoverageSummaryAttributes, optional

        :param id: Unique identifier for the coverage summary (base64-hashed).
        :type id: str, optional

        :param type: JSON:API type for coverage summary response. The value must always be ``ci_app_coverage_summary``.
        :type type: CoverageSummaryType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
