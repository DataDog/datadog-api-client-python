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
    from datadog_api_client.v2.model.experiments_variant_results_v2_dto_data_attributes_metrics_items import (
        ExperimentsVariantResultsV2DTODataAttributesMetricsItems,
    )


class ExperimentsVariantResultsV2DTODataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_variant_results_v2_dto_data_attributes_metrics_items import (
            ExperimentsVariantResultsV2DTODataAttributesMetricsItems,
        )

        return {
            "assignment_count": (int,),
            "experiment_id": (str,),
            "is_control": (bool,),
            "metrics": ([ExperimentsVariantResultsV2DTODataAttributesMetricsItems],),
            "variant_key": (str,),
            "variant_name": (str,),
        }

    attribute_map = {
        "assignment_count": "assignment_count",
        "experiment_id": "experiment_id",
        "is_control": "is_control",
        "metrics": "metrics",
        "variant_key": "variant_key",
        "variant_name": "variant_name",
    }

    def __init__(
        self_,
        assignment_count: Union[int, UnsetType] = unset,
        experiment_id: Union[str, UnsetType] = unset,
        is_control: Union[bool, UnsetType] = unset,
        metrics: Union[List[ExperimentsVariantResultsV2DTODataAttributesMetricsItems], UnsetType] = unset,
        variant_key: Union[str, UnsetType] = unset,
        variant_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Details of the variant result.

        :param assignment_count: Number of subjects assigned to this variant.
        :type assignment_count: int, optional

        :param experiment_id: ID of the experiment associated with this result.
        :type experiment_id: str, optional

        :param is_control: Whether this variant is the experiment's control.
        :type is_control: bool, optional

        :param metrics: Metrics reported for this variant.
        :type metrics: [ExperimentsVariantResultsV2DTODataAttributesMetricsItems], optional

        :param variant_key: Key that identifies the experiment variant.
        :type variant_key: str, optional

        :param variant_name: Display name of the experiment variant.
        :type variant_name: str, optional
        """
        if assignment_count is not unset:
            kwargs["assignment_count"] = assignment_count
        if experiment_id is not unset:
            kwargs["experiment_id"] = experiment_id
        if is_control is not unset:
            kwargs["is_control"] = is_control
        if metrics is not unset:
            kwargs["metrics"] = metrics
        if variant_key is not unset:
            kwargs["variant_key"] = variant_key
        if variant_name is not unset:
            kwargs["variant_name"] = variant_name
        super().__init__(kwargs)
