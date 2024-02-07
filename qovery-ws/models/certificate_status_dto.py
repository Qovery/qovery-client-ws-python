# coding: utf-8

"""
    websocket-gateway

    Describe the weboscket endpoints

    The version of the OpenAPI document: 0.1.0
    Contact: erebe@erebe.eu
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from qovery-ws.models.service_state_dto import ServiceStateDto
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CertificateStatusDto(BaseModel):
    """
    CertificateStatusDto
    """ # noqa: E501
    dns_names: List[StrictStr]
    failed_issuance_attempt_count: Annotated[int, Field(strict=True, ge=0)]
    last_failure_issuance_time: Optional[StrictInt] = Field(default=None, description="Unix timestamp with millisecond precision")
    not_after: Optional[StrictInt] = Field(default=None, description="Unix timestamp with millisecond precision")
    not_before: Optional[StrictInt] = Field(default=None, description="Unix timestamp with millisecond precision")
    renewal_time: Optional[StrictInt] = Field(default=None, description="Unix timestamp with millisecond precision")
    state: ServiceStateDto
    state_message: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["dns_names", "failed_issuance_attempt_count", "last_failure_issuance_time", "not_after", "not_before", "renewal_time", "state", "state_message"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CertificateStatusDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if last_failure_issuance_time (nullable) is None
        # and model_fields_set contains the field
        if self.last_failure_issuance_time is None and "last_failure_issuance_time" in self.model_fields_set:
            _dict['last_failure_issuance_time'] = None

        # set to None if not_after (nullable) is None
        # and model_fields_set contains the field
        if self.not_after is None and "not_after" in self.model_fields_set:
            _dict['not_after'] = None

        # set to None if not_before (nullable) is None
        # and model_fields_set contains the field
        if self.not_before is None and "not_before" in self.model_fields_set:
            _dict['not_before'] = None

        # set to None if renewal_time (nullable) is None
        # and model_fields_set contains the field
        if self.renewal_time is None and "renewal_time" in self.model_fields_set:
            _dict['renewal_time'] = None

        # set to None if state_message (nullable) is None
        # and model_fields_set contains the field
        if self.state_message is None and "state_message" in self.model_fields_set:
            _dict['state_message'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CertificateStatusDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dns_names": obj.get("dns_names"),
            "failed_issuance_attempt_count": obj.get("failed_issuance_attempt_count"),
            "last_failure_issuance_time": obj.get("last_failure_issuance_time"),
            "not_after": obj.get("not_after"),
            "not_before": obj.get("not_before"),
            "renewal_time": obj.get("renewal_time"),
            "state": obj.get("state"),
            "state_message": obj.get("state_message")
        })
        return _obj


