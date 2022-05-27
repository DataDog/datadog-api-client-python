# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsStepDetailWarning(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_warning_type import SyntheticsWarningType

        return {
            "message": (str,),
            "type": (SyntheticsWarningType,),
        }

    attribute_map = {
        "message": "message",
        "type": "type",
    }

    def __init__(self, message, type, *args, **kwargs):
        """
        Object collecting warnings for a given step.

        :param message: Message for the warning.
        :type message: str

        :param type: User locator used.
        :type type: SyntheticsWarningType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.message = message
        self.type = type

    @classmethod
    def _from_openapi_data(cls, message, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsStepDetailWarning, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.message = message
        self.type = type
        return self
