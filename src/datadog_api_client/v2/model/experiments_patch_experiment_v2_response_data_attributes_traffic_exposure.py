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
    from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_traffic_exposure_mode import (
        ExperimentsCreateExperimentV2RequestDataAttributesTrafficExposureMode,
    )
    from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_traffic_exposure_steps_items import (
        ExperimentsCreateExperimentV2RequestDataAttributesTrafficExposureStepsItems,
    )


class ExperimentsPatchExperimentV2ResponseDataAttributesTrafficExposure(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_traffic_exposure_mode import (
            ExperimentsCreateExperimentV2RequestDataAttributesTrafficExposureMode,
        )
        from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_traffic_exposure_steps_items import (
            ExperimentsCreateExperimentV2RequestDataAttributesTrafficExposureStepsItems,
        )

        return {
            "fraction": (float,),
            "mode": (ExperimentsCreateExperimentV2RequestDataAttributesTrafficExposureMode,),
            "steps": ([ExperimentsCreateExperimentV2RequestDataAttributesTrafficExposureStepsItems],),
        }

    attribute_map = {
        "fraction": "fraction",
        "mode": "mode",
        "steps": "steps",
    }

    def __init__(
        self_,
        mode: ExperimentsCreateExperimentV2RequestDataAttributesTrafficExposureMode,
        fraction: Union[float, UnsetType] = unset,
        steps: Union[
            List[ExperimentsCreateExperimentV2RequestDataAttributesTrafficExposureStepsItems], UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Traffic exposure fraction or schedule configured for the experiment.

        :param fraction: STATIC exposure fraction. Draft experiments can change this value. After start only warehouse experiments without a Datadog flag can change a STATIC fraction through the public API.
        :type fraction: float, optional

        :param mode: Whether exposure uses a fixed fraction or a sequence of steps.
        :type mode: ExperimentsCreateExperimentV2RequestDataAttributesTrafficExposureMode

        :param steps: Configured exposure plan rather than wall-clock history. At least two steps must have strictly increasing fractions and no gaps. Warehouse steps start at assignments_start_date and can use different durations. New Datadog plans have at most five steps and a first fraction above zero. Their nonfinal durations must be equal and exclude time paused. Datadog steps start with the experiment. Running warehouse experiments can replace step fractions, durations, and the exposure mode. After start, Datadog exposure plans cannot change through the public API. The final duration is null and its fraction holds until assignment ends.
        :type steps: [ExperimentsCreateExperimentV2RequestDataAttributesTrafficExposureStepsItems], optional
        """
        if fraction is not unset:
            kwargs["fraction"] = fraction
        if steps is not unset:
            kwargs["steps"] = steps
        super().__init__(kwargs)

        self_.mode = mode
