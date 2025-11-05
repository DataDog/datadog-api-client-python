# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.fleet_deployment_file_op import FleetDeploymentFileOp


class FleetDeploymentOperation(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_deployment_file_op import FleetDeploymentFileOp

        return {
            "file_op": (FleetDeploymentFileOp,),
            "file_path": (str,),
            "patch": (
                {
                    str: (
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
                    )
                },
            ),
        }

    attribute_map = {
        "file_op": "file_op",
        "file_path": "file_path",
        "patch": "patch",
    }

    def __init__(
        self_, file_op: FleetDeploymentFileOp, file_path: str, patch: Union[Dict[str, Any], UnsetType] = unset, **kwargs
    ):
        """
        A single configuration file operation to perform on the target hosts.

        :param file_op: Type of file operation to perform on the target configuration file.

            * ``merge-patch`` : Merges the provided patch data with the existing configuration file.
              Creates the file if it doesn't exist.
            * ``delete`` : Removes the specified configuration file from the target hosts.
        :type file_op: FleetDeploymentFileOp

        :param file_path: Absolute path to the target configuration file on the host.
        :type file_path: str

        :param patch: Patch data in JSON format to apply to the configuration file.
            When using ``merge-patch`` , this object is merged with the existing configuration,
            allowing you to add, update, or override specific fields without replacing the entire file.
            The structure must match the target configuration file format (for example, YAML structure
            for Datadog Agent config). Not applicable when using the ``delete`` operation.
        :type patch: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional
        """
        if patch is not unset:
            kwargs["patch"] = patch
        super().__init__(kwargs)

        self_.file_op = file_op
        self_.file_path = file_path
