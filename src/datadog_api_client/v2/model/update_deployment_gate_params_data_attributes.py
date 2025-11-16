# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UpdateDeploymentGateParamsDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "dry_run": (bool,),
        }

    attribute_map = {
        "dry_run": "dry_run",
    }

    def __init__(self_, dry_run: bool, **kwargs):
        """
        Attributes for updating a deployment gate.

        :param dry_run: Whether to run in dry-run mode.
        :type dry_run: bool
        """
        super().__init__(kwargs)

        self_.dry_run = dry_run
