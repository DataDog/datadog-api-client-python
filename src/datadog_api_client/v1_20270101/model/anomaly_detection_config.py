# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.anomaly_detection_config_detection_sensitivity import (
        AnomalyDetectionConfigDetectionSensitivity,
    )


class AnomalyDetectionConfig(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.anomaly_detection_config_detection_sensitivity import (
            AnomalyDetectionConfigDetectionSensitivity,
        )

        return {
            "detection_sensitivity": (AnomalyDetectionConfigDetectionSensitivity,),
        }

    attribute_map = {
        "detection_sensitivity": "detection_sensitivity",
    }

    def __init__(self_, detection_sensitivity: AnomalyDetectionConfigDetectionSensitivity, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param detection_sensitivity: Test-only generated schema for the dashboard versioning proof of concept.
        :type detection_sensitivity: AnomalyDetectionConfigDetectionSensitivity
        """
        super().__init__(kwargs)

        self_.detection_sensitivity = detection_sensitivity
