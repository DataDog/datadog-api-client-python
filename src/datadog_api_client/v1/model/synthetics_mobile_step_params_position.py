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
    from datadog_api_client.v1.model.synthetics_mobile_step_params_position_positions_items import (
        SyntheticsMobileStepParamsPositionPositionsItems,
    )


class SyntheticsMobileStepParamsPosition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_mobile_step_params_position_positions_items import (
            SyntheticsMobileStepParamsPositionPositionsItems,
        )

        return {
            "positions": ([SyntheticsMobileStepParamsPositionPositionsItems],),
        }

    attribute_map = {
        "positions": "positions",
    }

    def __init__(
        self_, positions: Union[List[SyntheticsMobileStepParamsPositionPositionsItems], UnsetType] = unset, **kwargs
    ):
        """
        The definition of ``SyntheticsMobileStepParamsPosition`` object.

        :param positions: The ``position`` ``positions``.
        :type positions: [SyntheticsMobileStepParamsPositionPositionsItems], optional
        """
        if positions is not unset:
            kwargs["positions"] = positions
        super().__init__(kwargs)
