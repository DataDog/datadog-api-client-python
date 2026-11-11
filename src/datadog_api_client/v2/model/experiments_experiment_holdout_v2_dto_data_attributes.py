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
    from datadog_api_client.v2.model.experiments_experiment_holdout_v2_dto_data_attributes_holdout_type import (
        ExperimentsExperimentHoldoutV2DTODataAttributesHoldoutType,
    )
    from datadog_api_client.v2.model.experiments_experiment_holdout_v2_dto_data_attributes_kind import (
        ExperimentsExperimentHoldoutV2DTODataAttributesKind,
    )
    from datadog_api_client.v2.model.experiments_experiment_holdout_v2_dto_data_attributes_state import (
        ExperimentsExperimentHoldoutV2DTODataAttributesState,
    )


class ExperimentsExperimentHoldoutV2DTODataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_experiment_holdout_v2_dto_data_attributes_holdout_type import (
            ExperimentsExperimentHoldoutV2DTODataAttributesHoldoutType,
        )
        from datadog_api_client.v2.model.experiments_experiment_holdout_v2_dto_data_attributes_kind import (
            ExperimentsExperimentHoldoutV2DTODataAttributesKind,
        )
        from datadog_api_client.v2.model.experiments_experiment_holdout_v2_dto_data_attributes_state import (
            ExperimentsExperimentHoldoutV2DTODataAttributesState,
        )

        return {
            "evaluation_order": (int, none_type),
            "holdout_type": (ExperimentsExperimentHoldoutV2DTODataAttributesHoldoutType,),
            "key": (str,),
            "kind": (ExperimentsExperimentHoldoutV2DTODataAttributesKind,),
            "name": (str,),
            "state": (ExperimentsExperimentHoldoutV2DTODataAttributesState,),
            "traffic_allocation": (float,),
        }

    attribute_map = {
        "evaluation_order": "evaluation_order",
        "holdout_type": "holdout_type",
        "key": "key",
        "kind": "kind",
        "name": "name",
        "state": "state",
        "traffic_allocation": "traffic_allocation",
    }

    def __init__(
        self_,
        evaluation_order: Union[int, none_type, UnsetType] = unset,
        holdout_type: Union[ExperimentsExperimentHoldoutV2DTODataAttributesHoldoutType, none_type, UnsetType] = unset,
        key: Union[str, UnsetType] = unset,
        kind: Union[ExperimentsExperimentHoldoutV2DTODataAttributesKind, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        state: Union[ExperimentsExperimentHoldoutV2DTODataAttributesState, UnsetType] = unset,
        traffic_allocation: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a holdout that the experiment is attached to.

        :param evaluation_order: Zero-based position of this MANAGED holdout in the experiment's evaluation order. The GLOBAL holdout is evaluated first. Null for EXTERNAL holdouts.
        :type evaluation_order: int, none_type, optional

        :param holdout_type: How Datadog serves a MANAGED holdout. GLOBAL holdouts apply to every eligible experiment of a subject type. SELECTIVE holdouts apply only to the experiments attached to them. Null for EXTERNAL holdouts.
        :type holdout_type: ExperimentsExperimentHoldoutV2DTODataAttributesHoldoutType, none_type, optional

        :param key: Key of the holdout.
        :type key: str, optional

        :param kind: Whether Datadog serves the holdout. Datadog serves MANAGED holdouts. EXTERNAL holdouts record what your own feature flagging system holds back, and Datadog does not serve them.
        :type kind: ExperimentsExperimentHoldoutV2DTODataAttributesKind, optional

        :param name: Display name of the holdout.
        :type name: str, optional

        :param state: Lifecycle phase of the holdout. PENDING holdouts have not started including experiments. INCLUDING holdouts are adding experiments. WAITING_FOR_ANALYSIS holdouts have stopped including experiments but have not started analysis. ANALYSING holdouts are in their analysis window. COMPLETE applies only to EXTERNAL holdouts that have ended their analysis window but are not archived.
        :type state: ExperimentsExperimentHoldoutV2DTODataAttributesState, optional

        :param traffic_allocation: Share of subjects the holdout holds back, from 0 to 1.
        :type traffic_allocation: float, optional
        """
        if evaluation_order is not unset:
            kwargs["evaluation_order"] = evaluation_order
        if holdout_type is not unset:
            kwargs["holdout_type"] = holdout_type
        if key is not unset:
            kwargs["key"] = key
        if kind is not unset:
            kwargs["kind"] = kind
        if name is not unset:
            kwargs["name"] = name
        if state is not unset:
            kwargs["state"] = state
        if traffic_allocation is not unset:
            kwargs["traffic_allocation"] = traffic_allocation
        super().__init__(kwargs)
