# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


class UpdateDeploymentRuleParamsDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "dry_run": (bool,),
            "name": (str,),
            "options": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
        }

    attribute_map = {
        "dry_run": "dry_run",
        "name": "name",
        "options": "options",
    }

    def __init__(self_, dry_run: bool, name: str, options: Any, **kwargs):
        """
        Parameters for updating a deployment rule.

        :param dry_run: Whether to run this rule in dry-run mode.
        :type dry_run: bool

        :param name: The name of the deployment rule.
        :type name: str

        :param options: Options for deployment rule response representing either faulty deployment detection or monitor options. The actual type is determined by the parent's 'type' field.
        :type options: bool, date, datetime, dict, float, int, list, str, UUID, none_type
        """
        super().__init__(kwargs)

        self_.dry_run = dry_run
        self_.name = name
        self_.options = options
