# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class SeverityOverrideAttributes(ModelComposed):
    def __init__(self, **kwargs):
        """
        Severity override to apply to the findings.
        Set ``action`` to ``set`` to apply a manual severity override with the given ``value``.
        Set ``action`` to ``clear`` to remove a manual severity override.

        :param action: The action that applies a manual severity override.
        :type action: SeverityOverrideSetActionType

        :param description: Additional information about the severity change. This field has a limit of 280 characters.
        :type description: str, optional

        :param value: Severity to apply to the findings.
            `info` sets the lowest severity the finding type allows.
        :type value: SeverityOverrideValue
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.severity_override_set import SeverityOverrideSet
        from datadog_api_client.v2.model.severity_override_clear import SeverityOverrideClear

        return {
            "oneOf": [
                SeverityOverrideSet,
                SeverityOverrideClear,
            ],
        }
