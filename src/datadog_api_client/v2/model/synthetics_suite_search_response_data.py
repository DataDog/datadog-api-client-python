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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_suite_search_response_data_attributes import (
        SyntheticsSuiteSearchResponseDataAttributes,
    )
    from datadog_api_client.v2.model.suite_search_response_type import SuiteSearchResponseType


class SyntheticsSuiteSearchResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_suite_search_response_data_attributes import (
            SyntheticsSuiteSearchResponseDataAttributes,
        )
        from datadog_api_client.v2.model.suite_search_response_type import SuiteSearchResponseType

        return {
            "attributes": (SyntheticsSuiteSearchResponseDataAttributes,),
            "id": (UUID,),
            "type": (SuiteSearchResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[SyntheticsSuiteSearchResponseDataAttributes, UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        type: Union[SuiteSearchResponseType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Synthetics suite search response data

        :param attributes: Synthetics suite search response data attributes
        :type attributes: SyntheticsSuiteSearchResponseDataAttributes, optional

        :param id:
        :type id: UUID, optional

        :param type:
        :type type: SuiteSearchResponseType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
