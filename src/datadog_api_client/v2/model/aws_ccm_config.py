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
    from datadog_api_client.v2.model.data_export_config import DataExportConfig


class AWSCcmConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.data_export_config import DataExportConfig

        return {
            "data_export_configs": ([DataExportConfig],),
        }

    attribute_map = {
        "data_export_configs": "data_export_configs",
    }

    def __init__(self_, data_export_configs: List[DataExportConfig], **kwargs):
        """
        AWS Cloud Cost Management config.

        :param data_export_configs: List of data export configurations for Cost and Usage Reports.
        :type data_export_configs: [DataExportConfig]
        """
        super().__init__(kwargs)

        self_.data_export_configs = data_export_configs
