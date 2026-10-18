# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
)


class SecurityMonitoringBatchMigrationResourceOutput(ModelNormal):
    _nullable = True

    def __init__(self_, **kwargs):
        """
        The translation output. When the resource is ``completed`` , a Cloud SIEM detection rule
        definition in the same format as the create detection rule API. When the resource is
        ``failed`` , an object with an ``error`` describing the failure, with ``kind`` set to
        ``translation_error`` or ``internal_error`` , and optional ``type`` and ``message``. Otherwise, null.
        """
        super().__init__(kwargs)
