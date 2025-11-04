# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.facet_info_response_data_attributes_result_range import (
        FacetInfoResponseDataAttributesResultRange,
    )
    from datadog_api_client.v2.model.facet_info_response_data_attributes_result_values_items import (
        FacetInfoResponseDataAttributesResultValuesItems,
    )


class FacetInfoResponseDataAttributesResult(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.facet_info_response_data_attributes_result_range import (
            FacetInfoResponseDataAttributesResultRange,
        )
        from datadog_api_client.v2.model.facet_info_response_data_attributes_result_values_items import (
            FacetInfoResponseDataAttributesResultValuesItems,
        )

        return {
            "range": (FacetInfoResponseDataAttributesResultRange,),
            "values": ([FacetInfoResponseDataAttributesResultValuesItems],),
        }

    attribute_map = {
        "range": "range",
        "values": "values",
    }

    def __init__(
        self_,
        range: Union[FacetInfoResponseDataAttributesResultRange, UnsetType] = unset,
        values: Union[List[FacetInfoResponseDataAttributesResultValuesItems], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param range:
        :type range: FacetInfoResponseDataAttributesResultRange, optional

        :param values:
        :type values: [FacetInfoResponseDataAttributesResultValuesItems], optional
        """
        if range is not unset:
            kwargs["range"] = range
        if values is not unset:
            kwargs["values"] = values
        super().__init__(kwargs)
