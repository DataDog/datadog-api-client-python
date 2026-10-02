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
    from datadog_api_client.v2.model.experiments_experiment_v2_dto_data_attributes_conclusion_outcome import (
        ExperimentsExperimentV2DTODataAttributesConclusionOutcome,
    )


class ExperimentsPatchExperimentV2ResponseDataAttributesConclusion(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_experiment_v2_dto_data_attributes_conclusion_outcome import (
            ExperimentsExperimentV2DTODataAttributesConclusionOutcome,
        )

        return {
            "decision_reason": (str, none_type),
            "outcome": (ExperimentsExperimentV2DTODataAttributesConclusionOutcome,),
            "summary": (str, none_type),
        }

    attribute_map = {
        "decision_reason": "decision_reason",
        "outcome": "outcome",
        "summary": "summary",
    }

    def __init__(
        self_,
        decision_reason: Union[str, none_type, UnsetType] = unset,
        outcome: Union[ExperimentsExperimentV2DTODataAttributesConclusionOutcome, none_type, UnsetType] = unset,
        summary: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Outcome and supporting text recorded when the experiment is concluded.

        :param decision_reason: Reason for the recorded decision.
        :type decision_reason: str, none_type, optional

        :param outcome: Recorded experiment outcome.
        :type outcome: ExperimentsExperimentV2DTODataAttributesConclusionOutcome, none_type, optional

        :param summary: Summary of the experiment conclusion.
        :type summary: str, none_type, optional
        """
        if decision_reason is not unset:
            kwargs["decision_reason"] = decision_reason
        if outcome is not unset:
            kwargs["outcome"] = outcome
        if summary is not unset:
            kwargs["summary"] = summary
        super().__init__(kwargs)
