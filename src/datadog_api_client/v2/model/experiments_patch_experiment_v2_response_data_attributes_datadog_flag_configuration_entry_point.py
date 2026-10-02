# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_datadog_entry_point_filter import ExperimentsDatadogEntryPointFilter


class ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPoint(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_datadog_entry_point_filter import (
            ExperimentsDatadogEntryPointFilter,
        )

        return {
            "filters": ([[ExperimentsDatadogEntryPointFilter]],),
            "measure_id": (str,),
        }

    attribute_map = {
        "filters": "filters",
        "measure_id": "measure_id",
    }

    def __init__(self_, filters: List[List[ExperimentsDatadogEntryPointFilter]], measure_id: str, **kwargs):
        """
        Datadog measure and filters used to select analyzed subjects.

        :param filters: Complete Datadog OR-of-ANDs entry-point filter expression.
        :type filters: [[ExperimentsDatadogEntryPointFilter]]

        :param measure_id: Datadog measure UUID.
        :type measure_id: str
        """
        super().__init__(kwargs)

        self_.filters = filters
        self_.measure_id = measure_id
