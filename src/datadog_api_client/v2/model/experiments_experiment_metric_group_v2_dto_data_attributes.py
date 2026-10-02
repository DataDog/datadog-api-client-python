# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_experiment_metric_group_mutation_v2_data_attributes_metrics_items import (
        ExperimentsExperimentMetricGroupMutationV2DataAttributesMetricsItems,
    )


class ExperimentsExperimentMetricGroupV2DTODataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_experiment_metric_group_mutation_v2_data_attributes_metrics_items import (
            ExperimentsExperimentMetricGroupMutationV2DataAttributesMetricsItems,
        )

        return {
            "is_decision": (bool,),
            "metrics": ([ExperimentsExperimentMetricGroupMutationV2DataAttributesMetricsItems],),
            "migration_metadata": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "name": (str,),
        }

    attribute_map = {
        "is_decision": "is_decision",
        "metrics": "metrics",
        "migration_metadata": "migration_metadata",
        "name": "name",
    }

    def __init__(
        self_,
        is_decision: Union[bool, UnsetType] = unset,
        metrics: Union[List[ExperimentsExperimentMetricGroupMutationV2DataAttributesMetricsItems], UnsetType] = unset,
        migration_metadata: Union[Any, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Name, purpose, and selected metrics of an experiment metric group.

        :param is_decision: Whether this group contains the experiment decision metrics.
        :type is_decision: bool, optional

        :param metrics: Metrics selected for this experiment metric group.
        :type metrics: [ExperimentsExperimentMetricGroupMutationV2DataAttributesMetricsItems], optional

        :param migration_metadata: Metadata associated with migration of this resource.
        :type migration_metadata: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param name: Display name of the experiment metric group.
        :type name: str, optional
        """
        if is_decision is not unset:
            kwargs["is_decision"] = is_decision
        if metrics is not unset:
            kwargs["metrics"] = metrics
        if migration_metadata is not unset:
            kwargs["migration_metadata"] = migration_metadata
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
