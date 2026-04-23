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
    from datadog_api_client.v2.model.synthetics_test_result_summary_attributes import (
        SyntheticsTestResultSummaryAttributes,
    )
    from datadog_api_client.v2.model.synthetics_test_result_relationships import SyntheticsTestResultRelationships
    from datadog_api_client.v2.model.synthetics_test_result_summary_type import SyntheticsTestResultSummaryType


class SyntheticsTestResultSummaryData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_summary_attributes import (
            SyntheticsTestResultSummaryAttributes,
        )
        from datadog_api_client.v2.model.synthetics_test_result_relationships import SyntheticsTestResultRelationships
        from datadog_api_client.v2.model.synthetics_test_result_summary_type import SyntheticsTestResultSummaryType

        return {
            "attributes": (SyntheticsTestResultSummaryAttributes,),
            "id": (str,),
            "relationships": (SyntheticsTestResultRelationships,),
            "type": (SyntheticsTestResultSummaryType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[SyntheticsTestResultSummaryAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[SyntheticsTestResultRelationships, UnsetType] = unset,
        type: Union[SyntheticsTestResultSummaryType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Wrapper object for a Synthetic test result summary.

        :param attributes: Attributes of a Synthetic test result summary.
        :type attributes: SyntheticsTestResultSummaryAttributes, optional

        :param id: The result ID.
        :type id: str, optional

        :param relationships: Relationships for a Synthetic test result.
        :type relationships: SyntheticsTestResultRelationships, optional

        :param type: Type of the Synthetic test result summary resource, ``result_summary``.
        :type type: SyntheticsTestResultSummaryType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
