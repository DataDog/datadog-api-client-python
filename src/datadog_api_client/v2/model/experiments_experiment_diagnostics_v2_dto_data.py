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
    from datadog_api_client.v2.model.experiments_experiment_diagnostics_v2_dto_data_attributes import (
        ExperimentsExperimentDiagnosticsV2DTODataAttributes,
    )
    from datadog_api_client.v2.model.experiments_experiment_diagnostics_v2_dto_data_type import (
        ExperimentsExperimentDiagnosticsV2DTODataType,
    )


class ExperimentsExperimentDiagnosticsV2DTOData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_experiment_diagnostics_v2_dto_data_attributes import (
            ExperimentsExperimentDiagnosticsV2DTODataAttributes,
        )
        from datadog_api_client.v2.model.experiments_experiment_diagnostics_v2_dto_data_type import (
            ExperimentsExperimentDiagnosticsV2DTODataType,
        )

        return {
            "attributes": (ExperimentsExperimentDiagnosticsV2DTODataAttributes,),
            "id": (UUID,),
            "type": (ExperimentsExperimentDiagnosticsV2DTODataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: UUID,
        type: ExperimentsExperimentDiagnosticsV2DTODataType,
        attributes: Union[ExperimentsExperimentDiagnosticsV2DTODataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Experiment diagnostics resource with its identifier and check results.

        :param attributes: Diagnostic check results and their evaluation state.
        :type attributes: ExperimentsExperimentDiagnosticsV2DTODataAttributes, optional

        :param id: Identifier of the experiment whose diagnostics are returned.
        :type id: UUID

        :param type: Experiment diagnostics resource type.
        :type type: ExperimentsExperimentDiagnosticsV2DTODataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
