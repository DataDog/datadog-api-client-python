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
    from datadog_api_client.v2.model.experiments_create_experiment_metric_group_v2_request_data_attributes_metrics_items import (
        ExperimentsCreateExperimentMetricGroupV2RequestDataAttributesMetricsItems,
    )


class ExperimentsCreateExperimentMetricGroupV2RequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_create_experiment_metric_group_v2_request_data_attributes_metrics_items import (
            ExperimentsCreateExperimentMetricGroupV2RequestDataAttributesMetricsItems,
        )

        return {
            "metrics": ([ExperimentsCreateExperimentMetricGroupV2RequestDataAttributesMetricsItems],),
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
        "metrics": "metrics",
        "migration_metadata": "migration_metadata",
        "name": "name",
    }

    def __init__(
        self_,
        name: str,
        metrics: Union[
            List[ExperimentsCreateExperimentMetricGroupV2RequestDataAttributesMetricsItems], UnsetType
        ] = unset,
        migration_metadata: Union[Any, UnsetType] = unset,
        **kwargs,
    ):
        """
        Name and metric selection for the new experiment metric group.

        :param metrics: Metrics to include in the experiment metric group.
        :type metrics: [ExperimentsCreateExperimentMetricGroupV2RequestDataAttributesMetricsItems], optional

        :param migration_metadata: Metadata associated with migration of this resource.
        :type migration_metadata: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param name: Display name of the experiment metric group.
        :type name: str
        """
        if metrics is not unset:
            kwargs["metrics"] = metrics
        if migration_metadata is not unset:
            kwargs["migration_metadata"] = migration_metadata
        super().__init__(kwargs)

        self_.name = name
