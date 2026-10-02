# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_experiment_diagnostics_v2_dto_data_attributes_diagnostics_items_skipped_reason import (
        ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsSkippedReason,
    )
    from datadog_api_client.v2.model.experiments_experiment_diagnostics_v2_dto_data_attributes_diagnostics_items_status import (
        ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsStatus,
    )
    from datadog_api_client.v2.model.experiments_experiment_diagnostics_v2_dto_data_attributes_diagnostics_items_type import (
        ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType,
    )


class ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_experiment_diagnostics_v2_dto_data_attributes_diagnostics_items_skipped_reason import (
            ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsSkippedReason,
        )
        from datadog_api_client.v2.model.experiments_experiment_diagnostics_v2_dto_data_attributes_diagnostics_items_status import (
            ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsStatus,
        )
        from datadog_api_client.v2.model.experiments_experiment_diagnostics_v2_dto_data_attributes_diagnostics_items_type import (
            ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType,
        )

        return {
            "message": (str, none_type),
            "metric_id": (str, none_type),
            "skipped_reason": (ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsSkippedReason,),
            "status": (ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsStatus,),
            "title": (str,),
            "type": (ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType,),
        }

    attribute_map = {
        "message": "message",
        "metric_id": "metric_id",
        "skipped_reason": "skipped_reason",
        "status": "status",
        "title": "title",
        "type": "type",
    }

    def __init__(
        self_,
        status: ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsStatus,
        title: str,
        type: ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType,
        message: Union[str, none_type, UnsetType] = unset,
        metric_id: Union[str, none_type, UnsetType] = unset,
        skipped_reason: Union[
            ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsSkippedReason, none_type, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Result of one diagnostic check for an experiment.

        :param message: Explanation of the diagnostic check result.
        :type message: str, none_type, optional

        :param metric_id: Identifier of the metric associated with this check.
        :type metric_id: str, none_type, optional

        :param skipped_reason: Reason the diagnostic check could not be evaluated.
        :type skipped_reason: ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsSkippedReason, none_type, optional

        :param status: Outcome of an individual diagnostic check.
        :type status: ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsStatus

        :param title: Short title of the diagnostic check.
        :type title: str

        :param type: Kind of diagnostic check performed.
        :type type: ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType
        """
        if message is not unset:
            kwargs["message"] = message
        if metric_id is not unset:
            kwargs["metric_id"] = metric_id
        if skipped_reason is not unset:
            kwargs["skipped_reason"] = skipped_reason
        super().__init__(kwargs)

        self_.status = status
        self_.title = title
        self_.type = type
