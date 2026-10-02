# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_experiment_diagnostics_v2_dto_data_attributes_diagnostics_items import (
        ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItems,
    )
    from datadog_api_client.v2.model.experiments_experiment_diagnostics_v2_dto_data_attributes_result import (
        ExperimentsExperimentDiagnosticsV2DTODataAttributesResult,
    )
    from datadog_api_client.v2.model.experiments_experiment_diagnostics_v2_dto_data_attributes_state import (
        ExperimentsExperimentDiagnosticsV2DTODataAttributesState,
    )


class ExperimentsExperimentDiagnosticsV2DTODataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_experiment_diagnostics_v2_dto_data_attributes_diagnostics_items import (
            ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItems,
        )
        from datadog_api_client.v2.model.experiments_experiment_diagnostics_v2_dto_data_attributes_result import (
            ExperimentsExperimentDiagnosticsV2DTODataAttributesResult,
        )
        from datadog_api_client.v2.model.experiments_experiment_diagnostics_v2_dto_data_attributes_state import (
            ExperimentsExperimentDiagnosticsV2DTODataAttributesState,
        )

        return {
            "diagnostics": ([ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItems],),
            "evaluated_at": (datetime, none_type),
            "result": (ExperimentsExperimentDiagnosticsV2DTODataAttributesResult,),
            "state": (ExperimentsExperimentDiagnosticsV2DTODataAttributesState,),
        }

    attribute_map = {
        "diagnostics": "diagnostics",
        "evaluated_at": "evaluated_at",
        "result": "result",
        "state": "state",
    }

    def __init__(
        self_,
        diagnostics: List[ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItems],
        state: ExperimentsExperimentDiagnosticsV2DTODataAttributesState,
        evaluated_at: Union[datetime, none_type, UnsetType] = unset,
        result: Union[ExperimentsExperimentDiagnosticsV2DTODataAttributesResult, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Diagnostic check results and their evaluation state.

        :param diagnostics: Results of individual diagnostic checks.
        :type diagnostics: [ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItems]

        :param evaluated_at: Time when the diagnostic checks were evaluated.
        :type evaluated_at: datetime, none_type, optional

        :param result: Overall result of the experiment diagnostic checks.
        :type result: ExperimentsExperimentDiagnosticsV2DTODataAttributesResult, none_type, optional

        :param state: Current state of the diagnostic evaluation.
        :type state: ExperimentsExperimentDiagnosticsV2DTODataAttributesState
        """
        if evaluated_at is not unset:
            kwargs["evaluated_at"] = evaluated_at
        if result is not unset:
            kwargs["result"] = result
        super().__init__(kwargs)

        self_.diagnostics = diagnostics
        self_.state = state
