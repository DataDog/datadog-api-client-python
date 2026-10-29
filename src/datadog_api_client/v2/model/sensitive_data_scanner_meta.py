# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
)


class SensitiveDataScannerMeta(ModelNormal):
    def __init__(self_, **kwargs):
        """
        Meta response. Always an empty object.
        """
        super().__init__(kwargs)
