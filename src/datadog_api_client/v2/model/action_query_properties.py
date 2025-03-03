# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.action_query_condition import ActionQueryCondition
    from datadog_api_client.v2.model.action_query_debounce_in_ms import ActionQueryDebounceInMs
    from datadog_api_client.v2.model.action_query_mocked_outputs import ActionQueryMockedOutputs
    from datadog_api_client.v2.model.action_query_only_trigger_manually import ActionQueryOnlyTriggerManually
    from datadog_api_client.v2.model.action_query_polling_interval_in_ms import ActionQueryPollingIntervalInMs
    from datadog_api_client.v2.model.action_query_requires_confirmation import ActionQueryRequiresConfirmation
    from datadog_api_client.v2.model.action_query_show_toast_on_error import ActionQueryShowToastOnError
    from datadog_api_client.v2.model.action_query_spec import ActionQuerySpec
    from datadog_api_client.v2.model.action_query_mocked_outputs_object import ActionQueryMockedOutputsObject
    from datadog_api_client.v2.model.action_query_spec_object import ActionQuerySpecObject


class ActionQueryProperties(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.action_query_condition import ActionQueryCondition
        from datadog_api_client.v2.model.action_query_debounce_in_ms import ActionQueryDebounceInMs
        from datadog_api_client.v2.model.action_query_mocked_outputs import ActionQueryMockedOutputs
        from datadog_api_client.v2.model.action_query_only_trigger_manually import ActionQueryOnlyTriggerManually
        from datadog_api_client.v2.model.action_query_polling_interval_in_ms import ActionQueryPollingIntervalInMs
        from datadog_api_client.v2.model.action_query_requires_confirmation import ActionQueryRequiresConfirmation
        from datadog_api_client.v2.model.action_query_show_toast_on_error import ActionQueryShowToastOnError
        from datadog_api_client.v2.model.action_query_spec import ActionQuerySpec

        return {
            "condition": (ActionQueryCondition,),
            "debounce_in_ms": (ActionQueryDebounceInMs,),
            "mocked_outputs": (ActionQueryMockedOutputs,),
            "only_trigger_manually": (ActionQueryOnlyTriggerManually,),
            "outputs": (str,),
            "polling_interval_in_ms": (ActionQueryPollingIntervalInMs,),
            "requires_confirmation": (ActionQueryRequiresConfirmation,),
            "show_toast_on_error": (ActionQueryShowToastOnError,),
            "spec": (ActionQuerySpec,),
        }

    attribute_map = {
        "condition": "condition",
        "debounce_in_ms": "debounceInMs",
        "mocked_outputs": "mockedOutputs",
        "only_trigger_manually": "onlyTriggerManually",
        "outputs": "outputs",
        "polling_interval_in_ms": "pollingIntervalInMs",
        "requires_confirmation": "requiresConfirmation",
        "show_toast_on_error": "showToastOnError",
        "spec": "spec",
    }

    def __init__(
        self_,
        spec: Union[ActionQuerySpec, str, ActionQuerySpecObject],
        condition: Union[ActionQueryCondition, bool, str, UnsetType] = unset,
        debounce_in_ms: Union[ActionQueryDebounceInMs, float, str, UnsetType] = unset,
        mocked_outputs: Union[ActionQueryMockedOutputs, str, ActionQueryMockedOutputsObject, UnsetType] = unset,
        only_trigger_manually: Union[ActionQueryOnlyTriggerManually, bool, str, UnsetType] = unset,
        outputs: Union[str, UnsetType] = unset,
        polling_interval_in_ms: Union[ActionQueryPollingIntervalInMs, float, str, UnsetType] = unset,
        requires_confirmation: Union[ActionQueryRequiresConfirmation, bool, str, UnsetType] = unset,
        show_toast_on_error: Union[ActionQueryShowToastOnError, bool, str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The properties of the action query.

        :param condition: Whether to run this query. If specified, the query will only run if this condition evaluates to ``true`` in JavaScript and all other conditions are also met.
        :type condition: ActionQueryCondition, optional

        :param debounce_in_ms: The minimum time in milliseconds that must pass before the query can be triggered again. This is useful for preventing accidental double-clicks from triggering the query multiple times.
        :type debounce_in_ms: ActionQueryDebounceInMs, optional

        :param mocked_outputs: The mocked outputs of the action query. This is useful for testing the app without actually running the action.
        :type mocked_outputs: ActionQueryMockedOutputs, optional

        :param only_trigger_manually: Determines when this query is executed. If set to ``false`` , the query will run when the app loads and whenever any query arguments change. If set to ``true`` , the query will only run when manually triggered from elsewhere in the app.
        :type only_trigger_manually: ActionQueryOnlyTriggerManually, optional

        :param outputs: The post-query transformation function, which is a JavaScript function that changes the query's ``.outputs`` property after the query's execution.
        :type outputs: str, optional

        :param polling_interval_in_ms: If specified, the app will poll the query at the specified interval in milliseconds. The minimum polling interval is 15 seconds. The query will only poll when the app's browser tab is active.
        :type polling_interval_in_ms: ActionQueryPollingIntervalInMs, optional

        :param requires_confirmation: Whether to prompt the user to confirm this query before it runs.
        :type requires_confirmation: ActionQueryRequiresConfirmation, optional

        :param show_toast_on_error: Whether to display a toast to the user when the query returns an error.
        :type show_toast_on_error: ActionQueryShowToastOnError, optional

        :param spec: The definition of the action query.
        :type spec: ActionQuerySpec
        """
        if condition is not unset:
            kwargs["condition"] = condition
        if debounce_in_ms is not unset:
            kwargs["debounce_in_ms"] = debounce_in_ms
        if mocked_outputs is not unset:
            kwargs["mocked_outputs"] = mocked_outputs
        if only_trigger_manually is not unset:
            kwargs["only_trigger_manually"] = only_trigger_manually
        if outputs is not unset:
            kwargs["outputs"] = outputs
        if polling_interval_in_ms is not unset:
            kwargs["polling_interval_in_ms"] = polling_interval_in_ms
        if requires_confirmation is not unset:
            kwargs["requires_confirmation"] = requires_confirmation
        if show_toast_on_error is not unset:
            kwargs["show_toast_on_error"] = show_toast_on_error
        super().__init__(kwargs)

        self_.spec = spec
