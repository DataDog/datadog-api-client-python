# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsStep(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_step_type import SyntheticsStepType

        return {
            "allow_failure": (bool,),
            "is_critical": (bool,),
            "name": (str,),
            "params": (dict,),
            "timeout": (int,),
            "type": (SyntheticsStepType,),
        }

    attribute_map = {
        "allow_failure": "allowFailure",
        "is_critical": "isCritical",
        "name": "name",
        "params": "params",
        "timeout": "timeout",
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        The steps used in a Synthetics browser test.

        :param allow_failure: A boolean set to allow this step to fail.
        :type allow_failure: bool, optional

        :param is_critical: A boolean to use in addition to ``allowFailure`` to determine if the test should be marked as failed when the step fails.
        :type is_critical: bool, optional

        :param name: The name of the step.
        :type name: str, optional

        :param params: The parameters of the step.
        :type params: dict, optional

        :param timeout: The time before declaring a step failed.
        :type timeout: int, optional

        :param type: Step type used in your Synthetic test.
        :type type: SyntheticsStepType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsStep, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
