# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_configuration_source import (
        TimeseriesAnomalyInvestigationConfigurationSource,
    )


class TimeseriesAnomalyInvestigationDetection(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_configuration_source import (
            TimeseriesAnomalyInvestigationConfigurationSource,
        )

        return {
            "configuration_source": (TimeseriesAnomalyInvestigationConfigurationSource,),
            "profile": (str, none_type),
        }

    attribute_map = {
        "configuration_source": "configuration_source",
        "profile": "profile",
    }

    def __init__(
        self_,
        configuration_source: TimeseriesAnomalyInvestigationConfigurationSource,
        profile: Union[str, none_type],
        **kwargs,
    ):
        """
        Anomaly detection configuration used for the result.

        :param configuration_source: Source of the anomaly detection configuration.
        :type configuration_source: TimeseriesAnomalyInvestigationConfigurationSource

        :param profile: Applied Watchdog Explains profile, or null when the request supplied an explicit ``anomalies()`` formula. The current Watchdog profile is ``watchdog_explains_v1``.
        :type profile: str, none_type
        """
        super().__init__(kwargs)

        self_.configuration_source = configuration_source
        self_.profile = profile
