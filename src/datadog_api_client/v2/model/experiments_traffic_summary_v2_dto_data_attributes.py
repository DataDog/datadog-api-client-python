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
    from datadog_api_client.v2.model.experiments_traffic_summary_v2_dto_data_attributes_variants_items import (
        ExperimentsTrafficSummaryV2DTODataAttributesVariantsItems,
    )


class ExperimentsTrafficSummaryV2DTODataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_traffic_summary_v2_dto_data_attributes_variants_items import (
            ExperimentsTrafficSummaryV2DTODataAttributesVariantsItems,
        )

        return {
            "is_traffic_imbalanced": (bool,),
            "total_subjects": (int,),
            "variants": ([ExperimentsTrafficSummaryV2DTODataAttributesVariantsItems],),
        }

    attribute_map = {
        "is_traffic_imbalanced": "is_traffic_imbalanced",
        "total_subjects": "total_subjects",
        "variants": "variants",
    }

    def __init__(
        self_,
        is_traffic_imbalanced: Union[bool, UnsetType] = unset,
        total_subjects: Union[int, UnsetType] = unset,
        variants: Union[List[ExperimentsTrafficSummaryV2DTODataAttributesVariantsItems], UnsetType] = unset,
        **kwargs,
    ):
        """
        Details of the experiment traffic summary.

        :param is_traffic_imbalanced: Whether the observed variant traffic is imbalanced.
        :type is_traffic_imbalanced: bool, optional

        :param total_subjects: Total number of subjects included in the traffic summary.
        :type total_subjects: int, optional

        :param variants: Exposure counts for each experiment variant.
        :type variants: [ExperimentsTrafficSummaryV2DTODataAttributesVariantsItems], optional
        """
        if is_traffic_imbalanced is not unset:
            kwargs["is_traffic_imbalanced"] = is_traffic_imbalanced
        if total_subjects is not unset:
            kwargs["total_subjects"] = total_subjects
        if variants is not unset:
            kwargs["variants"] = variants
        super().__init__(kwargs)
