# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class HostMetaInstallMethod(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "installer_version": (str,),
            "tool": (str,),
            "tool_version": (str,),
        }

    attribute_map = {
        "installer_version": "installer_version",
        "tool": "tool",
        "tool_version": "tool_version",
    }

    def __init__(self, *args, **kwargs):
        """
        Agent install method.

        :param installer_version: The installer version.
        :type installer_version: str, optional

        :param tool: Tool used to install the agent.
        :type tool: str, optional

        :param tool_version: The tool version.
        :type tool_version: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(HostMetaInstallMethod, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
